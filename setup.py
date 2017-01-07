from setuptools import setup
setup(
  name = 'pycricbuzz',
  packages = ['pycricbuzz'], 
  version = '0.7',
  description = 'A library for fetching live cricket scores from cricbuzz',
  author = 'Shivam Mitra',
  author_email = 'shivamm389@gmail.com',
  license = 'GPLv2',
  url = 'https://github.com/codophobia/pycricbuzz', 
  download_url = 'https://github.com/codophobia/pycricbuzz/tarball/0.6', 
  keywords = ['cricket', 'cricbuzz'], 
  install_requires=[
          'requests',
          'beautifulsoup4',
      ],
  classifiers = [],
)
