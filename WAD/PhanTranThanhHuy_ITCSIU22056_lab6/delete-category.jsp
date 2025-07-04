<%@ page contentType="text/html" pageEncoding="UTF-8"%>
<%@ include file="/WEB-INF/jsp/db-connection.jsp" %>

<%
String categoryId = request.getParameter("id");
if (categoryId != null && !categoryId.isEmpty()) {
    Connection conn = null;
    PreparedStatement pstmt = null;
    try {
        conn = getConnection();
        String sql = "DELETE FROM categories WHERE id = ?";
        pstmt = conn.prepareStatement(sql);
        pstmt.setInt(1, Integer.parseInt(categoryId));
        pstmt.executeUpdate();
    } catch (Exception e) {
        e.printStackTrace();
    } finally {
        closeResources(conn, pstmt, null);
    }
}
response.sendRedirect("category-list.jsp");
%>
