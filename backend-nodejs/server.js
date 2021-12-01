const express = require('express');

const app = express();
const {PythonShell} = require('python-shell');

const PORT = 3000;
const IMAGES_PATH = "C:\\Users\\Huy\\Documents\\Code\\trash-ai\\backend-nodejs\\output\\out.jpg";

app.get("/", (req, res, next) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        pythonPath: 'D:/miniconda3/envs/imageai/python',
        args: []
    };

    PythonShell.run('model.py', options, function (err, result) {
        if (err) throw err;
        console.log(result.toString());
        res.sendFile(IMAGES_PATH);
        //res.send(result.toString());
    });
});

app.listen(PORT, () => {
    console.log('Running server on port %d...', PORT);
})