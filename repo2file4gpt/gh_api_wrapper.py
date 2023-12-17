import logging
from github import Github


class GithubAPIWrapper:
    def __init__(self, token):
        self.github = Github(token)

    def get_repo(self, url):
        repo_name = url.split("/")[-1]
        return self.github.get_repo(url.split("/")[-2] + "/" + repo_name), repo_name

    def get_contents(self, repo, path=""):
        try:
            return repo.get_contents(path)
        except Exception as e:
            logging.error(
                f"Error getting contents of {path} in {repo.full_name}: {str(e)}"
            )
            return []

    def estimate_total_files(self, repo, path=""):
        contents = self.get_contents(repo, path)
        total_files = 0
        for content in contents:
            if content.type == "dir":
                total_files += self.estimate_total_files(repo, content.path)
            else:
                total_files += 1
        return total_files
