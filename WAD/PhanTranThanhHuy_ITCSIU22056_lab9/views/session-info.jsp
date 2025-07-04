 <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 <%@ page import="java.util.Map" %>
 <!DOCTYPE html>
 <html>
 <head>
    <meta charset="UTF-8">
    <title>Session Information</title>
    <link rel="stylesheet"
 href="${pageContext.request.contextPath}/css/styles.css">
 </head>
 <body class="${theme}">
    <div class="container">
        <h1>Session Information</h1>
        
        <h2>Basic Session Info</h2>
        <table class="cart-table">
            <thead>
                <tr>
                    <th>Property</th>
                    <th>Value</th>
                </tr>
            </thead>
            <tbody>
                <%
                Map<String,Object>sessionInfo =(Map<String, Object>)
 request.getAttribute("sessionInfo");
                for(Map.Entry<String,Object>entry :
 sessionInfo.entrySet()){
                %>
                    <tr>
                        <td><strong><%=entry.getKey()%></strong></td>
                        <td><%=entry.getValue()%></td>
                    </tr>
                <%
                }
                %>
            </tbody>
        </table>
        
        <h2>Session Attributes</h2>
        <%
        Map<String,Object>sessionAttributes =(Map<String,Object>)
 request.getAttribute("sessionAttributes");
        if(sessionAttributes.isEmpty()) {
        %>
            <p>No session attributes found.</p>
        <%
        }else{
        %>
            <table class="cart-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <%
                    for(Map.Entry<String,Object>entry :
 sessionAttributes.entrySet()){
                    %>
                        <tr>
                            <td><strong><%= entry.getKey()%></strong></td>
                            <td><%=entry.getValue()%></td>
                        </tr>
                    <%
                    }
                    %>
                </tbody>
            </table>
        <%
        }
        %>
        
        <h2>Cookies</h2>
        <%
        Map<String,String>cookies =(Map<String,String>)
 request.getAttribute("cookies");
        if(cookies.isEmpty()){
        %>
            <p>No cookies found.</p>
        <%
        }else{
        %>
            <table class="cart-table">
                <thead>
                    <tr>
                        <th>Name</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    <%
                    for(Map.Entry<String,String>entry :
 cookies.entrySet()){
                    %>
                        <tr>
                            <td><strong><%= entry.getKey()%></strong></td>
                            <td><%=entry.getValue()%></td>
                        </tr>
                    <%
                    }
                    %>
                </tbody>
            </table>
        <%
        }
        %>
        
        <div class="navigation">
            <a href="${pageContext.request.contextPath}/">Home</a> | 
            <a href="${pageContext.request.contextPath}/cart">Shopping 
Cart</a> | 
            <a href="${pageContext.request.contextPath}/preferences">User 
Preferences</a>
        </div>
    </div>
 </body>
 </html>