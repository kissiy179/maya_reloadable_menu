
from glob import glob
from os.path import basename
from os.path import splitext
from setuptools import setup
from setuptools import find_packages

def _requires_from_file(filename):
    return open(filename).read().splitlines()

setup(
    name="reloadable_menu",
    version="0.2.0",
    license="MIT",
    description=u"再読み込み可能なメニューを実装するパッケージ",
    author="satoshi kishimoto",
    url="",
    packages=find_packages("python"),
    package_dir={"": "python"},
    py_modules=[splitext(basename(path))[0] for path in glob('python/*.py')],
    include_package_data=True,
    zip_safe=False,
    install_requires=_requires_from_file('requirements.txt'),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"]  
)
