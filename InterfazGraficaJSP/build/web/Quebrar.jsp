<%-- 
    Document   : Modificado
    Created on : 28/03/2017, 06:51:58 PM
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
        <title>JSP Page</title>
    </head>
    <body>




        <form action="Login.jsp" method="POST">

            <%          
               session.removeAttribute( "NomUs");
               session.removeAttribute( "NomEmp");
               session.removeAttribute( "NomDept");
               session.removeAttribute( "Codi");
               response.sendRedirect("IniciarSesion.jsp");
            %>
        </form>


    </body>
</html>
