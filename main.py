import gitignoretemplatefetcher, gitignoreselector, gitignorewriter

if __name__ == '__main__':
    repo_dir: str = gitignoretemplatefetcher.GitignoreTemplateFetcher.clone_repo()
    source_file_names = gitignoreselector.GitignoreSelector.select_filenames(repo_dir).get("gitignores")
    gitignorewriter.GitignoreWriter.write_result(".global_gitignore", source_file_names, repo_dir)
    print("Check the result file \".gitignore_global\" and after creating a backup of the old one, manually copy it "
          "to your home directory if it's correct.")
