<%@ include file="header.jsp" %>

<c:if test="${course != null}">
    <h2>Edit Student</h2>
    <form action="${pageContext.request.contextPath}/course/update" method="post">
        <input type="hidden" name="id" value="${course.id}" />
</c:if>

<c:if test="${course == null}">
    <h2>Add New Course</h2>
    <form action="${pageContext.request.contextPath}/course/add" method="POST">
</c:if>
    <div class="form-group">
        <label for="code">Code:</label>
        <input type="text" id="code" name="code" value="${course.code}" required />
    </div>
    <div class="form-group">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" value="${course.name}" required />
    </div>
    <div class="form-group">
        <label for="description">Description:</label>
        <textarea id="description" name="description">${course.description}</textarea>
    </div>
    <div class="form-group">
        <label for="credits">Credits:</label>
        <input type="number" id="credits" name="credits" value="${course.credits}" required />
    </div>

    <button type="submit" class="btn">Save</button>
    <a href="${pageContext.request.contextPath}/courses" class="btn">Cancel</a>
    </form>
</form>

<%@ include file="footer.jsp" %>
