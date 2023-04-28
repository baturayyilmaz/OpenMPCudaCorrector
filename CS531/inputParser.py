import os

def generateJSONL(prompData, completionData, outputFileName):
    FILE_PATH="C:\\Users\\suuser\\Desktop\\PythonWorkspace\\CS531\\jsonlFiles"
    outputFilePath = os.path.join(FILE_PATH, outputFileName)
    
    with open(outputFilePath, "w") as file:

        for i in range(len(prompData)):
            prompt = prompData[i]
            completion = completionData[i]

            seperator = "->" # last line of problem02.txt is important for this otherwise this separator becomes too long
            # prompt suffix = '$<n>$ ->'
            endingToken = "##" # last line of solution04.txt is important for this otherwise this separator becomes too long
            # completion suffix = "$<n>$ ##"

            line = f"{{\"prompt\":\"{prompt} {seperator}\", \"completion\":\"{completion} {endingToken}\"}}\n"
            file.write(line)

        
        

def main():
    FILE_PATH="C:\\Users\\suuser\\Desktop\\PythonWorkspace\\CS531\\Files\\"
    CLASS_OF_CODE="cache locality"
    problemCodes = []
    solutionCodes = []
    codeClasses=[]

    for root, dirs, files in os.walk(FILE_PATH):
        problemCodes = ["" for _ in range(int(len(files) / 2))]
        solutionCodes = ["" for _ in range(int(len(files) / 2))]
        codeClasses = [CLASS_OF_CODE for _ in range(int(len(files) / 2))]
        for fileName in files:  # for each file in input file path

            filePath = os.path.join(FILE_PATH, fileName)
            fileNumber = int(fileName[-6:-4])
            code = ""
            with open(filePath, "r") as file:
                lines = file.readlines()
                for line in lines:
                    code += line.strip() + "$<n>$"

                if "solution" in fileName:
                    solutionCodes[fileNumber-1] = code
                
                elif "problem" in fileName:
                    problemCodes[fileNumber-1] = code 

    generateJSONL(prompData=problemCodes, completionData=codeClasses, outputFileName="data01.jsonl")
    generateJSONL(prompData=problemCodes, completionData=solutionCodes, outputFileName="data02.jsonl")




if __name__ == "__main__":
    main()
    