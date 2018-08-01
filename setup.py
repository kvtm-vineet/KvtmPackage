import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="KvtmPackage",
    version="0.0.1",
    author="Vineet Mehenwal",
    author_email="vineet.mehenwal@kvantuminc.com",
    description="A small package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kvtm-vineet/KvtmPackage",
    packages=setuptools.find_packages(),
    install_require=[
        "numpy==1.11.2"
    ],
    classifiers=(
        "Programming Language :: Python :: 2.7",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
    ),
)