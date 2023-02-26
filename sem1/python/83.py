import csv
try:
    with open('csv2.csv','w+',newline='') as outf:
        fieldnames=['Rollno','Name']
        content=csv.DictWriter(outf,fieldnames=fieldnames)
        content.writeheader()
        content.writerow({'Rollno':'1','Name':'Aadila'})
        content.writerow({'Rollno':'2','Name':'Aleena'})
        content.writerow({'Rollno':'3','Name':'Ameena'})
        content.writerow({'Rollno':'4','Name':'Anjaly'})
        print('csv2.csv : ')
        outf.seek(0,0)
        print(outf.read())
except Exception as e:
    print(e)
