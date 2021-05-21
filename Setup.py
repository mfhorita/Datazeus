# coding=UTF-8

from setuptools import setup
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='autotasks',
    version='1.0.7',
    author='Marcelo Horita',
    author_email='mfhorita@gmail.com.br',
    packages=['autotasks'],
    description='Pacote de automação de processos',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mfhorita',
    license='MIT License',
    keywords='autotasks vba rpa msg pdf web scrapy sys',
    classifiers=[
        'License :: Freeware',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Development Status :: 5 - Production/Stable',
        'Natural Language :: Portuguese (Brazilian)',
        'Intended Audience :: Developers',
        'Topic :: Utilities'],
    install_requires=[
        'PyAutoGUI>=0.9.47',
        'beautifulsoup4>=4.8.0',
        'selenium==3.7.0',
        'pytesseract>=0.3.0',
        'psutil>=5.7.0',
        'pywin32>=223',
        'PyPDF2>=1.26.0'
    ]
)