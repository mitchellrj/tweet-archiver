import sys

from setuptools import setup


requires = ['tweepy']

if sys.version_info < (2, 6):
    requires.append('simplejson')


setup(
    name = 'tweet-archiver',
    version = '0.1',
    author = 'Alex Muller',
    author_email = 'alex@mullr.net',
    description = 'Get full Tweet metadata given a list of status IDs.',
    long_description = open('README.rst').read(),
    zip_safe = True,
    packages = ['tweet_archiver'],
    include_package_data=True,
    install_requires = requires,
    entry_points = {
        'console_scripts' : [
            'tweet-archiver = tweet_archiver:main'
        ]
    }
)
