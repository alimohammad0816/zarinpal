from setuptools import setup, find_packages
import pathlib


def get_requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with pathlib.Path(pathlib.Path(__file__).parent / "requirements.txt").open() as reqs:
        for install in reqs:
            requirements_list.append(install.strip())

    return requirements_list


setup(
    name='python-zarinpal',
    version='0.1.0',
    author='alimohammad0816',
    author_email='alimohammad0816@gmail.com',
    description='python library for zarin pal rest apis',
    keywords="python zarinpal api wrapper",
    packages=find_packages(),
    install_requires=get_requirements(),
    include_package_data=True,
    license="LGPLv3",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Communications :: Chat",
        "Topic :: Internet",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.8',
)
