import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='github-analyzer',
     version='0.2',
     author="Shashank Sharma",
     author_email="shashank.sharma98@gmail.com",
     description="To analyze Github repositories",
     long_description=long_description,
     long_description_content_type="text/markdown",
     license='MIT',
     install_requires=["requests"],
     include_package_data=True,
     url="https://github.com/isohack/github-analyzer",
     packages=['github_analyzer', 'github_analyzer.resources', 'github_analyzer.constants'],
     package_dir={'github_analyzer': 'github_analyzer', 'github_analyzer.resources': 'github_analyzer/resources'},
 )
