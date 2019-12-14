# Github Analyzer

Ability to analyze the repository and return meaningful information out of it

### Local Testing

Create virtual environment by:

`python -m venv myvenv`

Then to install this package, do:

`pip install .`

This will install it into your virtual environment and to remove do:

`pip uninstall github-analyzer`

### Testing

`import github_analyzer`

`client = github_analyzer.Client()`

`data = client.repository.fetch('shashank-sharma', 'mythical-feedback')`

Now you'll get the data
