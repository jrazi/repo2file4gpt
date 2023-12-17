import os


class MarkdownExporter:
    def __init__(self, output_dir="./outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def open_file(self, filename):
        self.file = open(os.path.join(self.output_dir, filename), "w", encoding="utf-8")

    def close_file(self):
        self.file.close()

    def write_header(self, repo_name):
        print(
            f"# Title: The Content of Github Repository {repo_name}\n", file=self.file
        )
        print("## Content Structure\n", file=self.file)
        print(
            "The content of repository are stored in this single file. First, there will appear the README.md content. After that, the directory structure of the repository will be specified. In the following sections, with a depth-first approach, the content of the repository files will be displayed.\n",
            file=self.file,
        )

    def write_metadata(self, repo):
        print("## Repository Metadata\n", file=self.file)
        print(f"**Number of Stars:** {repo.stargazers_count}\n", file=self.file)
        print(f"**Number of Forks:** {repo.forks_count}\n", file=self.file)
        print(f"**Latest Update Date:** {repo.updated_at}\n", file=self.file)
        print(f"**Repository Creation Date:** {repo.created_at}\n", file=self.file)
        print(f"**Crawled Branch:** {repo.default_branch}\n", file=self.file)

    def write_file_content(self, content, filetype):
        print(f"\n### {content.path}\n", file=self.file)
        print(f"```{filetype}", file=self.file)
        print(content.decoded_content.decode(), file=self.file)
        print("```", file=self.file)
