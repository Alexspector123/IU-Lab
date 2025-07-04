<%-- Database connection settings --%>
<%@ page import="java.sql.*" %>
<%!
// Database connection variables
private static final String JDBC_URL = "jdbc:mysql://localhost:3306/productdb";
private static final String JDBC_USER = "root"; // Change to your MySQL username
private static final String JDBC_PASSWORD = "Snowace2911"; // Change to your MySQL password
// Method to get database connection
public static Connection getConnection() throws SQLException, ClassNotFoundException {
Class.forName("com.mysql.cj.jdbc.Driver");
return DriverManager.getConnection(JDBC_URL, JDBC_USER, JDBC_PASSWORD);
}
// Method to close database resources
public static void closeResources(Connection conn, Statement stmt, ResultSet rs) {
try {
if (rs != null) rs.close();
} catch (SQLException e) {
e.printStackTrace();
}
try {
if (stmt != null) stmt.close();
} catch (SQLException e) {
e.printStackTrace();
}
try {
if (conn != null) conn.close();
} catch (SQLException e) {
e.printStackTrace();
}
}
%>