package com.example.lareacirclerectangle;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

public class MainActivity extends AppCompatActivity {

    private EditText inputDimension1, inputDimension2;
    private Button calculateButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        inputDimension1 = findViewById(R.id.dimension1);
        inputDimension2 = findViewById(R.id.dimension2);
        calculateButton = findViewById(R.id.calculate_button);

        calculateButton.setOnClickListener(view -> {
            double dimension1 = getDimensionValue(inputDimension1);
            double dimension2 = getDimensionValue(inputDimension2);

            if (dimension1 == 0 || dimension2 == 0) {
                Intent intent = new Intent(MainActivity.this, ResultActivity.class);
                intent.putExtra("area", Math.PI * Math.pow(Math.max(dimension1, dimension2), 2));
                startActivity(intent);
            } else {
                Intent intent = new Intent(MainActivity.this, ResultActivity.class);
                intent.putExtra("area", dimension1 * dimension2);
                startActivity(intent);
            }
        });
    }

    private double getDimensionValue(EditText editText) {
        String text = editText.getText().toString();
        return Double.parseDouble(text.isEmpty() ? "0" : text);
    }
}
