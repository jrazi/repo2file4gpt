# 📁 repo2file4gpt

## Expanding LLMs Knowledge through Public Codebases

repo2file4gpt facilitates the ingestion of open source GitHub repositories into AI systems, unlocking a vast set of technical knowledge for machine learning.

By structuring and aggregating content in an indexed markdown format, repo2file4gpt prepares the harvested open source intelligence for direct integration into large language models and Q&A systems. The full hierarchy from the original GitHub tree is preserved to retain useful context.

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
