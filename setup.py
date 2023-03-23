from setuptools import setup

setup(
    name='pybtex-biblatex',
    description='Pybtex bibLaTeX plugin',
    version='0.0.1',
    author='Vanja Štefanec',
    packages=['pybtex_biblatex'],
    entry_points={
        'pybtex.database.input': 'biblatex = pybtex_biblatex:BibLaTeXParser',
        'pybtex.database.input.suffixes': '.bib = pybtex_biblatex:BibLaTeXParser',
        'pybtex.database.output': 'biblatex = pybtex_biblatex:BibLaTeXWriter',
        'pybtex.database.output.suffixes': '.bib = pybtex_biblatex:BibLaTeXWriter',
    },
    install_requires=['pybtex', 'pylatexenc']
)
