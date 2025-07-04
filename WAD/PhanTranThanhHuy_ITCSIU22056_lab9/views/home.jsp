<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 <!DOCTYPE html>
 <html>
 <head>
    <meta charset="UTF-8">
    <title>Online Store</title>
    <link rel="stylesheet"
 href="${pageContext.request.contextPath}/css/styles.css">
 </head>
 <body class="${theme}">
    <div class="container">
        <h1>${welcomeMessage}</h1>
        
        <div class="product-grid">
            <div class="product">
                <img
 src="${pageContext.request.contextPath}/images/product1.jpg" alt="Product 1">
                <h3>Laptop</h3>
                <p>$999.99</p>
                <form action="${pageContext.request.contextPath}/cart"
 method="post">
                    <input type="hidden" name="action" value="add">
                    <input type="hidden" name="productId" value="1">
                    <input type="hidden" name="productName" value="Laptop">
                    <input type="hidden" name="productPrice" value="999.99">
                    <button type="submit" class="btn btn-primary">Add to 
Cart</button>
                </form>
            </div>
            
            <div class="product">
                <img
 src="${pageContext.request.contextPath}/images/product2.jpg" alt="Product 2">
                <h3>Smartphone</h3>
                <p>$699.99</p>
                <form action="${pageContext.request.contextPath}/cart"
 method="post">
                    <input type="hidden" name="action" value="add">
                    <input type="hidden" name="productId" value="2">
                    <input type="hidden" name="productName"
 value="Smartphone">
                    <input type="hidden" name="productPrice" value="699.99">
                    <button type="submit" class="btn btn-primary">Add to 
Cart</button>
                </form>
            </div>
            
            <div class="product">
                <img
 src="${pageContext.request.contextPath}/images/product3.jpg" alt="Product 3">
                <h3>Headphones</h3>
                <p>$149.99</p>
                <form action="${pageContext.request.contextPath}/cart"
 method="post">
                    <input type="hidden" name="action" value="add">
                    <input type="hidden" name="productId" value="3">
                    <input type="hidden" name="productName"
 value="Headphones">
                    <input type="hidden" name="productPrice" value="149.99">
                    <button type="submit" class="btn btn-primary">Add to 
Cart</button>
                </form>
            </div>
        </div>
        
        <div class="navigation">
            <a href="${pageContext.request.contextPath}/preferences">User
Preferences</a> | 
            <a href="${pageContext.request.contextPath}/cart">Shopping 
Cart</a>
        </div>
    </div>
</body>
 </html>