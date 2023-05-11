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


    for i in range(1, 11):
        problemFileName = f"problem{i:02d}.txt"
        solutionFileName = f"solution{i:02d}.txt"

        counter = 0
        
        FUNCTION_NAMES = ["foo", "bar"]
        PARAMS = ["arr", "inArr"]
        VARIABLE_1 = ["nthreads", "threadNum"]
        VARIABLE_2 = ["output", "total"]
        VARIABLE_3 = ["s_priv", "resultArr"]
        VARIABLE_4 = ["ARRAY_SIZE", "SIZE"]
        VARIABLE_PAD = ["PADDING", "PAD"]

        for f in range(0, len(FUNCTION_NAMES)):
            for p in range(0, len(PARAMS)):
                for v1 in range(0, len(VARIABLE_1)):
                    for v2 in range(0, len(VARIABLE_2)):
                        for v3 in range(0, len(VARIABLE_3)):
                            for v4 in range(0, len(VARIABLE_4)):

                                # Problem text
                                with open(f"Files\\{problemFileName}", "r") as file:
                                    content = file.read()
                                    content = content.replace("<FUNC_NAME>", FUNCTION_NAMES[f])
                                    content = content.replace("<PARAM_1>", PARAMS[p])
                                    content = content.replace("<VAR_1>", VARIABLE_1[v1])
                                    content = content.replace("<VAR_2>", VARIABLE_2[v2])
                                    content = content.replace("<VAR_3>", VARIABLE_3[v3])
                                    content = content.replace("<VAR_4>", VARIABLE_4[v4])
                                    temp = problemFileName.replace(".txt", "")
                                    with open(f"AugmentedData\\{temp}_augment{counter}.txt", "w") as oFile:
                                        oFile.write(content)

                                for vp in range(0, len(VARIABLE_PAD)):
                                    # Solution text
                                    with open(f"Files\\{solutionFileName}", "r") as file:
                                        content = file.read()
                                        content = content.replace("<FUNC_NAME>", FUNCTION_NAMES[f])
                                        content = content.replace("<PARAM_1>", PARAMS[p])
                                        content = content.replace("<VAR_1>", VARIABLE_1[v1])
                                        content = content.replace("<VAR_2>", VARIABLE_2[v2])
                                        content = content.replace("<VAR_3>", VARIABLE_3[v3])
                                        content = content.replace("<VAR_4>", VARIABLE_4[v4])
                                        content = content.replace("<VAR_PAD>", VARIABLE_PAD[vp])
                                        temp = solutionFileName.replace(".txt", "")
                                        with open(f"AugmentedData\\{temp}_augment{counter}.txt", "w") as oFile:
                                            oFile.write(content)
                                
                                counter += 1
        break





    # for root, dirs, files in os.walk(FILE_PATH):
    #     problemCodes = ["" for _ in range(int(len(files) / 2))]
    #     solutionCodes = ["" for _ in range(int(len(files) / 2))]
    #     codeClasses = [CLASS_OF_CODE for _ in range(int(len(files) / 2))]
    #     for fileName in files:  # for each file in input file path

    #         filePath = os.path.join(FILE_PATH, fileName)
    #         fileNumber = int(fileName[-6:-4])
    #         code = ""
    #         with open(filePath, "r") as file:
    #             lines = file.readlines()
    #             for line in lines:
    #                 code += line.strip() + "$<n>$"

    #             if "solution" in fileName:
    #                 solutionCodes[fileNumber-1] = code
                
    #             elif "problem" in fileName:
    #                 problemCodes[fileNumber-1] = code 



    # generateJSONL(prompData=problemCodes, completionData=codeClasses, outputFileName="data01.jsonl")
    # generateJSONL(prompData=problemCodes, completionData=solutionCodes, outputFileName="data02.jsonl")




if __name__ == "__main__":
    main()
    