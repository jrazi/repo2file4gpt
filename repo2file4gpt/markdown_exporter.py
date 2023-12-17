import os
import logging


class MarkdownExporter:
    def __init__(self, output_dir="./outputs"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs("./logs", exist_ok=True)
        logging.basicConfig(
            filename="./logs/app.log",
            filemode="w",
            format="%(name)s - %(levelname)s - %(message)s",
            level=logging.INFO,
        )

    def open_file(self, filename):
        self.file = open(os.path.join(self.output_dir, filename), "w", encoding="utf-8")
        logging.info(f"Processing {filename}")

    def close_file(self):
        logging.info(f"Finished processing {self.file.name}")
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
        message = None
        try:
            if content.encoding == "base64":
                print(content.decoded_content.decode(), file=self.file)
            else:
                message = f"Content of {content.path} could not be decoded. Encoding: {content.encoding}"
        except Exception as e:
            message = f"Error processing content of {content.path}: {str(e)}"
        print("```", file=self.file)
        return message
