class GitignoreWriter:

    @staticmethod
    def write_result(target_path: str, source_file_names: [], repo_dir: str):

        result_file_content : str = "################## gitignore-manager-contents below this line\r\n"

        for source_file_name in source_file_names:
            result_file_content += "################## " + source_file_name + " ##################\r\n"
            with open(repo_dir + "/Global/" + source_file_name, 'r') as file:
                result_file_content += file.read() + "\r\n\r\n"

        with open(target_path, 'a+') as file:
            file.write(result_file_content)
