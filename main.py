import gitignore_template_fetcher, gitignore_selector, gitignore_writer

if __name__ == '__main__':
    repo_dir: str = gitignore_template_fetcher.gitignore_template_fetcher.clone_repo()
    answers = gitignore_selector.gitignore_selector.select_filenames(repo_dir)
    gitignore_writer.gitignore_writer.write_result("~/.global_gitignore")
