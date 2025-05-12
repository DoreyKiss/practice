# This repository contain exercises I have done during the years.

[advanced python](),
[decorators](),
[design patterns](https://www.linkedin.com/learning/python-design-patterns-2021),

### Local Python Environment Setup

this project uses [poetry](https://python-poetry.org/docs/#installing-with-pipx).

1. Install required tools, and select the environment.

```bash
    brew install poetry
    poetry env use python3.12 
```
2. check envs

```bash
    poetry env list 
    poetry env info  
```

3. If the virtual env is not active activate by hand.

```bash
    poetry env activate
```

4. install dependencies

```bash
    poetry install 
```

### Selecting the interpreter:

paste the output of this script to the interpreter path

```bash
    poetry env info --path 
```

### for a fresh start, try these:

```bash
    poetry cache clear --all pypi     # Clear cache
    poetry env remove --all           # Reset environment
    rm poetry.lock && poetry install  # Start fresh
```

### Adding packages using poetry:

1. adding dependencies

```bash
    poetry add requests
```

2. adding dev dependencies

```bash
    poetry add --dev pytest-playwright
```

4. install browsers

```bash
    poetry run playwright install firefox chromium
```

### Running code  

1. for running all pytests
```bash
    poetry run hello
```

2. for playwright tests
```bash
    poetry run pytest -m playwright  
```

### Extensions

[python](https://marketplace.visualstudio.com/items?itemName=ms-python.python),
[pylance](https://marketplace.visualstudio.com/items?itemName=ms-python.vscode-pylance),
[python debugger](https://marketplace.visualstudio.com/items?itemName=ms-python.debugpy),
for  [toml](https://marketplace.visualstudio.com/items?itemName=tamasfe.even-better-toml) file,
for  [spell checking](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker).

### Code Quality

[flake8](https://pypi.org/project/flake8/),
[isort](https://pypi.org/project/isort/),
[black](https://pypi.org/project/black/),

