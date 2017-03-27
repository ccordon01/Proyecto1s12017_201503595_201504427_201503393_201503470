package com.grupo7.proy1.edd.proy1v2;

import android.content.Intent;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Toast;

import java.util.HashMap;

public class Main extends AppCompatActivity {
    SessionManager session;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main);
        session = new SessionManager(getApplicationContext());
        Toast.makeText(getApplicationContext(), "User Login Status: " + session.isLoggedIn(), Toast.LENGTH_LONG).show();
        session.checkLogin();

        // get user data from session
        HashMap<String, String> user = session.getUserDetails();

        // name
        String name = user.get(SessionManager.KEY_NAME);


    }

    public void onClickRentar(View v) {
        Intent i = new Intent(getApplicationContext(),Renta.class);
        startActivity(i);
        setContentView(R.layout.renta);;

    }

    public void onClickDev(View v) {
        Intent i = new Intent(getApplicationContext(),Dev.class);
        startActivity(i);
        setContentView(R.layout.dev);
    }

    public void onClickLogout(View v) {
        Intent i = new Intent(getApplicationContext(),Login.class);
        startActivity(i);
        setContentView(R.layout.a_login);
    }
}
