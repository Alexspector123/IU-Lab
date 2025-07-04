<%@ page contentType="text/html" pageEncoding="UTF-8"%>
<%@ include file="/WEB-INF/jsp/header.jsp" %>
<%@ include file="/WEB-INF/jsp/db-connection.jsp" %>

<%
    // Handle delete action if specified
    String deleteId = request.getParameter("deleteId");
    String successMessage = "";
    String errorMessage = "";

    if (deleteId != null && !deleteId.isEmpty()) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            conn = getConnection();
            String sql = "DELETE FROM products WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, Integer.parseInt(deleteId));
            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                successMessage = "Product deleted successfully!";
            } else {
                errorMessage = "Product not found or could not be deleted.";
            }
        } catch (Exception e) {
            errorMessage = "Error deleting product: " + e.getMessage();
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, null);
        }
    }
%>

<h2>Product List</h2>
<a href="${pageContext.request.contextPath}/product-form.jsp" class="btn btn-success">Add New Product</a>

<% if (!successMessage.isEmpty()) { %>
    <div class="success-message">
        <%= successMessage %>
    </div>
<% } %>

<% if (!errorMessage.isEmpty()) { %>
    <div class="error-message">
        <%= errorMessage %>
    </div>
<% } %>

<table>
    <thead>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Description</th>
            <th>Price</th>
            <th>Stock</th>
            <th>Category ID</th>
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
                rs = stmt.executeQuery("SELECT * FROM products ORDER BY id");
                boolean productsFound = false;

                while (rs.next()) {
                    productsFound = true;
                    int id = rs.getInt("id");
                    String name = rs.getString("name");
                    String description = rs.getString("description");
                    double price = rs.getDouble("price");
                    int stock = rs.getInt("stock");
                    int category_id = rs.getInt("category_id");
        %>
        <tr>
            <td><%= id %></td>
            <td><%= name %></td>
            <td><%= description != null ? description : "" %></td>
            <td>$<%= String.format("%.2f", price) %></td>
            <td><%= stock %></td>
            <td><%= category_id %></td>
            <td>
                <a href="${pageContext.request.contextPath}/product-form.jsp?id=<%= id %>" class="btn btn-primary">Edit</a>
                <a href="${pageContext.request.contextPath}/product-list.jsp?deleteId=<%= id %>"
                   class="btn btn-danger"
                   onclick="return confirm('Are you sure you want to delete this product?');">
                   Delete
                </a>
            </td>
        </tr>
        <%
                }
                if (!productsFound) {
        %>
        <tr>
            <td colspan="6" style="text-align: center;">No products found</td>
        </tr>
        <%
                }
            } catch (Exception e) {
                out.println("<tr><td colspan='6' class='error-message'>Error retrieving products: " + e.getMessage() + "</td></tr>");
                e.printStackTrace();
            } finally {
                closeResources(conn, stmt, rs);
            }
        %>
    </tbody>
</table>

<%@ include file="/WEB-INF/jsp/footer.jsp" %>
