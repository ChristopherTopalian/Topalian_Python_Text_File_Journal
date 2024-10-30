// Topalian_Combine_txt_Files.js

let fs = require('fs');
let path = require('path');

function combineTextFiles(directory, textFileName)
{
    let outputFilePath = path.join(directory, 'main.txt');

    let fileContents = [];

    function traverseFolder(folder)
    {
        let files = fs.readdirSync(folder);

        for (let i = 0; i < files.length; i++)
        {
            let file = files[i];

            let filePath = path.join(folder, file);

            let stats = fs.statSync(filePath);

            if (stats.isDirectory())
            {
                traverseFolder(filePath);
            }
            else if (path.extname(filePath) === '.txt')
            {
                let content = fs.readFileSync(filePath, 'utf8');
                // check if file is not script file itself
                if (filePath !== textFileName)
                {
                    fileContents.push(content);
                }
            }
        }
    }

    traverseFolder(directory);

    fs.writeFileSync(outputFilePath, fileContents.join('\n'), 'utf8');

    console.log(`Combined ${fileContents.length} .txt files into ${outputFilePath}`);
}

// get current directory of script
let currentDirectory = process.cwd();

// get filename of script
let textFileName = __filename;

combineTextFiles(currentDirectory, textFileName);