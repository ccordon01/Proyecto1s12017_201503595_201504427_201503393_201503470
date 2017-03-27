package com.grupo7.proy1.edd.proy1v2;

import android.app.AlertDialog;
import android.content.DialogInterface;
import android.content.Intent;
import android.os.Build;
import android.os.StrictMode;
import android.support.annotation.RequiresApi;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.EditText;
import android.widget.TextView;

import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import java.io.IOException;
import java.io.UnsupportedEncodingException;
import java.util.ArrayList;
import java.util.List;

import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.ClientProtocolException;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.message.BasicNameValuePair;

import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;
import android.app.Activity;
import android.os.Bundle;
import android.util.Log;
import android.widget.Toast;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.UnsupportedEncodingException;
import java.net.URL;
import java.net.URLConnection;
import java.net.URLEncoder;

/*import okhttp3.HttpUrl;
import okhttp3.Request;
import okhttp3.MediaType;
import okhttp3.OkHttpClient;
import okhttp3.Request;
import okhttp3.RequestBody;
import okhttp3.Response;*/
public class Login extends AppCompatActivity {
    public OkHttpClient webClient = new OkHttpClient();
    EditText empresa, depto, login, pass;
    public String titulo = "";
    public int aviso =0;
    SessionManager session;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
        StrictMode.setThreadPolicy(policy);
        session = new SessionManager(getApplicationContext());
        Toast.makeText(getApplicationContext(), "User Login Status: " + session.isLoggedIn(), Toast.LENGTH_LONG).show();
        super.onCreate(savedInstanceState);
        setContentView(R.layout.a_login);
        empresa      =   (EditText)findViewById(R.id.txtempre);
        depto      =   (EditText)findViewById(R.id.txtdep);
        login      =    (EditText)findViewById(R.id.txtusu);
        pass       =   (EditText)findViewById(R.id.txtcontra);
    }

    @RequiresApi(api = Build.VERSION_CODES.KITKAT)
    public void onClickLogin(View v) {
        Log.d("Evento PostRequest: ","Boton presionado");
        String desc = "";
        RequestBody formBody = new FormEncodingBuilder()
                .add("emp", empresa.getText().toString())
                .add("depto", depto.getText().toString())
                .add("user", login.getText().toString())
                .add("pass", pass.getText().toString())
                .build();
        String r = getString("login", formBody);
        System.out.println(r);
        if(("Bienvenido "+login.getText().toString()).equals(r)){
            titulo = "Sesion Iniciada";
            aviso =android.R.drawable.ic_dialog_info;
        }
        else{
            titulo = "Error";
            aviso =android.R.drawable.ic_dialog_alert;
        }
        desc=r;
        AlertDialog.Builder builder = new AlertDialog.Builder(this);

        builder.setTitle(titulo)
                .setIcon(
                        getResources().getDrawable(aviso))
                .setMessage(desc)
                .setNeutralButton(android.R.string.ok, new DialogInterface.OnClickListener() {

                    @Override
                    public void onClick(DialogInterface arg0, int arg1) {
                        if(titulo!="Error"){
                            session.createLoginSession(login.getText().toString(), pass.getText().toString(),empresa.getText().toString(),depto.getText().toString());
                            Intent i = new Intent(getApplicationContext(),Main.class);
                            startActivity(i);
                            setContentView(R.layout.main);
                            finish();
                        }
                    }
                });

        builder.create();
        builder.show();
        //OkHttpClient client = new OkHttpClient();
            //Request request = new Request.Builder()
              //      .url("http://192.168.1.237:5000/e")
                //    .build();

            /*try (Response response = client.newCall(request).execute()) {
                //return response.body().string();
            } catch (IOException e) {
                e.printStackTrace();
            }*/
        /*HttpUrl.Builder urlBuilder = HttpUrl.parse("http://192.168.1.237:5000/python").newBuilder();
        urlBuilder.addQueryParameter("v", "1.0");
        urlBuilder.addQueryParameter("user", "vogella");
        String url = urlBuilder.build().toString();

        Request request = new Request.Builder()
                .url(url)
                .build();*/
        //makePostRequest();
        /*String data = null;
        try {
            data = URLEncoder.encode("empresa", "UTF-8")
                    + "=" + URLEncoder.encode(empresa.getText().toString(), "UTF-8");

            data += "&" + URLEncoder.encode("depto", "UTF-8") + "="
                    + URLEncoder.encode(depto.getText().toString(), "UTF-8");

            data += "&" + URLEncoder.encode("user", "UTF-8")
                    + "=" + URLEncoder.encode(login.getText().toString(), "UTF-8");

            data += "&" + URLEncoder.encode("pass", "UTF-8")
                    + "=" + URLEncoder.encode(pass.getText().toString(), "UTF-8");
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }

        String text = "";
        BufferedReader reader=null;

        // Send data
        try
        {

            // Defined URL  where to send data
            URL url = new URL("http://192.168.1.237:5000/python");

            // Send POST data request

            URLConnection conn = url.openConnection();
            conn.setDoOutput(true);
            OutputStreamWriter wr = new OutputStreamWriter(conn.getOutputStream());
            wr.write( data );
            wr.flush();

            // Get the server response

            reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            StringBuilder sb = new StringBuilder();
            String line = null;

            // Read Server Response
            while((line = reader.readLine()) != null)
            {
                // Append server response in string
                sb.append(line + "\n");
            }

            text = sb.toString();
            System.out.println(text);
        }
        catch(Exception ex)
        {

        }
        finally
        {
            try
            {

                reader.close();
            }

            catch(Exception ex) {}
        }
        /*Intent i = new Intent(getApplicationContext(),Main.class);
        startActivity(i);
        setContentView(R.layout.main);*/
    }
    private void makePostRequest() {

        Log.d("Evento PostRequest: ","Inicia");
        HttpClient httpClient = new DefaultHttpClient();
        // replace with your url
        HttpPost httpPost = new HttpPost("http://192.168.1.237:5000/python");


        //Post Data
        List<NameValuePair> nameValuePair = new ArrayList<NameValuePair>(2);
        nameValuePair.add(new BasicNameValuePair("username", "test_user"));
        nameValuePair.add(new BasicNameValuePair("password", "123456789"));


        //Encoding POST data
        try {

            Log.d("Evento PostRequest: ","Envio informacion");
            httpPost.setEntity(new UrlEncodedFormEntity(nameValuePair));
        } catch (UnsupportedEncodingException e) {
            // log exception
            e.printStackTrace();
        }

        //making POST request.
        try {
            HttpResponse response = httpClient.execute(httpPost);
            // write response to log
            Log.d("Http Post Response:", response.toString());
        } catch (ClientProtocolException e) {
            // Log exception
            e.printStackTrace();
        } catch (IOException e) {
            // Log exception
            e.printStackTrace();
        }

    }
    public String getString(String metodo, RequestBody formBody) {

        try {
            URL url = new URL("http://192.168.1.237:5000/" + metodo);
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Login.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Login.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }
}
