import io

class gitignore_writer:

    def write_result(targetPath : str, sourceFileNames: []):

        resultFileContent : str = "################## gitignore-manager-contents below this line\r\n";

        for sourceFileName in sourceFileNames:
            resultFileContent += "################## " + sourceFileName + " ##################\r\n"
            with open(sourceFileName, 'r') as file:
                resultFileContent += file.read() + "\r\n\r\n"

        with open(targetPath, 'a+') as file:
            file.write(resultFileContent)
