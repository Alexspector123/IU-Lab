<%@ include file="header.jsp" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/fmt" prefix="fmt" %>

<h2>Course Details</h2>

<c:if test="${course != null}">
    <div style="background: #fff; padding: 20px; border-radius: 5px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
        <div style="margin-bottom: 15px;">
            <strong>ID:</strong> ${course.id}
        </div>
        <div style="margin-bottom: 15px;">
            <strong>Name:</strong> ${course.name}
        </div>
        <div style="margin-bottom: 15px;">
            <strong>Code:</strong> ${course.code}
        </div>
        <div style="margin-bottom: 15px;">
            <strong>Credits:</strong> ${course.credits}
        </div>
    </div>

    <div style="margin-top: 20px;">
        <a href="${pageContext.request.contextPath}/course/edit?id=${course.id}" class="btn">Edit</a>
        <a href="${pageContext.request.contextPath}/courses" class="btn">Back to List</a>
    </div>
</c:if>

<c:if test="${course == null}">
    <div style="background: #ffe6e6; padding: 20px; border-radius: 5px;">
        <p>Course not found.</p>
    </div>
    <div style="margin-top: 20px;">
        <a href="${pageContext.request.contextPath}/courses" class="btn">Back to List</a>
    </div>
</c:if>

<%@ include file="footer.jsp" %>
