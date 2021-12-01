const express = require('express');

const app = express();
const {PythonShell} = require('python-shell');

const PORT = 3000;
const IMAGES_PATH = "C:\\Users\\Rasean\\Documents\\Code\\trash-ai\\backend-nodejs\\output\\out.jpg";
//the pathing above might need to be changed in order to run on your end

app.get("/", (req, res, next) => {
    let options = {
        mode: 'text',
        pythonOptions: ['-u'],
        pythonPath: 'C:\Users\Rasean\miniconda3\envs\imageai',
        //the pathing above will need to be changed to run on your end
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
