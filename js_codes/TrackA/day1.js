// Node.js + Express: Hello Backend
// npm i express
import express from 'express';

const app = express();
const PORT = 3000;

// First route - this IS the backend
app.get('/', (req, res) => {
  // req = what user asked for
  // res = what we send back
  res.send('Hello from Node.js Backend! 👋');
});

app.get('/api/user', (req, res) => {
  // Real backend returns structured data
  res.json({ 
    id: 1, 
    name: 'Ishmail',
    role: 'backend dev' 
  });
});

app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});