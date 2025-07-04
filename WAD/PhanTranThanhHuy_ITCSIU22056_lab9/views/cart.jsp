<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 <%@ page import="java.util.List" %>
 <%@ page import="com.weblab.model.Product" %>
 <!DOCTYPE html>
 <html>
 <head>
    <meta charset="UTF-8">
    <title>Shopping Cart</title>
    <link rel="stylesheet"
 href="${pageContext.request.contextPath}/css/styles.css">
 </head>
 <body class="${theme}">
    <div class="container">
        <h1>Shopping Cart</h1>
        
        <%
        List<Product>cart =(List<Product>)session.getAttribute("cart");
        if(cart ==null||cart.isEmpty()) {
        %>
            <p>Your cart is empty.</p>
        <%
        }else{
        %>
            <form action="${pageContext.request.contextPath}/cart"
method="post">
                <input type="hidden" name="action" value="update">
                
                <table class="cart-table">
                    <thead>
                        <tr>
                            <th>Product</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Subtotal</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <%
                        for(Product product :cart){
                        %>
                            <tr>
                                <td><%=product.getName()%></td>
                                <td>$<%= String.format("%.2f",
 product.getPrice())%></td>
                                <td>
                                    <input type="hidden" name="productId"
 value="<%=product.getId()%>">
                                    <input type="number" name="quantity"
 value="<%=product.getQuantity()%>"min="0"class="form-control"
 style="width: 60px;">
                                </td>
                                <td>$<%= String.format("%.2f",
 product.getSubtotal()) %></td>
                                <td>
                                    <a
 href="${pageContext.request.contextPath}/cart?action=remove&productId=<%=
 product.getId()%>"
                                       
onclick="document.getElementById('removeForm<%=product.getId()
 %>').submit(); return false;">Remove</a>
                                    <form id="removeForm<%=product.getId()
 %>"action="${pageContext.request.contextPath}/cart" method="post"
 style="display:none;">
                                        <input type="hidden" name="action"
 value="remove">
                                        <input type="hidden" name="productId"
 value="<%=product.getId()%>">
                                    </form>
                                </td>
                            </tr>
                        <%
                        }
                        %>
                    </tbody>
                </table>
                
                <div class="cart-summary">
                    Total: $<%=String.format("%.2f",(Double)
 request.getAttribute("cartTotal"))%>
                </div>
                
                <div class="cart-actions">
                    <button type="submit" class="btn btn-primary">Update 
Cart</button>
                    
                    <div>
                        <a href="#"
 onclick="document.getElementById('clearForm').submit(); return false;"
 class="btn btn-secondary">Clear Cart</a>
                        <a href="#"
 onclick="document.getElementById('checkoutForm').submit(); return false;"
 class="btn btn-success">Checkout</a>
                    </div>
                </div>
            </form>
            
            <form id="clearForm"
 action="${pageContext.request.contextPath}/cart" method="post">
                <input type="hidden" name="action" value="clear">
            </form>
            
            <form id="checkoutForm"
 action="${pageContext.request.contextPath}/cart" method="post">
                <input type="hidden" name="action" value="checkout">
            </form>
        <%
        }
        %>
        
        <div class="navigation">
            <a href="${pageContext.request.contextPath}/">Continue 
Shopping</a> | 
            <a href="${pageContext.request.contextPath}/preferences">User 
Preferences</a>
        </div>
    </div>
 </body>
 </html>