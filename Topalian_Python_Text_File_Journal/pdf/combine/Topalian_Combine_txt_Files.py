# Topalian_Combine_txt_Files.py

import os

def combineTextFiles(directory, textFileName):
    outputFilePath = os.path.join(directory, 'main.txt')
    fileContents = []

    def traverseFolder(folder):
        for root, dirs, files in os.walk(folder):
            for file in files:
                filePath = os.path.join(root, file)
                if filePath != textFileName and filePath.endswith('.txt'):
                    with open(filePath, 'r', encoding='utf-8') as f:
                        fileContents.append(f.read())

    traverseFolder(directory)

    with open(outputFilePath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(fileContents))
    print(f"Combined {len(fileContents)} .txt files into {outputFilePath}")

# get current directory of script
currentDirectory = os.path.dirname(os.path.abspath(__file__))

# get filename of script
textFileName = os.path.abspath(__file__)

combineTextFiles(currentDirectory, textFileName)