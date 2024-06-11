from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="exputils",  # Replace with your own project name
    version="0.1.0",
    author="Shibo Li",
    author_email="shiboli.cs@gmail.com",
    description="Some convinient tools for experiments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shib0li/exputils",  # Replace with your project's URL
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        # List your project's dependencies here.
        # You can use requirements.txt to specify dependencies in a separate file.
    ],
)