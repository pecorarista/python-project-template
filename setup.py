from setuptools import setup


setup(name='mypkg',
      version='1.0',
      description='Example Package',
      author='Miyazawa Akira',
      author_email='pecorarista@gmail.com',
      url='https://github.com/pecorarista/python-project-template',
      entry_points={"console_scripts": ["mypkg = mypkg.main:main"]},
      test_suite='tests')
