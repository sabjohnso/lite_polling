import setuptools

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lite_polling",
    version="0.1.0",
    author="Samuel B. Johnson",
    author_email="sabjohnso@yahoo.com",
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    url = "https://github.com/sbjohnso/lite_polling",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Idependent"
    ],
    python_requires = ">=3.4"
)


