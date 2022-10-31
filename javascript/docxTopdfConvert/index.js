const express = require('express');
const port = 9000;

const app = express();

app.listen(port, () =>
  console.log(
    `nodejs-convert-file-server listening at http://localhost:${port}`,
  ),
);