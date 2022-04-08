#!/usr/bin/env python3
from setuptools import setup

from version import __version__


with open("README.md") as f:
    long_description = f.read()

setup(
    name="telegram-send",
    version=__version__,
    description="Send messages and files over Telegram from the command-line.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rahiel/telegram-send",
    license="GPLv3+",

    python_requires=">=3.6",
    py_modules=["telegram_send", "version"],
    install_requires=["python-telegram-bot>=12.1.1", "colorama", "appdirs"],
    entry_points={"console_scripts": ["telegram-send=telegram_send.telegram_send:main"]},

    author="Rahiel Kasim",
    author_email="rahielkasim@gmail.com",
    # https://pypi.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # "Development Status :: 4 - Beta",
        "Development Status :: 5 - Production/Stable",
        # "Development Status :: 6 - Mature",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities"
    ],
    keywords="telegram send message file"
)
