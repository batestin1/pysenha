
from setuptools import setup

from setuptools import find_packages

setup(
    name = 'pysenha',
    version = '4.0.0',
    author = 'Bates',
    author_email = 'Bates@mailer.com.br',
    packages = ['pysenha'],
    description = 'a way to make your life easier',
    long_description = 'file: README.md',
    url = 'https://github.com/batestin1/',
    project_urls = {'Download' : 'https://github.com/batestin1/', 'Codigo fonte' : 'https://github.com/batestin1/'},
    keywords = 'a way to make your life easier',
    classifiers = [],
    install_requires=[
            'yagmail',
            'datetime'
        ]
)