from setuptools import setup

setup(
    name='pybtex-json',
    description='Pybtex bibLaTeX plugin',
    version='0.0.1',
    author='Vanja Štefanec',
    packages=['pybtex_biblatex'],
    entry_points={
        'pybtex.database.input': 'json = pybtex_biblatex:BibLaTeXParser',
        'pybtex.database.input.suffixes': '.bib = pybtex_biblatex:BibLaTeXParser',
    },
    install_requires=['pybtex', 'pylatexenc']
)
