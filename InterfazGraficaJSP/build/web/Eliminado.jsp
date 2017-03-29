<%-- 
    Document   : Eliminado
    Created on : 28/03/2017, 05:51:48 PM
    Author     : Flinttloco
--%>
<%@page  import ="com.squareup.okhttp.RequestBody" %>
<%@page import="com.squareup.okhttp.FormEncodingBuilder"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
<%@page import="Service.WebService"%>
<!DOCTYPE html>
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <title>Eliminando</title>
    </head>
    <body>




        <form action="EliminarActivo.jsp" method="POST">

            <%
                String Usuario = (String) session.getAttribute("NomUs");
                String Empresa = (String) session.getAttribute("NomEmp");
                String Departamento = (String) session.getAttribute("NomDept");
                String Codigo = (String) session.getAttribute("Codi");
                WebService solicitud = new WebService();

          

                    RequestBody formBody = new FormEncodingBuilder()
                            .add("txtUsuario", Usuario)
                            .add("txtEmpresa", Empresa)
                            .add("txtDeartamento", Departamento)
                            .add("txtCodigo", Codigo)
                            .build();
                    String r = solicitud.Eliminar(formBody);
                    System.out.println(r + "---");
                    if (r.equalsIgnoreCase("True")) {
                        String a = "Activo Eliminado";
                        out.println("<script>");
                        out.println("alert('" + a + "');");
                        out.println("</script>");
                        response.sendRedirect("EliminarActivo.jsp");

                    } else {
                        String a = "No se puedo Eliminar el Activo";
                        out.println("<script>");
                        out.println("alert('" + a + "');");
                        out.println("</script>");
                        response.sendRedirect("EliminarActivo.jsp");
                    }
                


            %>
        </form>


    </body>
</html>
