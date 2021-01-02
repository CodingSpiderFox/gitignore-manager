from git import Repo
import os

class GitignoreTemplateFetcher:

    def __init__(self):
        pass

    @staticmethod
    def clone_repo():
        repo_dir : str = "./gitignore-templates"

        if not os.path.exists(repo_dir):
            Repo.clone_from("https://github.com/github/gitignore", repo_dir)

        return repo_dir
