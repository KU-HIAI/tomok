from setuptools import setup, find_packages

with open('tomok/requirements.txt') as f:
    require_packages = [line[:-1] if line[-1] == '\n' else line for line in f]

setup(name='tomok',
      version='0.1.0',
      url='https://github.com/KU-HIAI/tomok',
      license='Apache-2.0',
      author='Taemin Lee',
      author_email='persuade@gmail.com',
      description='TOMOK',
      packages=find_packages(),
      long_description=open('README.md', 'r', encoding='utf-8').read(),
      long_description_content_type="text/markdown",
      python_requires='>=3',
      zip_safe=False,
      include_package_data=True,
      classifiers=(
          'Programming Language :: Python :: 3.8',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering',
      ),
      install_requires=require_packages,
      keywords="TOMOK"
      )