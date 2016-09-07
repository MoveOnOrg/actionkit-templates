from setuptools import find_packages, setup
import textwrap

setup(
    name='actionkit-templates',
    version='0.1',
    author='Schuyler Duveen',
    packages=find_packages(),
    package_data={'actionkit_templates': ['templates/*.html']},
    url='https://github.com/MoveOnOrg/actionkit-templates',
    license='GPL3',
    description="actionkit-templates allows you to view your ActionKit templates locally testing different configurations for each page type.  It also documents by-code many context variables for each page",
    long_description=textwrap.dedent(open('README.md', 'r').read()),
    entry_points={
        'console_scripts': [
            'aktemplateserve = actionkit_templates.aktemplateserve:serve_templates',
        ],
    },
    install_requires=[
        'Django==1.8',
    ],
    keywords = "python actionkit",
    classifiers=['Development Status :: 4 - Beta', 'Environment :: Console', 'Intended Audience :: Developers', 'Natural Language :: English', 'Operating System :: OS Independent', 'Topic :: Internet :: WWW/HTTP'],
)
