<%-- 
    Document   : ModificarActivo
    Created on : 23/03/2017, 11:46:07 AM
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
        <title>Modificar Activos</title>
        <!-- CSS -->
        <link rel="stylesheet" href="http://fonts.googleapis.com/css?family=Roboto:400,100,300,500">
        <link rel="stylesheet" href="Estilos/Login2/bootstrap/css/bootstrap.min.css">
        <link rel="stylesheet" href="Estilos/Login2/font-awesome/css/font-awesome.min.css">
        <link rel="stylesheet" href="Estilos/Login2/css/form-elements.css">
        <link rel="stylesheet" href="Estilos/Login2/css/style.css">

        <link rel="apple-touch-icon-precomposed" sizes="144x144" href="Estilos/Login2/ico/apple-touch-icon-144-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="114x114" href="Estilos/Login2/ico/apple-touch-icon-114-precomposed.png">
        <link rel="apple-touch-icon-precomposed" sizes="72x72" href="Estilos/Login2/ico/apple-touch-icon-72-precomposed.png">
        <link rel="apple-touch-icon-precomposed" href="Estilos/Login2/ico/apple-touch-icon-57-precomposed.png">
        <script type="text/javascript">
            var mostrarValor = function (foo, bar) {
                document.getElementById('txtcod').value = foo;
            };
        </script>
    </head>

    <body>

        <%
            //CONSULTA PARA TODOS LOS ACTIVOS DEL USUARIO

            String Usuario = (String) session.getAttribute("NomUs");
            String Empresa = (String) session.getAttribute("NomEmp");
            String Departamento = (String) session.getAttribute("NomDept");
            WebService solicitud = new WebService();

            RequestBody formBody = new FormEncodingBuilder()
                    .add("txtUsuario", Usuario)
                    .add("txtEmpresa", Empresa)
                    .add("txtDeartamento", Departamento)
                    .build();
            String r = solicitud.Activos(formBody);
            //System.out.println(r + "---");
            String[] separada = r.split(",");
        %>

        <input type="text" name="Prueba" id="Prueba" value="" size="12" readonly="readonly" />


        <!-- Top content -->
        <div class="top-content" align="left">

            <div class="inner-bg">
                <div class="container">
                    <div class="row"><h1> MODIFICAR ACTIVOS</h1></div>

                    <div class="row">
                        <div class="col-sm-5 col-sm-offset-3 form-box">

                            <div class="form-top">
                                <div class="form-top-left">
                                    <p>Modifica tus activos.</p>
                                </div>
                            </div>

                            <div class="form-bottom">
                                <form role="form" action="ModificarActivo.jsp" method="post" class="login-form">
                                    <h4>Codigo Producto: </h4>
                                    <div class="form-group">
                                        <table>
                                            <tr>
                                                <td>
                                                    <select name="Opciones" onchange="mostrarValor(this.options[this.selectedIndex].innerHTML, this.value)">
                                                        <%for (int i = 0; i < separada.length; i++) { %>
                                                        <option value="<%out.println(separada[i]); %>"><%out.println(separada[i]); %></option>
                                                        <% }%>
                                                    </select>
                                                </td>

                                                <td>
                                                    <input type="submit" value="Visualizar" />
                                                </td>

                                            </tr>
                                        </table>


                                    </div>
                                    <%
                                        //String op ="I47D83A17J22T27"; 
                                        String op = request.getParameter("Opciones");

                                        if (op == null) {
                                            op = separada[0];
                                        }
                                        op = op.substring(0, 15);
                                        System.out.println("-----------------------------------");
                                        System.out.println("Usuario: " + Usuario);
                                        System.out.println("Empresa: " + Empresa);
                                        System.out.println("Departamento: " + Departamento);
                                        System.out.println("Codigo:" + op);
                                        System.out.println("-----------------------------------");

                                        RequestBody formBody1 = new FormEncodingBuilder()
                                                .add("txtUsuario", Usuario)
                                                .add("txtEmpresa", Empresa)
                                                .add("txtDeartamento", Departamento)
                                                .add("txtCodigo", op)
                                                .build();

                                        String r1 = solicitud.Activ(formBody1);
                                        System.out.println(r1 + "---");
                                        String[] separada1 = r1.split(",");
                                        System.out.println("-------------Resultados------------");
                                        System.out.println(separada1[0]);
                                        System.out.println(separada1[1]);

                                    %>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtNombre" value="<%out.println(separada1[0]);%>" class="form-username form-control" id="form-username">
                                    </div>
                                    <div class="form-group">
                                        <label class="sr-only" for="form-username">Username</label>
                                        <input type="text" name="txtDescripcion" value="<%out.println(separada1[1]);%>" class="form-username form-control" id="form-username">
                                    </div>

                                    <%

                                        String des = (String) request.getParameter("txtDescripcion");
                                        System.out.println("descraaaaaaaaaaaaaaaaaaaaaaaaaaa:" + des);
                                        if (des != null) {
                                            RequestBody formBody3 = new FormEncodingBuilder()
                                                    .add("txtUsuario", Usuario)
                                                    .add("txtEmpresa", Empresa)
                                                    .add("txtDeartamento", Departamento)
                                                    .add("txtCodigo", op)
                                                    .add("txtDescripcion", des)
                                                    .build();
                                            String r2 = solicitud.Modificar(formBody3);
                                            System.out.println(r2 + "---");
                                        }
                                    %>
                                    <button type="submit" class="btn">Modificar Activo</button>
                                </form>




                            </div>

                        </div>
                    </div>
                    <div class="row">


                        <div class="col-sm-6 col-sm-offset-3 social-login">
                            <h3>    Iniciado como: <%out.println(Usuario);%></h3>
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
        <script src="Estilos/Login2/js/jquery-1.11.1.min.js"></script>
        <script src="Estilos/Login2/bootstrap/js/bootstrap.min.js"></script>
        <script src="Estilos/Login2/js/jquery.backstretch.min.js"></script>
        <script src="Estilos/Login2/js/scripts.js"></script>
    </body>

</html>