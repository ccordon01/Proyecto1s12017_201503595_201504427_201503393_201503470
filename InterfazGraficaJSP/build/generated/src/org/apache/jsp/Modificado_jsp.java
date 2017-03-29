package org.apache.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;
import com.squareup.okhttp.RequestBody;
import com.squareup.okhttp.FormEncodingBuilder;
import Service.WebService;

public final class Modificado_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      out.write("<!DOCTYPE html>\n");
      out.write("<html>\n");
      out.write("    <head>\n");
      out.write("        <meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n");
      out.write("        <title>JSP Page</title>\n");
      out.write("    </head>\n");
      out.write("    <body>\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("        <form action=\"ModificarActivo.jsp\" method=\"POST\">\n");
      out.write("\n");
      out.write("            ");

                String Usuario = (String) session.getAttribute("NomUs");
                String Empresa = (String) session.getAttribute("NomEmp");
                String Departamento = (String) session.getAttribute("NomDept");
                String Codigo = (String) session.getAttribute("Codi");
                String Descripcion = (String) session.getAttribute("Des");
                WebService solicitud = new WebService();

                System.out.println(Usuario);
                System.out.println(Empresa);
                System.out.println(Departamento);
                System.out.println(Codigo);
                System.out.println(Descripcion);
                
                
                /*
                

                    RequestBody formBody = new FormEncodingBuilder()
                            .add("txtUsuario", Usuario)
                            .add("txtEmpresa", Empresa)
                            .add("txtDeartamento", Departamento)
                            .add("txtCodigo", Codigo)
                            .add("txtDescripcion", Descripcion)
                            .build();
                    String r = solicitud.Modificar(formBody);
                    System.out.println(r + "---");
                    
                    if (r.equalsIgnoreCase("True")) {
                        String a = "Activo Modificado";
                        out.println("<script>");
                        out.println("alert('" + a + "');");
                        out.println("</script>");
                        response.sendRedirect("ModificarActivo.jsp");

                    } 
                    else {
                        String a = "No se puedo Modificar el Activo";
                        out.println("<script>");
                        out.println("alert('" + a + "');");
                        out.println("</script>");
                        response.sendRedirect("ModificarActivo.jsp");
                    }
                
                    */

            
      out.write("\n");
      out.write("        </form>\n");
      out.write("\n");
      out.write("\n");
      out.write("    </body>\n");
      out.write("</html>\n");
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
