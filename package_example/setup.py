import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packagename-pkg-atd",
    version="0.0.1",
    author="atd-code",
    author_email="anthony.demong@live.ca",
    description="package description",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/atd-code/modules",
    project_urls={
        "Issues": "https://github.com/atd-code/modules/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
