const db = require('../config/database');
class Task {

  // Get all tasks
  static async findAll({ status, q, createdAt, sortBy, order } = {}) {
    try {
      let sql = 'SELECT * FROM tasks WHERE 1=1';
      const params = [];

      // Filter by status
      if (status && status !== 'all') {
        sql += ' AND status = ?';
        params.push(status);
      }

      // Search by title or description
      if (q) {
        sql += ' AND (LOWER(title) LIKE ? OR LOWER(description) LIKE ?)';
        params.push(`%${q.toLowerCase()}%`, `%${q.toLowerCase()}%`);
      }

      // Filter by creation date (YYYY-MM-DD)
      if (createdAt) {
        sql += ' AND DATE(created_at) = ?';
        params.push(createdAt);
      }

      // Sorting
      const allowedSort = ['title', 'status', 'created_at'];
      const sortField = allowedSort.includes(sortBy) ? sortBy : 'created_at';
      const sortOrder = order === 'asc' ? 'ASC' : 'DESC';
      sql += ` ORDER BY ${sortField} ${sortOrder}`;

      const [rows] = await db.pool.query(sql, params);
      return rows;
    } catch (error) {
      throw error;
    }
  }

  // Get task by ID
  static async findById(id) {
    try {
      const [rows] = await db.pool.query(
        'SELECT * FROM tasks WHERE id = ?',
        [id]
      );
      return rows[0];
    } catch (error) {
      throw error;
    }
  }

  // Create a new task
  static async create(taskData) {
    try {
      const { title, description, status } = taskData;
      const [result] = await db.pool.query(
        'INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)',
        [title, description, status || 'pending']
      );
      return this.findById(result.insertId);
    } catch (error) {
      throw error;
    }
  }

  // Update a task
  static async update(id, taskData) {
    try {
      const { title, description, status } = taskData;
      const [result] = await db.pool.query(
        'UPDATE tasks SET title = ?, description = ?, status = ? WHERE id = ?',
        [title, description, status, id]
      );
      return result.affectedRows > 0 ? this.findById(id) : null;
    } catch (error) {
      throw error;
    }
  }

  // Delete a task
  static async delete(id) {
    try {
      const [result] = await db.pool.query(
        'DELETE FROM tasks WHERE id = ?',
        [id]
      );
      return result.affectedRows > 0;
    } catch (error) {
      throw error;
    }
  }
}

module.exports = Task;