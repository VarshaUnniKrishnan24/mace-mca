package com.example.myapplication;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;

public class MainActivity extends AppCompatActivity {
    EditText edittextname;
    Spinner spinnergender;
    Button btnsubmit;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        EditText edittextname=findViewById(R.id.edittextname);
        Spinner spinnergender=findViewById(R.id.spinnergender);
        Button btnsubmit=findViewById(R.id.btnsubmit);

        ArrayAdapter<CharSequence> adapter=ArrayAdapter.createFromResource(this,R.array.gender_array, android.R.layout.simple_spinner_item);
        adapter.setDropDownViewResource(android.R.layout.simple_dropdown_item_1line);
        spinnergender.setAdapter(adapter);

        btnsubmit.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String name=edittextname.getText().toString();
                String gender=spinnergender.getSelectedItem().toString();

                Intent intent=new Intent(MainActivity.this,DisplayActivity.class);
                intent.putExtra("name",name);
                intent.putExtra("gender",gender);
                startActivity(intent);
            }
        });
    }
}
