 <%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
 <!DOCTYPE html>
 <html>
 <head>
    <meta charset="UTF-8">
    <title>User Preferences</title>
    <link rel="stylesheet"
href="${pageContext.request.contextPath}/css/styles.css">
 </head>
 <body class="${currentTheme}">
    <div class="container">
        <h1>User Preferences</h1>
        
        <%if(request.getParameter("updated")!=null){%>
            <div class="alert alert-success">
                Your preferences have been updated successfully!
            </div>
        <%}%>
        
        <form action="${pageContext.request.contextPath}/preferences"
 method="post">
            <div class="form-group">
                <label for="theme">Theme:</label>
                <select name="theme" id="theme" class="form-control">
                    <option value="light" ${currentTheme =='light'?
 'selected':''}>Light</option>
                    <option value="dark" ${currentTheme =='dark'?
 'selected':''}>Dark</option>
                    <option value="blue" ${currentTheme =='blue'?
 'selected':''}>Blue</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="language">Language:</label>
                <select name="language" id="language" class="form-control">
                    <option value="en" ${currentLanguage =='en'?'selected'
 :''}>English</option>
                    <option value="fr" ${currentLanguage =='fr'?'selected'
 :''}>French</option>
                    <option value="es" ${currentLanguage =='es'?'selected'
 :''}>Spanish</option>
                    <option value="vi" ${currentLanguage =='vi'?'selected'
 :''}>Vietnamese</option>
                </select>
            </div>
            
            <button type="submit" class="btn btn-primary">Save Preferences</button>
        </form>
        
        <div class="navigation">
            <a href="${pageContext.request.contextPath}/">Home</a> | 
            <a href="${pageContext.request.contextPath}/cart">Shopping Cart</a>
        </div>
    </div>
 </body>
 </html>