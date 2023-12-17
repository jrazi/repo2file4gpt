import logging
from tqdm import tqdm
from .gh_api_wrapper import GithubAPIWrapper
from .markdown_exporter import MarkdownExporter


class RepositoryScraper:
    def __init__(self, token, filetypes, line_limits, output_dir):
        self.github = GithubAPIWrapper(token)
        self.exporter = MarkdownExporter(output_dir)
        self.filetypes = filetypes
        self.line_limits = line_limits

    def get_repo_content(self, repo, path="", pbar=None):
        contents = self.github.get_contents(repo, path)
        for content in contents:
            if content.type == "dir":
                self.get_repo_content(repo, content.path, pbar)
            else:
                if content.path.endswith(tuple(self.filetypes)):
                    message = self.exporter.write_file_content(
                        content, content.path.split(".")[-1]
                    )
                    if message is not None:
                        logging.warning(message)
            pbar.update()

    def process_repository(self, url, pbar):
        repo, repo_name = self.github.get_repo(url)
        owner_handle = repo.owner.login
        total_files = self.github.estimate_total_files(repo)
        self.exporter.open_file(f"{owner_handle}_{repo_name}.md")
        self.exporter.write_header(repo_name)
        self.exporter.write_metadata(repo)
        with tqdm(
            total=total_files,
            desc=f"Processing {repo.full_name}",
            ncols=70,
            position=1,
            leave=False,
        ) as pbar2:
            self.get_repo_content(repo, pbar=pbar2)
        self.exporter.close_file()
        pbar.update()

    def process_repositories(self, repo_urls):
        print(f"Processing {len(repo_urls)} repositories\n")
        print("Please checkout the log file for additional logs and error reports\n")
        with tqdm(
            total=len(repo_urls), desc="Overall Progress", ncols=70, position=0
        ) as pbar:
            for url in repo_urls:
                self.process_repository(url, pbar)
