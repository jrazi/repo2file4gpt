# 📁 repo2file4gpt

repo2file4gpt is a Python package that scrapes GitHub repositories and exports their content into structured markdown files. The goal is to convert repository content into a machine-readable format for use in AI training data.

It extracts key files like code, markdown, and notebooks from public GitHub repositories. The content is exported into an aggregated markdown file per repository with the full hierarchy preserved.

## Installation

You can install repo2file4gpt directly from PyPI:

```bash
pip install repo2file4gpt
```

## Quick Start

### Command Line Interface

After installing repo2file4gpt, you can use it from the command line as follows:

```bash
repo2file4gpt --token YOUR_GITHUB_TOKEN --repos user/repo1 user/repo2 --filetypes py js --output_dir ./outputs/
```

Replace `YOUR_GITHUB_TOKEN` with your actual GitHub token, and `user/repo1` and `user/repo2` with the actual repositories you want to process.

### Python Code

You can also use repo2file4gpt in your Python code:

```python
import repo2file4gpt

# Specify the GitHub token, list of repositories, file types, and output directory
token = "YOUR_GITHUB_TOKEN"
repos = ["user/repo1", "user/repo2"]
filetypes = ["py", "js"]
output_dir = "./outputs/"

# Create a RepositoryScraper instance
processor = repo2file4gpt.RepositoryScraper(token, filetypes, repo2file4gpt.LINE_LIMITS, output_dir)

# Process the repositories
processor.process_repositories(repos)
```

Again, replace `YOUR_GITHUB_TOKEN` with your actual GitHub token, and `user/repo1` and `user/repo2` with the actual repositories you want to process.

## TODO

- Add support for more file types.
- Improve error handling for robustness.
- Optimize performance for large repositories.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
