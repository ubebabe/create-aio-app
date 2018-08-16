import os
import re

from setuptools import find_packages, setup


REGEXP = re.compile(r"^__version__\W*=\W*'([\d.abrc]+)'")


def read_version():

    init_py = os.path.join(
        os.path.dirname(__file__),
        '_ms_',
        '__init__.py',
    )

    with open(init_py) as f:
        for line in f:
            match = REGEXP.match(line)
            if match is not None:
                return match.group(1)
        else:
            msg = f'Cannot find version in ${init_py}'
            raise RuntimeError(msg)


install_requires = [
    'aiohttp',
    'aiopg[sa]',
    'aiohttp_jinja2',
    'trafaret_config',
    'markdown2',
]


setup(
    name='_ms_',
    version=read_version(),
    description='_ms_',
    platforms=['POSIX'],
    packages=find_packages(),
    package_data={
        '': ['config/*.*']
    },
    include_package_data=True,
    install_requires=install_requires,
    zip_safe=False,
)
