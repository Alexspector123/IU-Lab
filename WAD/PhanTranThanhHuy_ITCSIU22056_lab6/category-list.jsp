<%@ page contentType="text/html" pageEncoding="UTF-8"%>
<%@ include file="/WEB-INF/jsp/header.jsp" %>
<%@ include file="/WEB-INF/jsp/db-connection.jsp" %>

<h2>Category List</h2>
<a href="category-form.jsp" class="btn btn-success">Add Category</a>
<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        <%
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            conn = getConnection();
            stmt = conn.createStatement();
            rs = stmt.executeQuery("SELECT * FROM categories ORDER BY id");

            while (rs.next()) {
                int id = rs.getInt("id");
                String name = rs.getString("name");
        %>
        <tr>
            <td><%= id %></td>
            <td><%= name %></td>
            <td>
                <a href="category-form.jsp?id=<%= id %>" class="btn btn-primary">Edit</a>
                <a href="delete-category.jsp?id=<%= id %>" class="btn btn-danger" onclick="return confirm('Are you sure?')">Delete</a>
            </td>
        </tr>
        <%  
            }
        } catch (Exception e) {
            e.printStackTrace();
        } finally {
            closeResources(conn, stmt, rs);
        }
        %>
    </tbody>
</table>

<%@ include file="/WEB-INF/jsp/footer.jsp" %>
