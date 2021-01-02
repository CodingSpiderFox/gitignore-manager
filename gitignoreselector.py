from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import glob


def get_available_filenames(repo_dir):
    return glob.glob(repo_dir + "/Global/**.gitignore")


class GitignoreSelector:

    @staticmethod
    def select_filenames(repo_dir: str):
        filenames: str = get_available_filenames(repo_dir)

        filename_choices = []
        for filename in filenames:
            filename = filename.replace(repo_dir + "/Global/", "")
            file_name_choice_item = {'name': filename}
            filename_choices.append(file_name_choice_item)

        questions = [
            {
                'type': 'checkbox',
                'qmark': '😃',
                'message': 'Select gitignore files to concatenate',
                'name': 'gitignores',
                'choices': filename_choices,
                'validate': lambda answer: 'You must choose at least one file.'
                if len(answer) == 0 else True
            }
        ]

        answers = prompt(questions)
        return answers
