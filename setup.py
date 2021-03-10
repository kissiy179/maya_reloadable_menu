from glob import glob
from os.path import basename
from os.path import splitext
from os.path import exists
from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    if not exists(filename):
        return []
    
    return open(filename).read().splitlines()

setup(
    name='mayapy_package_utilities',
    version='0.1.0',
    package_dir={"": "python"},
    packages=find_packages("python"),
    py_modules=[splitext(basename(path))[0] for path in glob('python/*.py')],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=2.7",
    install_requires=_requires_from_file('requirements.txt'),
)
