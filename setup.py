import setuptools

with open("requirements.txt") as fp:
    install_requires = fp.read()

with open("version.txt") as fp:
    version = fp.readline().strip()

with open("README.md") as fp:
    readme = fp.read()

with open("LICENSE") as f:
    license = f.read()

setuptools.setup(
    name="geomove",
    description="Moves points on earth towards a given bearing by a given distance.",
    long_description=readme,
    version=version,
    license=license,
    author="Marius Merschformann",
    author_email="marius.merschformann@gmail.com",
    url="https://github.com/merschformann/geomove",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
)
