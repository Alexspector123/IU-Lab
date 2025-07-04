<%@ page contentType="text/html" pageEncoding="UTF-8"%>
<%@ include file="/WEB-INF/jsp/header.jsp" %>
<%@ include file="/WEB-INF/jsp/db-connection.jsp" %>

<%
String categoryId = request.getParameter("id");
boolean isEdit = (categoryId != null && !categoryId.isEmpty());
String name = "";
String successMessage = "";
String errorMessage = "";

if (isEdit) {
    Connection conn = null;
    PreparedStatement pstmt = null;
    ResultSet rs = null;
    try {
        conn = getConnection();
        String sql = "SELECT * FROM categories WHERE id = ?";
        pstmt = conn.prepareStatement(sql);
        pstmt.setInt(1, Integer.parseInt(categoryId));
        rs = pstmt.executeQuery();
        if (rs.next()) {
            name = rs.getString("name");
        } else {
            errorMessage = "Category not found!";
        }
    } catch (Exception e) {
        errorMessage = "Error retrieving category: " + e.getMessage();
        e.printStackTrace();
    } finally {
        closeResources(conn, pstmt, rs);
    }
}

if ("POST".equalsIgnoreCase(request.getMethod())) {
    name = request.getParameter("name");
    Connection conn = null;
    PreparedStatement pstmt = null;
    try {
        conn = getConnection();
        if (isEdit) {
            String sql = "UPDATE categories SET name = ? WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, name);
            pstmt.setInt(2, Integer.parseInt(categoryId));
        } else {
            String sql = "INSERT INTO categories (name) VALUES (?)";
            pstmt = conn.prepareStatement(sql);
            pstmt.setString(1, name);
        }
        int rowsAffected = pstmt.executeUpdate();
        if (rowsAffected > 0) {
            successMessage = isEdit ? "Category updated successfully!" : "Category added successfully!";
        } else {
            errorMessage = "Operation failed!";
        }
    } catch (Exception e) {
        errorMessage = "Error processing request: " + e.getMessage();
        e.printStackTrace();
    } finally {
        closeResources(conn, pstmt, null);
    }
}
%>

<h2><%= isEdit ? "Edit" : "Add New" %> Category</h2>
<% if (!errorMessage.isEmpty()) { %>
    <div class="error-message"><%= errorMessage %></div>
<% } %>
<% if (!successMessage.isEmpty()) { %>
    <div class="success-message"><%= successMessage %></div>
<% } %>

<form method="post">
    <div class="form-group">
        <label for="name">Category Name:</label>
        <input type="text" id="name" name="name" value="<%= name %>" required>
    </div>
    <button type="submit" class="btn btn-success"><%= isEdit ? "Update" : "Add" %> Category</button>
</form>

<%@ include file="/WEB-INF/jsp/footer.jsp" %>
