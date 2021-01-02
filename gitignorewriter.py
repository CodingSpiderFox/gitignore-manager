import os


class GitignoreWriter:

    @staticmethod
    def write_result(target_path: str, source_file_names: [], repo_dir: str):

        result_file_content: str = "################## gitignore-manager-contents below this line\r\n"

        for source_file_name in source_file_names:
            result_file_content += "################## " + source_file_name + " ##################\r\n"
            with open(repo_dir + "/Global/" + source_file_name, 'r') as file:
                result_file_content += file.read() + "\r\n\r\n"

        if os.path.exists(target_path):
            file_writing_mode = 'a+'  # append if already exists
        else:
            file_writing_mode = 'w'  # make a new file if not

        with open(target_path, file_writing_mode) as target_file:
            target_file.write(result_file_content)
