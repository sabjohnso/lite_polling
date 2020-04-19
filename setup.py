import setuptools

import sphinx
from sphinx.setup_command import BuildDoc
cmdclass = {'build_sphinx': BuildDoc}

with open('README.rst', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="lite_polling",
    version="0.1.0",
    author="Samuel B. Johnson",
    author_email="sabjohnso.dev@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/x-rst",
    url = "https://github.com/sbjohnso/lite_polling",
    license = "MIT",
    packages = setuptools.find_packages(),
    cmdclass = cmdclass,
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Idependent"
    ],
    python_requires = ">=3.4",
    command_options = {
        'build_sphinx' : {
            'source_dir' :  ('setup.py', 'doc/source')}}
)


