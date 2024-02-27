// app.js
const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const port = process.env.PORT || 8080;

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/submit_js_code', (req, res) => {
    try {
        const jsCode = req.body.js_code;
        console.log(jsCode)
        const result = runJavaScript(jsCode); // Implement the logic to run JS code
        res.json({ result });
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});

app.get('/', (req, res) => {
    try {
        res.json("result");
    } catch (error) {
        res.status(500).json({ error: error.message });
    }
});


function runJavaScript(jsCode) {
    // Implement the logic to run JS code
    return eval(jsCode); // Example: Using eval for simplicity (Note: Be cautious about using eval in production)
}

app.listen(port, () => {
    console.log(`Node.js server running on port ${port}`);
});
