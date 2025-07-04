const express = require('express');
const Task = require('../models/Task');

const router = express.Router();

// Get all tasks
router.get('/', async (req, res) => {
    try {
        const { status, q, sortBy, order } = req.query;
        const tasks = await Task.findAll({ status, q, sortBy, order });
        res.render('index', {
            title: 'Task Manager',
            tasks,
            status: status || 'all',
            q: q || '',
            sortBy: sortBy || 'created_at',
            order: order || 'desc'
        });
    } catch (error) {
        console.error('Error fetching tasks:', error);
        res.status(500).render('index', {
            title: 'Task Manager',
            error: 'Error fetching tasks',
            tasks: [],
            status: 'all',
            q: '',
            sortBy: 'created_at',
            order: 'desc'
        });
    }
});

// Get task creation form
router.get('/tasks/create', (req, res) => {
    res.render('create', {
        title: 'Create Task'
    });
});

// Create new task
router.post('/tasks', async (req, res) => {
    try {
        const { title, description, status } = req.body;
        // Validate input
        if (!title) {
            return res.status(400).render('create', {
                title: 'Create Task',
                error: 'Title is required',
                task: req.body
            });
        }
        // Create task
        await Task.create({
            title,
            description,
            status: status || 'pending'
        });
        res.redirect('/');
    } catch (error) {
        console.error('Error creating task:', error);
        res.status(500).render('create', {
            title: 'Create Task',
            error: 'Error creating task',
            task: req.body
        });
    }
});

// Get task edit form
router.get('/tasks/edit/:id', async (req, res) => {
    try {
        const task = await Task.findById(req.params.id);
        if (!task) {
            return res.status(404).render('error', {
                title: 'Error',
                message: 'Task not found',
                error: { status: 404 }
            });
        }
        res.render('edit', {
            title: 'Edit Task',
            task
        });
    } catch (error) {
        console.error('Error fetching task:', error);
        res.status(500).render('error', {
            title: 'Error',
            message: 'Error fetching task',
            error
        });
    }
});

// Update task
router.post('/tasks/update/:id', async (req, res) => {
    try {
        const { title, description, status } = req.body;
        // Validate input
        if (!title) {
            const task = await Task.findById(req.params.id);
            return res.status(400).render('edit', {
                title: 'Edit Task',
                error: 'Title is required',
                task: { ...task, ...req.body }
            });
        }
        // Update task
        constupdated = await Task.update(req.params.id, {
            title,
            description,
            status: status || 'pending'
        });
        if (!updated) {
            return res.status(404).render('error', {
                title: 'Error',
                message: 'Task not found',
                error: { status: 404 }
            });
        }
        res.redirect('/');
    } catch (error) {
        console.error('Error updating task:', error);
        res.status(500).render('error', {
            title: 'Error',
            message: 'Error updating task',
            error
        });
    }
});

// Delete task
router.get('/tasks/delete/:id', async (req, res) => {
    try {
        constdeleted = await Task.delete(req.params.id);
        if (!deleted) {
            return res.status(404).render('error', {
                title: 'Error',
                message: 'Task not found',
                error: { status: 404 }
            });
        }
        res.redirect('/');
    } catch (error) {
        console.error('Error deleting task:', error);
        res.status(500).render('error', {
            title: 'Error',
            message: 'Error deleting task',
            error
        });
    }
});
module.exports = router