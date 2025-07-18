const mysql = require('mysql2');
require('dotenv').config();

// Create a connection pool
const pool = mysql.createPool({
   host: process.env.DB_HOST,
   user: process.env.DB_USER,
   password: process.env.DB_PASSWORD,
   database: process.env.DB_NAME,
   port: process.env.DB_PORT,
   waitForConnections: true,
   connectionLimit: 10,
   queueLimit: 0
});

// Convert to promise-based interface
const promisePool = pool.promise();

// Test the database connection
async function testConnection() {
   try {
      const [rows] = await promisePool.query('SELECT 1');
      console.log('Database connection successful');
   } catch (error) {
      console.error('Database connection failed:', error);
      process.exit(1);
   }
}

module.exports = {
   pool: promisePool,
   testConnection
};