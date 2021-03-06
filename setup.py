import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitflag",
    version="2.0.0",
    author="Travis Clarke",
    author_email="travis.m.clarke@gmail.com",
    description="A bit flag class for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/clarketm/bitflag",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
