from sentence_transformers import SentenceTransformer, util
import spacy
import os

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

model_name = "all-mpnet-base-v2"
model = SentenceTransformer(model_name)
paragrah_seg = spacy.load("en_core_web_sm")

def segment_paragraph(paragraph):
    doc = paragrah_seg(paragraph)
    res = []
    for sentence in doc.sents:
        res.append(sentence.text.strip())
    return res

def semantic_senetence_similarity(s1, s2):
    embeddings1 = model.encode(s1)
    embeddings2 = model.encode(s2)
    cosine_score = util.cos_sim(embeddings1, embeddings2)
    return cosine_score[0][0]

def match_answer_with_key(answer, key, threshold=0.5):
    segmented_answer_sentences = segment_paragraph(answer)
    segmented_key_sentences = segment_paragraph(key)
    sentence_covereded_in_answer = [False for _ in range(len(segmented_key_sentences))]
    matched_sentences = []
    for answer_sentence in segmented_answer_sentences:
        for key_sentence in segmented_key_sentences:
            similarity = semantic_senetence_similarity(answer_sentence, key_sentence)
            if similarity > threshold:
                sentence_covereded_in_answer[segmented_key_sentences.index(key_sentence)] = True
                obj = {
                    "answer_sentence": answer_sentence,
                    "key_sentence": key_sentence,
                    "similarity_score": similarity.item(),
                }
                matched_sentences.append(obj)

    key_sentences_not_in_answer = [
        segmented_key_sentences[i]
        for i in range(len(segmented_key_sentences))
        if sentence_covereded_in_answer[i] == False
    ]
    key_sentences_in_answer = [
        segmented_key_sentences[i]
        for i in range(len(segmented_key_sentences))
        if sentence_covereded_in_answer[i] == True
    ]

    total_len = sum(len(sent) for sent in segmented_key_sentences)
    sum_ = 0
    for i in range(len(segmented_key_sentences)):
        if sentence_covereded_in_answer[i] == True:
            sum_ += len(segmented_key_sentences[i])
    final_score = 10 * sum_ / total_len
    final_dict = {
        "semantic_score": final_score,
        "key_sentences_not_in_answer": key_sentences_not_in_answer,
        "key_sentences_in_answer": key_sentences_in_answer,
        "matched_sentences": matched_sentences,
    }
    return final_dict
