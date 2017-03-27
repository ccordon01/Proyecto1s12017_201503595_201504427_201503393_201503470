package com.grupo7.proy1.edd.proy1v2;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class Dev extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.dev);
    }

    public void onClickMenu(View v) {
        Intent i = new Intent(getApplicationContext(),Main.class);
        startActivity(i);
        setContentView(R.layout.main);
    }

    public void onClickDev(View v) {
        Intent i = new Intent(getApplicationContext(),Main.class);
        startActivity(i);
        setContentView(R.layout.main);
    }
}
