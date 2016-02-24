from setuptools import setup

setup(
    name='CodeforcesImporter',
    version='v1.0',
    packages=['', 'codeforces_importer', 'codeforces_importer.Entity', 'codeforces_importer.classifier'],
    url='https://github.com/dragonslayerx/CodeforcesImporter',
    license='',
    author='dragonslayerx',
    author_email='swapnilsaxena@live.in',
    install_requires=[
          'lxml', 'jinja2', 'requests'
    ],
    description='Just a small script for importing user statistics and past submissions on codeforces'
)
