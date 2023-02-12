from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
  'Programming Language :: Python :: 3'
]

setup(
    name ='Ethical',
    version='0.0.1',
    description='A python library to assist in writing ethical python code.',
    long_description='A python library to assist in writing ethical python code. A python library to assist in writing ethical python code.',
    url='https://github.com/winstreak1/Ethical',
    author='Peter Mavronicolas',
    author_email='p.mavronicolas@gmail.com',
    license='LPG L',
    classifiers=classifiers,
    keywords='ethical, race, creed, nationality, color, age',
    packages=find_packages(),
    install_requires=['']
)