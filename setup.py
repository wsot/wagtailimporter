from setuptools import setup, find_packages

with open('README.md') as readme, \
     open('requirements.txt') as requirements:
    setup(
        name="wagtailimporter",
        version="0.0.1",
        description="Wagtail module to load pages from Yaml",
        long_description=readme.read(),
        url='https://github.com/squareweave/wagtailimporter',
        author='Squareweave',
        author_email='team@squareweave.com.au',
        license='BSD',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
        ],
        packages=find_packages(),
        install_requires=requirements.readlines(),
    )