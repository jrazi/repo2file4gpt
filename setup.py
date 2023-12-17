from setuptools import setup, find_packages

setup(
    name="repo2file4gpt",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["PyGithub", "tqdm"],
)
