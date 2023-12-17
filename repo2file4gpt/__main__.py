import os

from .config import REPO_URLS, FILETYPES, LINE_LIMITS
from repo2file4gpt.repo_scrapper import RepositoryScraper


def main():
    processor = RepositoryScraper(
        os.getenv("GITHUB_ACCESS_TOKEN"), FILETYPES, LINE_LIMITS
    )
    processor.process_repositories(REPO_URLS)


if __name__ == "__main__":
    main()
