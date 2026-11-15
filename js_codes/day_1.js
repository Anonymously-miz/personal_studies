// // node.js - Javascript on the server. Node.js uses chrome's built in v8 engine and Libuv to perform backend operations on the server. while v8 engine handles the main thread, code execution and data types, Libuv handles the event loop, thread pool, file operations etc. because node.js is a single threaded but concurrent runtime.

// // the main thread handles cpu operations. so if a big math operation is put in the main thread it blocks all other operations until it is completed and finishes the operation which might break the server.

// // file and network operations are sent the to worker thread pool where they enter an event loop and are id with a callback function

// // therefore node.js is not entirely non-blocking.

// // Day 1: Your first Node process - no Express yet
// // server.js
// const http = require('http');
// const port = 3000;

// const server = http.createServer((req, res) => {
//   // req = incoming, res = outgoing
//   res.writeHead(200, { 'Content-Type': 'text/plain' });
//   res.end('Node is just JS on the server\n');
// });

// server.listen(port, () => {
//   console.log('V8 + libuv listening on 3000');
//   console.log('Process ID:', process.pid);
//   console.log(process.versions.v8);
//   console.log(`your site is running at http://localhost:${port}`);
// });

// Open DevTools with F12 / Cmd + Option + J
console.log("Hello, JavaScript!");
console.log("2 + 3 =", 2 + 3);

// JavaScript talks back in the console.
// That is your laboratory for the next 30 days.

// Three websites i use daily
// portal.techcrush.pro, instagram.com, udemy.com
// portal.techcrush.pro: javascript renders the page, keep records of attendance, quizzes and scores, update the screen based on new information receives.
// instagram.com: when a user clicks instagram.com javascript displays instagram.com, js stores information, js renders the page.
// udemy.com: js saves class progress, stores information, responsible for playback functions

// browser js is what brings life into a webpage and server js is what stores information, talk to other applications, aunthenticate and authorize.

// browser js is like a the outer layer/outer design of a jet and server js is the engine that makes it move.