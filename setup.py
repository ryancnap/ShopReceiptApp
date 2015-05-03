# Working example of a setup.py file. 
# The readme.txt, license.txt, and __init__.py files were also added for this.

from distutils.core import setup

setup(
	name = 'ShopReceipt',
	version = '0.1dev',
	packages = ['shopreceipt',],
	license = 'GNU Greater Public License',
	long_description = open('README.txt').read(),
)

