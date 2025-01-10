from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from _version_ variable in simpel/_init_.py
from Simpel import _version_ as version

setup(
	name="skippers",
	version=version,
	description="app for Simpel",
	author="Kamal Solanki",
	author_email="kamal@simpel.ai",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
