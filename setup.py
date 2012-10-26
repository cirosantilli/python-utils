from distutils.core import setup

setup(
    name='cirosantilli',
    version='0.1.0',
    author='Ciro Duran Santilli',
    author_email='ciro.santilli@gmail.com',
    packages=['cirosantilli'],
    scripts=[
        'bin/stowe-towels.py',
        ],
    url='https://github.com/cirosantilli/',
    license='license.md', #GPL, BSD, or MIT. firefox http://www.codinghorror.com/blog/2007/04/pick-a-license-any-license.html 
    description='my simple python scripts and modules',
    long_description=open('readme.md').read(),
    install_requires=[
        "termcolor >= 1.1.0",
        "unidecode >= 0.04.9",
    ],
)
