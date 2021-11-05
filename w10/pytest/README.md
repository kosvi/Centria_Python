# Pytest & Github workflow

### Requirements.txt

First create **requirements.txt** with command `pip freeze > requirements.txt`. Store requirements.txt to project root. You might want to clean the file since I got a ton of non-required crap in the generated requirements-file. 

### Create workflow

To project root create folder: `.github/workflows/`

Create `python-tests.yml` to newly created directory. You can check out the working content from [my repository](/.github/workflows/python-tests.yml). 

### Run tests

Now every push to repo runs pytest to automatically test your code. You can see the results by opening the *Actions* tab from top of the page. 
