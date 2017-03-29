package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import Service.Alfanumerico;
import Service.WebService;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.FormEncodingBuilder;

public final class EliminarActivo_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List<String> _jspx_dependants;

  private org.glassfish.jsp.api.ResourceInjector _jspx_resourceInjector;

  public java.util.List<String> getDependants() {
    return _jspx_dependants;
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;

    try {
      response.setContentType("text/html;charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;
      _jspx_resourceInjector = (org.glassfish.jsp.api.ResourceInjector) application.getAttribute("com.sun.appserv.jsp.resource.injector");

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("\n");
      out.write("    <head>\n");
      out.write("\n");
      out.write("        <meta charset=\"utf-8\">\n");
      out.write("        <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n");
      out.write("        <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n");
      out.write("        <title>Eliminar Activos</title>\n");
      out.write("        <!-- CSS -->\n");
      out.write("        <link rel=\"stylesheet\" href=\"http://fonts.googleapis.com/css?family=Roboto:400,100,300,500\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/bootstrap/css/bootstrap.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/font-awesome/css/font-awesome.min.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/css/form-elements.css\">\n");
      out.write("        <link rel=\"stylesheet\" href=\"Estilos/Eliminar/css/style.css\">\n");
      out.write("\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"144x144\" href=\"Estilos/Eliminar/ico/apple-touch-icon-144-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"114x114\" href=\"Estilos/Eliminar/ico/apple-touch-icon-114-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" sizes=\"72x72\" href=\"Estilos/Eliminar/ico/apple-touch-icon-72-precomposed.png\">\n");
      out.write("        <link rel=\"apple-touch-icon-precomposed\" href=\"Estilos/Eliminar/ico/apple-touch-icon-57-precomposed.png\">\n");
      out.write("           <script type=\"text/javascript\">\n");
      out.write("        var mostrarValor = function(foo, bar){\n");
      out.write("        document.getElementById('txtcod').value = foo; \n");
      out.write("        };\n");
      out.write("    </script>\n");
      out.write("    </head>\n");
      out.write("\n");
      out.write("    <body>\n");
      out.write("\n");
      out.write("        ");

            //CONSULTA PARA TODOS LOS ACTIVOS DEL USUARIO

            String Usuario = "admin";//(String) session.getAttribute("NomUs");
            String Empresa = "admin";//(String) session.getAttribute("NomEmp");
            String Departamento = "guatemala";//(String) session.getAttribute("NomDept");
            WebService solicitud = new WebService();

            RequestBody formBody = new FormEncodingBuilder()
                    .add("txtUsuario", Usuario)
                    .add("txtEmpresa", Empresa)
                    .add("txtDeartamento", Departamento)
                    .build();
            String r = solicitud.Activos(formBody);
            //System.out.println(r + "---");
            String[] separada = r.split(",");
        
      out.write("\n");
      out.write("\n");
      out.write("<input type=\"text\" name=\"Prueba\" id=\"Prueba\" value=\"\" size=\"12\" readonly=\"readonly\" />\n");
      out.write("\n");
      out.write("\n");
      out.write("        <!-- Top content -->\n");
      out.write("        <div class=\"top-content\" align=\"left\">\n");
      out.write("\n");
      out.write("            <div class=\"inner-bg\">\n");
      out.write("                <div class=\"container\">\n");
      out.write("                    <div class=\"row\"><h1> ELIMINAR ACTIVOS</h1></div>\n");
      out.write("\n");
      out.write("                    <div class=\"row\">\n");
      out.write("                        <div class=\"col-sm-5 col-sm-offset-3 form-box\">\n");
      out.write("\n");
      out.write("                            <div class=\"form-top\">\n");
      out.write("                                <div class=\"form-top-left\">\n");
      out.write("                                    <p>Elimina activos no disponibles.</p>\n");
      out.write("                                </div>\n");
      out.write("                            </div>\n");
      out.write("\n");
      out.write("                            <div class=\"form-bottom\">\n");
      out.write("                                <form role=\"form\" action=\"EliminarActivo.jsp\" method=\"post\" class=\"login-form\">\n");
      out.write("                                    <h4>Codigo Producto: </h4>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <table>\n");
      out.write("                                            <tr>\n");
      out.write("                                                <td>\n");
      out.write("                                                    <select name=\"Opciones\" onchange=\"mostrarValor(this.options[this.selectedIndex].innerHTML, this.value)\">\n");
      out.write("                                                        ");
for (int i = 0; i < separada.length; i++) { 
      out.write("\n");
      out.write("                                                        <option value=\"");
out.println(separada[i]); 
      out.write('"');
      out.write('>');
out.println(separada[i]); 
      out.write("</option>\n");
      out.write("                                                        ");
 }
      out.write("\n");
      out.write("                                                    </select>\n");
      out.write("                                                </td>\n");
      out.write("                                                \n");
      out.write("                                                <td>\n");
      out.write("                                                    <input type=\"submit\" value=\"Visualizar\" />\n");
      out.write("                                                </td>\n");
      out.write("                                                \n");
      out.write("                                            </tr>\n");
      out.write("                                        </table>\n");
      out.write("\n");
      out.write("\n");
      out.write("                                    </div>\n");
      out.write("                                                       ");

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

                                                        
      out.write("\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtNombre\" value=\"");
out.println(separada1[0]);
      out.write("\" class=\"form-username form-control\" id=\"form-username\">\n");
      out.write("                                    </div>\n");
      out.write("                                    <div class=\"form-group\">\n");
      out.write("                                        <label class=\"sr-only\" for=\"form-username\">Username</label>\n");
      out.write("                                        <input type=\"text\" name=\"txtDescripcion\" value=\"");
out.println(separada1[1]);
      out.write("\" class=\"form-username form-control\" id=\"form-username\">\n");
      out.write("                                    </div>\n");
      out.write("            \n");
      out.write("                                    \n");
      out.write("                                </form>\n");
      out.write("                                    \n");
      out.write("                                  <form role=\"form\" action=\"Eliminado.jsp\" method=\"get\" class=\"login-form\">\n");
      out.write("                                   ");

                                     session.setAttribute("Codi",op);
                                   
      out.write("\n");
      out.write("                                    <button type=\"submit\" class=\"btn\">Eliminar Activo</button>\n");
      out.write("                                </form>\n");
      out.write("                            </div>\n");
      out.write("\n");
      out.write("                        </div>\n");
      out.write("                    </div>\n");
      out.write("                    <div class=\"row\">\n");
      out.write("\n");
      out.write("\n");
      out.write("                        <div class=\"col-sm-6 col-sm-offset-3 social-login\">\n");
      out.write("                            <h3>    Iniciado como: ");
out.println(Usuario);
      out.write("</h3>\n");
      out.write("                            <div class=\"social-login-buttons\">\n");
      out.write("\n");
      out.write("                                <a class=\"btn btn-link-2\" href=\"MenuPrincipal.jsp\">\n");
      out.write("                                    Regresar al Menu Principal\n");
      out.write("                                </a>\n");
      out.write("\n");
      out.write("                            </div>\n");
      out.write("\n");
      out.write("                        </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("                    </div>\n");
      out.write("                </div>\n");
      out.write("            </div>\n");
      out.write("\n");
      out.write("        </div>\n");
      out.write("\n");
      out.write("\n");
      out.write("        <!-- Javascript -->\n");
      out.write("        <script src=\"Estilos/Eliminar/js/jquery-1.11.1.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/bootstrap/js/bootstrap.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/js/jquery.backstretch.min.js\"></script>\n");
      out.write("        <script src=\"Estilos/Eliminar/js/scripts.js\"></script>\n");
      out.write("    </body>\n");
      out.write("\n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          out.clearBuffer();
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
        else throw new ServletException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
