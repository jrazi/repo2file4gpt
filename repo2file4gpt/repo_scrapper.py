from .gh_api_wrapper import GithubAPIWrapper
from .markdown_exporter import MarkdownExporter


class RepositoryScraper:
    def __init__(self, token, filetypes, line_limits):
        self.github = GithubAPIWrapper(token)
        self.exporter = MarkdownExporter()
        self.filetypes = filetypes
        self.line_limits = line_limits

    def get_repo_content(self, repo, path=""):
        contents = self.github.get_contents(repo, path)
        for content in contents:
            if content.type == "dir":
                self.get_repo_content(repo, content.path)
            else:
                if content.path.endswith(tuple(self.filetypes)):
                    self.exporter.write_file_content(
                        content, content.path.split(".")[-1]
                    )

    def process_repository(self, url):
        repo = self.github.get_repo(url)
        repo_name = url.split("/")[-1]
        self.exporter.open_file(f"{repo_name}.md")
        self.exporter.write_header(repo_name)
        self.exporter.write_metadata(repo)
        self.get_repo_content(repo)
        self.exporter.close_file()

    def process_repositories(self, repo_urls):
        for url in repo_urls:
            self.process_repository(url)
