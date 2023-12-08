package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.ImageView;

public class DisplayActivity extends AppCompatActivity {

    ImageView imageview;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_display);

        imageview=findViewById(R.id.imageview);

        Bundle extras=getIntent().getExtras();
        if(extras!=null){
            String gender=extras.getString("gender");
            if("male".equals(gender)){
                imageview.setImageResource(R.drawable.img_1);
            }else if("female".equals(gender)){
                imageview.setImageResource(R.drawable.img);
            }
        }
    }
}
