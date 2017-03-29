<%-- 
    Document   : Login
    Created on : 23/03/2017, 07:44:08 AM
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
        <title>Login</title>
        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Login/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Login/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Login/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Login/css/style.css">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

        <!-- Favicon and touch icons -->

        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Estilos/Login/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Estilos/Login/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Estilos/Login/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="Estilos/Login/ico/apple-touch-icon-57-precomposed.png">

    </head>

    <body>
        <%
            session.removeAttribute("NomUs");
            session.removeAttribute("NomEmp");
            session.removeAttribute("NomDept");
            session.removeAttribute("Codi");
        %>
        <!-- Top content -->
        <div class="top-content" align="left">

            <div class="inner-bg">
                <div class="container">
                    <div class="row">

                        <h1><strong>INICIAR</strong> SESION</h1>

                    </div>
                    <div class="row">
                        <div class="col-sm-5 col-sm-offset-3 form-box">
                            <div class="form-top">
                                <div class="form-top-left">

                                    <p>Entra y administra tus activos</p>
                                </div>

                            </div>
                            <div class="form-bottom">
                                <form role="form" action="" method="post" class="login-form">
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtUsuario" placeholder="Usuario" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-password">Password</label>
                                        <input type="password" name="txtPassword" placeholder="Contraseña" class="form-password form-control" id="form-password">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtEmpresa" placeholder="Empresa" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtDepartamento" placeholder="Departamento" class="form-username form-control" id="form-username">
                                    </div>
                                    <button type="submit" class="btn">Iniciar Sesion</button>
                                </form>
                            </div>
                            <!-- Codigo en Java -->
                            <%
                                WebService solicitud = new WebService();

                                String Usr = request.getParameter("txtUsuario");
                                String Pass = request.getParameter("txtPassword");
                                String Emp = request.getParameter("txtEmpresa");
                                String Dept = request.getParameter("txtDepartamento");

                                if (Usr != null && Pass != null && Emp != null && Dept != null) {

                                    RequestBody formBody = new FormEncodingBuilder()
                                            .add("txtUsuario", Usr)
                                            .add("txtContraseña", Pass)
                                            .add("txtEmpresa", Emp)
                                            .add("txtDeartamento", Dept)
                                            .build();
                                    String r = solicitud.Login(formBody);
                                    System.out.println(r + "---");
                                    if (r.equalsIgnoreCase("True")) {

                                        //Variables de Sesion
                                        session.setAttribute("NomUs", Usr);
                                        session.setAttribute("NomEmp", Emp);
                                        session.setAttribute("NomDept", Dept);

                                        response.sendRedirect("MenuPrincipal.jsp");
                                    } else {
                                        String a = "Datos Incorrectos";
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
                            <h3>¿Aun no tienes cuenta? Registrate</h3>
                            <div class="social-login-buttons">

                                <a class="btn btn-link-2" href="Registro.jsp">
                                    Registrar Usuario
                                </a>

                            </div>

                        </div>
                    </div>
                </div>
            </div>

        </div>


        <!-- Javascript -->
        <script src="Estilos/Login/js/jquery-1.11.1.min.js"></script>
        <script src="Estilos/Login/bootstrap/js/bootstrap.min.js"></script>
        <script src="Estilos/Login/js/jquery.backstretch.min.js"></script>
        <script src="Estilos/Login/js/scripts.js"></script>

        <!--[if lt IE 10]>
            <script src="assets/js/placeholder.js"></script>
        <![endif]-->

    </body>

</html>