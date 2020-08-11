from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent  # The text of the README file

# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
README = (HERE / "README.md").read_text()
with open(path.join(HERE, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if ('git+' not in x) and (
    not x.startswith('#')) and (not x.startswith('-'))]

dependency_links = [x.strip().replace('git+', '') for x in all_reqs
                    if 'git+' not in x]

setup(
    name='mandarin_corpus_gen',
    description='A simple word frequencies generator given input text',
    version='1.0.0a1',
    packages=find_packages(),  # list of all packages
    install_requires=install_requires,
    python_requires='>=3.6',  # because of tensorflow
    entry_points='''
        [console_scripts]
        mandarin_corpus_gen=mandarin_corpus_generator.driver:process
    ''',
    author="Bryan Kok",
    keywords="corpus mandarin　extraction　histogram　pos",
    long_description=README,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Gate-of-Jade/corpus-generation',
    # download_url='https://github.com/CITGuru/cver/archive/1.0.0.tar.gz',
    dependency_links=dependency_links,
    author_email='bryan.wyern1@gmail.com',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ]
)
