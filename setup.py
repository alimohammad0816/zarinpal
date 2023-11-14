from setuptools import setup, find_packages
from pathlib import Path


def get_requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with Path("requirements.txt").open() as reqs:
        for install in reqs:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name='python-zarinpal',
    version='0.1.0',
    author='alimohammad0816',
    author_email='alimohammad0816@gmail.com',
    description='python library for zarin pal rest apis',
    packages=find_packages(),
    install_requires=get_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
)
