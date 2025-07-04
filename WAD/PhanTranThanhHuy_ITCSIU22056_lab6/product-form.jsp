<%@ page contentType="text/html" pageEncoding="UTF-8" %>
<%@ include file="/WEB-INF/jsp/header.jsp" %>
<%@ include file="/WEB-INF/jsp/db-connection.jsp" %>

<%
    // Check if editing an existing product
    String productId = request.getParameter("id");
    boolean isEdit = (productId != null && !productId.isEmpty());

    // Variables to store product data
    String name = "";
    String description = "";
    double price = 0.0;
    int stock = 0;
    int category_id = 0;
    
    // Variables for messages
    String errorMessage = "";
    String successMessage = "";

    // If editing, load the product data
    if (isEdit) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        ResultSet rs = null;
        try {
            conn = getConnection();
            String sql = "SELECT * FROM products WHERE id = ?";
            pstmt = conn.prepareStatement(sql);
            pstmt.setInt(1, Integer.parseInt(productId));
            rs = pstmt.executeQuery();
            if (rs.next()) {
                name = rs.getString("name");
                description = rs.getString("description") != null ? rs.getString("description") : "";
                price = rs.getDouble("price");
                stock = rs.getInt("stock");
                category_id = rs.getInt("category_id");
            } else {
                errorMessage = "Product not found!";
            }
        } catch (Exception e) {
            errorMessage = "Error retrieving product: " + e.getMessage();
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, rs);
        }
    }

    // Process form submission
    if ("POST".equalsIgnoreCase(request.getMethod())) {
        Connection conn = null;
        PreparedStatement pstmt = null;
        try {
            // Get form data
            name = request.getParameter("name");
            description = request.getParameter("description");
            price = Double.parseDouble(request.getParameter("price"));
            stock = Integer.parseInt(request.getParameter("stock"));
            category_id = Integer.parseInt(request.getParameter("category_id"));
            conn = getConnection();

            if (isEdit) {
                // Update existing product
                String sql = "UPDATE products SET name = ?, description = ?, price = ?, stock = ?, category_id = ? WHERE id = ?";
                pstmt = conn.prepareStatement(sql);
                pstmt.setString(1, name);
                pstmt.setString(2, description);
                pstmt.setDouble(3, price);
                pstmt.setInt(4, stock);
                pstmt.setInt(5, category_id);
                pstmt.setInt(6, Integer.parseInt(productId));
            } else {
                // Insert new product
                String sql = "INSERT INTO products (name, description, price, stock, category_id) VALUES (?, ?, ?, ?, ?)";
                pstmt = conn.prepareStatement(sql);
                pstmt.setString(1, name);
                pstmt.setString(2, description);
                pstmt.setDouble(3, price);
                pstmt.setInt(4, stock);
                pstmt.setInt(5, category_id);
            }

            int rowsAffected = pstmt.executeUpdate();
            if (rowsAffected > 0) {
                successMessage = isEdit ? "Product updated successfully!" : "Product added successfully!";
                
                // Clear form after successful addition
                if (!isEdit) {
                    name = "";
                    description = "";
                    price = 0.0;
                    stock = 0;
                    category_id = 0;
                }
            } else {
                errorMessage = isEdit ? "Product could not be updated." : "Product could not be added.";
            }
        } catch (Exception e) {
            errorMessage = "Error processing form: " + e.getMessage();
            e.printStackTrace();
        } finally {
            closeResources(conn, pstmt, null);
        }
    }
%>

<h2><%= isEdit ? "Edit" : "Add New" %> Product</h2>

<% if (!errorMessage.isEmpty()) { %>
    <div class="error-message">
        <%= errorMessage %>
    </div>
<% } %>

<% if (!successMessage.isEmpty()) { %>
    <div class="success-message">
        <%= successMessage %>
    </div>
<% } %>

<form method="post" action="${pageContext.request.contextPath}/product-form.jsp<%= isEdit ? "?id=" + productId : "" %>">
    <div class="form-group">
        <label for="name">Product Name:</label>
        <input type="text" id="name" name="name" value="<%= name %>" required>
    </div>

    <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" name="description"><%= description %></textarea>
    </div>

    <div class="form-group">
        <label for="price">Price:</label>
        <input type="number" id="price" name="price" step="0.01" min="0" value="<%= price %>" required>
    </div>

    <div class="form-group">
        <label for="stock">Stock:</label>
        <input type="number" id="stock" name="stock" min="0" value="<%= stock %>" required>
    </div>

    <div class="form-group">
        <label for="category">Category:</label>
        <select id="category" name="category_id" required>
            <option value="">Select Category</option>
            <%
                Connection conn = null;
                Statement stmt = null;
                ResultSet rs = null;
                try {
                    conn = getConnection();
                    stmt = conn.createStatement();
                    rs = stmt.executeQuery("SELECT * FROM categories ORDER BY name");
                    while (rs.next()) {
                        int catId = rs.getInt("id");
                        String catName = rs.getString("name");
                        boolean selected = (catId == category_id);
            %>
                        <option value="<%= catId %>" <%= selected ? "selected" : "" %>><%= catName %></option>
            <%
                    }
                } catch (Exception e) {
                    e.printStackTrace();
                } finally {
                    closeResources(conn, stmt, rs);
                }
            %>
        </select>
    </div>

    <button type="submit" class="btn btn-success"><%= isEdit ? "Update" : "Add" %> Product</button>
    <a href="${pageContext.request.contextPath}/product-list.jsp" class="btn btn-danger">Cancel</a>
</form>

<%@ include file="/WEB-INF/jsp/footer.jsp" %>