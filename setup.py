from insitu.copernicus.theme.config import PACKAGE_AUTHOR
from insitu.copernicus.theme.config import PACKAGE_AUTHOR_EMAIL
from insitu.copernicus.theme.config import PACKAGE_CLASSIFIERS
from insitu.copernicus.theme.config import PACKAGE_DESCRIPTION
from insitu.copernicus.theme.config import PACKAGE_DOCS_FOLDER
from insitu.copernicus.theme.config import PACKAGE_HISTORY_FILE
from insitu.copernicus.theme.config import PACKAGE_KEYWORDS
from insitu.copernicus.theme.config import PACKAGE_NAME
from insitu.copernicus.theme.config import PACKAGE_NAMESPACE_PACKAGES
from insitu.copernicus.theme.config import PACKAGE_README_FILE
from insitu.copernicus.theme.config import PACKAGE_URL
from insitu.copernicus.theme.config import PACKAGE_VERSION_FILE
from setuptools import setup, find_packages
import os

PATH = PACKAGE_NAME.split('.') + [PACKAGE_VERSION_FILE]
VERSION = open(os.path.join(*PATH)).read().strip()

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=PACKAGE_DESCRIPTION,
    long_description=open(PACKAGE_README_FILE).read() + "\n" +
    open(os.path.join(PACKAGE_DOCS_FOLDER, PACKAGE_HISTORY_FILE)).read(),
    # Get more strings from
    # http://pypi.python.org/pypi?:action=list_classifiers
    classifiers=PACKAGE_CLASSIFIERS,
    keywords=PACKAGE_KEYWORDS,
    author=PACKAGE_AUTHOR,
    author_email=PACKAGE_AUTHOR_EMAIL,
    url=PACKAGE_URL,
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=PACKAGE_NAMESPACE_PACKAGES,
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'plone.app.theming',
        'eea.sentry',
        # -*- Extra requirements: -*-
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.testing',
        ],
    },
)
