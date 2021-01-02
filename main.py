import gitignoretemplatefetcher, gitignoreselector, gitignorewriter

if __name__ == '__main__':
    repo_dir: str = gitignoretemplatefetcher.GitignoreTemplateFetcher.clone_repo()
    source_file_names = gitignoreselector.GitignoreSelector.select_filenames(repo_dir)
    gitignorewriter.GitignoreWriter.write_result("~/.global_gitignore_test", source_file_names, repo_dir)
