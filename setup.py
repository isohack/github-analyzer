with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='github-analyzer',
     version='0.1',
     author="Shashank Sharma",
     author_email="shashank.sharma98@gmail.com",
     description="To analyze Github repositories",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/isohack/github-analyzer",
     packages=['github_analyzer'],
     license='MIT',
 )
