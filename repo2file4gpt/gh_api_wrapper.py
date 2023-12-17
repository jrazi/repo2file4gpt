from github import Github


class GithubAPIWrapper:
    def __init__(self, token):
        self.github = Github(token)

    def get_repo(self, url):
        repo_name = url.split("/")[-1]
        return self.github.get_repo(url.split("/")[-2] + "/" + repo_name)

    def get_contents(self, repo, path=""):
        return repo.get_contents(path)
