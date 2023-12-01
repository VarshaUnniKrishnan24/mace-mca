package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.LinearLayout;

public class MainActivity extends AppCompatActivity implements View.OnClickListener {
    ImageView i1;
    LinearLayout ll1;
    Button b1;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        i1 = (ImageView)findViewById(R.id.img1);
        b1 = (Button) findViewById(R.id.b1);
        ll1 = (LinearLayout) findViewById(R.id.ll1);
        i1.setOnClickListener(this);
        b1.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        if (v.getId()==R.id.img1){
            i1.setVisibility(View.GONE);
            ll1.setVisibility(View.VISIBLE);
        }
        else if (v.getId()==R.id.b1){
            i1.setVisibility(View.VISIBLE);
            ll1.setVisibility(View.GONE);
        }
    }
}
