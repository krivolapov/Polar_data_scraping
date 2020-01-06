from setuptools import setup

__version__ = '0.1.0b1'

long_description = ''' '''

setup(
    name=parsetcx,
    version=__version__,
    description='A comprehensive parser for Polar .hrm files',
    long_description=long_description,
    url='https://github.com/bradenleith/hrmparser/',
    author='Braden Mitchell',
    author_email='braden.mitchell@mymail.unisa.edu.au',
    py_modules=['hrmparser']
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: GNU GPLv3 License',
        'Operating System :: OS Independent'
        'Programming Language :: Python :: 3'
    ],
    install_requirements=[

    ],
    keywords='heartrate  polar protrainer .hrm'
)
