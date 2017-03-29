package Service;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
/**
 *
 * @author Flinttloco
 */
import com.squareup.okhttp.FormEncodingBuilder;
import com.squareup.okhttp.OkHttpClient;
import com.squareup.okhttp.Request;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.Response;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.logging.Level;

public class WebService {

    public static OkHttpClient webClient = new OkHttpClient();

    public static String Login(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/Login");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Registrarse(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/Registro");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Activos(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/ConsultarActs");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Activ(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/ConsulAct");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Agregar(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/AgregarActivo");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Eliminar(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/EliminarActivo");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

    public static String Modificar(RequestBody formBody) {

        try {
            URL url = new URL("http://127.0.0.1:5000/ModificarActivo");
            Request request = new Request.Builder().url(url).post(formBody).build();
            Response response = webClient.newCall(request).execute();//Aqui obtiene la respuesta en dado caso si hayas pues un return en python
            String response_string = response.body().string();//y este seria el string de las respuesta
            return response_string;
        } catch (MalformedURLException ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        } catch (Exception ex) {
            java.util.logging.Logger.getLogger(Service.WebService.class.getName()).log(Level.SEVERE, null, ex);
        }
        return null;
    }

}
