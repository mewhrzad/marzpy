from setuptools import setup, find_packages

with open("README.md", "r") as file:
    readme = file.read()

setup(
    name="marzpy",
    version="0.0.2",
    author="Mewhrzad, IgorDuino",
    description="a simple application with python to manage Marzban panel",
    long_description="text/markdown",
    url="https://github.com/igorDuino/marzpy",
    keywords=["marzpy", "Marzban", "Gozargah", "Marzban python", "Marzban API"],
    packages=find_packages(),
    ins=["requests"],
    classifiers=["Programming Language :: Python :: 3"],
)
