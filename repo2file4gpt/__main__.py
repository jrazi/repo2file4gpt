import argparse
from .config import REPO_URLS, FILETYPES, LINE_LIMITS, OUTPUT_DIR
from repo2file4gpt.repo_scrapper import RepositoryScraper
import os

def main():
    parser = argparse.ArgumentParser(description="Process some repositories.")
    parser.add_argument("--token", type=str, help="GitHub access token")
    parser.add_argument("--repos", type=str, nargs="+", help="List of repository URLs to process")
    parser.add_argument("--filetypes", type=str, nargs="+", help="List of file types to process")
    parser.add_argument("--output_dir", type=str, help="Output directory")

    args = parser.parse_args()

    token = args.token if args.token else os.getenv("GITHUB_ACCESS_TOKEN")
    repos = [repo.strip() for repo in args.repos] if args.repos else REPO_URLS
    filetypes = [ftype.strip() for ftype in args.filetypes] if args.filetypes else FILETYPES
    output_dir = args.output_dir.strip() if args.output_dir else OUTPUT_DIR

    processor = RepositoryScraper(token, filetypes, LINE_LIMITS, output_dir)
    processor.process_repositories(repos)

if __name__ == "__main__":
    main()
