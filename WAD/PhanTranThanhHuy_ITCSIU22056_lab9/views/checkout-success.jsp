 <%@ page language="java"contentType="text/html; charset=UTF-8"
 pageEncoding="UTF-8"%>
 <!DOCTYPE html>
 <html>
 <head>
    <meta charset="UTF-8">
    <title>Checkout Success</title>
    <link rel="stylesheet"
 href="${pageContext.request.contextPath}/css/styles.css">
 </head>
 <body class="${theme}">
    <div class="container">
        <h1>${thankYouMessage}</h1>
        
        <div class="checkout-success">
            <p>Your order has been successfully processed.</p>
            <p>Order number: ORD-<%=System.currentTimeMillis() %></p>
            <p>A confirmation email has been sent to your email address.</p>
        </div>
        
        <div class="navigation">
            <a href="${pageContext.request.contextPath}/">Continue 
Shopping</a> | 
            <a href="${pageContext.request.contextPath}/preferences">User 
Preferences</a>
        </div>
    </div>
 </body>
 </html>