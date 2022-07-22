from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='script for sort files in folder',
      url='https://github.com/PavelStelmakhV/script-for-clean-folder',
      author='Stelmakh Pavel',
      author_email='stelmahpv13@ukr.net',
      license='MIT',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ]
)