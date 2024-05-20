import setuptools
from setuptools import find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


__version__ = '0.0.0'
REPO_NAME = 'DL_Chicken_Disease_Classification_AWS_AZURE_DVC'
AUTHOR_USER_NAME = 'psun6789'
SRC_REPO = 'ImageClassification'
AUTHOR_EMAIL = 'petersunny6789@gmail.com'


setuptools.setup(
    name = SRC_REPO,
    version= __version__,
    author= AUTHOR_USER_NAME, 
    author_email= AUTHOR_EMAIL,
    description='Python package for CNN Image Classification on Chicken Disease Dataset',
    long_description= long_description,
    long_description_content = 'text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls = {
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issue',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src')

)