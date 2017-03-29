<%-- 
    Document   : Registro
    Created on : 23/03/2017, 08:13:42 AM
    Author     : Flinttloco
--%>


<%@page import="Service.WebService"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<%@page  import ="com.squareup.okhttp.RequestBody" %>
<%@page import="com.squareup.okhttp.FormEncodingBuilder"%>
<!DOCTYPE html>
<html lang="en">

    <head>

        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Registrarse</title>
        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Registro/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Registro/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Registro/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Registro/css/style.css">
        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Estilos/Registro/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Estilos/Registro/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Estilos/Registro/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="Estilos/Registro/ico/apple-touch-icon-57-precomposed.png">

    </head>

    <body>

        <!-- Top content -->
        <div class="top-content" align="left">

            <div class="inner-bg">
                <div class="container">
                    <div class="row">

                        <h1><strong>CREAR</strong> CUENTA</h1>

                    </div>
                    <div class="row">
                        <div class="col-sm-5 col-sm-offset-3 form-box">
                            <div class="form-top">
                                <div class="form-top-left">

                                    <p>Registrate y pon a disposicion tus activos</p>
                                </div>

                            </div>
                            <div class="form-bottom">
                                <form role="form" action="Registro.jsp" method="post" class="login-form">
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtUsuario" placeholder="Nombre de Usuario" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-password">Password</label>
                                        <input type="password" name="txtPassword" placeholder="Contraseña" class="form-password form-control" id="form-password">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtNombre" placeholder="Nombre Completo" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtEmpresa" placeholder="Empresa para la que trabaja" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtDepartamento" placeholder="Departamento en el que trabaja" class="form-username form-control" id="form-username">
                                    </div>
                                    <button type="submit" class="btn">Registrarse</button>
                                </form>
                            </div>
                            <!-- Codigo en Java -->
                            <%
                                WebService solicitud = new WebService();

                                String Usr = request.getParameter("txtUsuario");
                                String Pass = request.getParameter("txtPassword");
                                String Emp = request.getParameter("txtEmpresa");
                                String Dept = request.getParameter("txtDepartamento");
                                String Nom = request.getParameter("txtNombre");
                                
                                if (Usr != null && Pass != null && Emp != null && Dept != null) {

                                    RequestBody formBody = new FormEncodingBuilder()
                                            .add("txtUsuario", Usr)
                                            .add("txtContraseña", Pass)
                                            .add("txtEmpresa", Emp)
                                            .add("txtDeartamento", Dept)
                                            .add("txtNombre",Nom)
                                            .build();
                                    String r = solicitud.Registrarse(formBody);
                                    System.out.println(r + "---");
                                    
                                    if (r.equalsIgnoreCase("True")) {
                                        
                                          String a = "Registro Correcto";
                                        out.println("<script>");
                                        out.println("alert('" + a + "');");
                                        out.println("</script>");
                                        
                                       
                                    } else {
                                        String a = "Registro Incorrecto";
                                        out.println("<script>");
                                        out.println("alert('" + a + "');");
                                        out.println("</script>");
                                    }
                                    
                                }


                            %>
                        </div>
                    </div>
                    <div class="row">

                        <div class="col-sm-6 col-sm-offset-3 social-login">
                            <h3>¿Ya te Registraste? Inicia Sesion</h3>
                            <div class="social-login-buttons">

                                <a class="btn btn-link-2" href="IniciarSesion.jsp">
                                    Iniciar Sesion
                                </a>

                            </div>

                        </div>
                    </div>
                </div>
            </div>

        </div>


        <!-- Javascript -->
        <script src="Estilos/Registro/js/jquery-1.11.1.min.js"></script>
        <script src="Estilos/Registro/bootstrap/js/bootstrap.min.js"></script>
        <script src="Estilos/Registro/js/jquery.backstretch.min.js"></script>
        <script src="Estilos/Registro/js/scripts.js"></script>

        <!--[if lt IE 10]>
            <script src="assets/js/placeholder.js"></script>
        <![endif]-->

    </body>

</html>