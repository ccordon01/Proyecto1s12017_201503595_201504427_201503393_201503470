<%-- 
    Document   : AgregarActivos
    Created on : 23/03/2017, 11:45:11 AM
    Author     : Flinttloco
--%>


<%@page import="Service.Alfanumerico"%>
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
        <title>Agregar Activos</title>
        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Agregar/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Agregar/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Agregar/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Agregar/css/style.css">

        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->

        <!-- Favicon and touch icons -->

        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Estilos/Agregar/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Estilos/Agregar/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Estilos/Agregar/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="Estilos/Agregar/ico/apple-touch-icon-57-precomposed.png">

    </head>

    <body>

        <!-- Top content -->
        <div class="top-content" align="left">

            <div class="inner-bg">
                <div class="container">
                    <div class="row">

                        <h1> AGREGAR ACTIVOS</h1>
                        <%
                        String Usuario = (String)session.getAttribute("NomUs");
                        String Empresa = (String)session.getAttribute("NomEmp");
                        String Departamento = (String)session.getAttribute("NomDept");
                        %>
                    </div>
                    <div class="row">
                        <div class="col-sm-5 col-sm-offset-3 form-box">
                            <div class="form-top">
                                <div class="form-top-left">

                                    <p>Crea un nuevo activo disponibles</p>
                                </div>

                            </div>
                            <div class="form-bottom">
                                <form role="form" action="AgregarActivo.jsp" method="post" class="login-form">
                                  
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtNombre" placeholder="Nombre" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtDescripcion" placeholder="Descripcion" class="form-username form-control" id="form-username">
                                    </div>
                                    <button type="submit" class="btn">Agregar Activo</button>
                                </form>
                            </div>
                            <!-- Codigo en Java -->
                            <%
                                WebService solicitud = new WebService();
                                Alfanumerico AlfaNum = new Alfanumerico();
                                
                                
                                String CodAct = AlfaNum.Codigo();
                                String NomAct = request.getParameter("txtNombre");
                                String DescripAct = request.getParameter("txtDescripcion");
                               

                                if (NomAct != null && DescripAct != null ) {

                                    RequestBody formBody = new FormEncodingBuilder()
                                            .add("txtUsuario", Usuario)
                                            .add("txtEmpresa", Empresa)
                                            .add("txtDeartamento", Departamento)
                                            .add("txtCodigo", CodAct)
                                            .add("txtNombre", NomAct)
                                            .add("txtDescripcion", DescripAct)
                                            .build();
                                    String r = solicitud.Agregar(formBody);
                                    System.out.println(r + "---");
                                    if (r.equalsIgnoreCase("True")) {
                                        String a = "Activo Agregado";
                                        out.println("<script>");
                                        out.println("alert('" + a + "');");
                                        out.println("</script>");
                                        
                                    } else {
                                        String a = "No se puedo Agregar el Activo";
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
                            <h3>    Iniciado como: Marco</h3>
                            <div class="social-login-buttons">

                                <a class="btn btn-link-2" href="MenuPrincipal.jsp">
                                    Regresar al Menu Principal
                                </a>

                            </div>

                        </div>
                    </div>
                </div>
            </div>

        </div>


        <!-- Javascript -->
        <script src="Estilos/Agregar/js/jquery-1.11.1.min.js"></script>
        <script src="Estilos/Agregar/bootstrap/js/bootstrap.min.js"></script>
        <script src="Estilos/Agregar/js/jquery.backstretch.min.js"></script>
        <script src="Estilos/Agregar/js/scripts.js"></script>

        <!--[if lt IE 10]>
            <script src="assets/js/placeholder.js"></script>
        <![endif]-->

    </body>

</html>