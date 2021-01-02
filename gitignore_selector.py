from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import glob

def get_available_filenames(repo_dir):
    return glob.glob(repo_dir + "/Global/**.gitignore")

class gitignore_selector:

    def select_filenames(repo_dir: str):
        filenames: str = get_available_filenames(repo_dir)

        questions = [
            {
                'type': 'checkbox',
                'qmark': '😃',
                'message': 'Select gitignore files to concatenate',
                'name': 'gitignores',
                'choices': [
                    filenames
                ],
                'validate': lambda answer: 'You must choose at least one file.'
                if len(answer) == 0 else True
            }
        ]

        answers = prompt(questions)
        return answers
