// Load environment variables
require('dotenv').config();
// Import required modules
const express = require('express');
const bodyParser = require('body-parser');
const path = require('path');
const db = require('./config/database');
// Import routes
const taskRoutes = require('./routes/tasks');
// Initialize Express app
const app = express();
const PORT = process.env.PORT || 3000;
// Connect to database
db.testConnection();
// Set up middleware
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static(path.join(__dirname, 'public')));
// Set up view engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

const expressLayouts = require('express-ejs-layouts');
app.use(expressLayouts);
app.set('layout', 'layout');

// Enable view rendering without layout parameter
app.use((req, res, next) => {
    const originalRender = res.render;
    res.render = function (view, options, callback) {
        if (typeof options === 'function') {
            callback = options;
            options = {};
        }
        if (!options) {
            options = {};
        }
        originalRender.call(this, view, options, callback);
    };
    next();
});
// Routes
app.use('/', taskRoutes);
// Start the server
app.listen(PORT, () => {
    console.log(`Server running on http://localhost:${PORT}`);
})