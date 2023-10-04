# learn-git

Using this repo I am learning some essential things about **git**.

### Roadmap

- [x] Publishing python project on `pypi` website using **Github Actions**.
- [ ] Code formatting and linting with **Github Actions**.
- [x] How to use **pre-commit hooks**?
- [ ] Learn `tox` for python project.
- [ ] Learn `cookiecutter` to develop [ml-project-template](https://github.com/arv-anshul/ml-project-template) project.
- [x] Learn how to use `Makefile`.

## 🧑‍🏫 Learn `pre-commit`

**pre-commit** is a very nice tool to ensure code quality by running checks on code before it is committed to the repository.

Literally, you can format and check linting of your code with this before any commit. If you want to do this in your project follow along:

### ⚙️ Installation & Working

1. Install **pre-commit**:

```sh
pip install pre-commit
```

2. Create a **pre-commit config file** at your root directory:

```sh
touch .pre-commit-config.yaml
```

3. Now, **define pre-commit hooks**. For example,

   - You want to check and format your codes with `black` formatter.
   - And you want to perform linting too with `flake8`.
   - Then, you have to put these texts into `.pre-commit-config.yaml` file.

```yaml
repos:
  # black - Format python scripts
  - repo: https://github.com/psf/black-pre-commit-mirror
    rev: 23.9.1
    hooks:
      - id: black
        language_version: python3.11 # Specify your python version

  # flake8 - Python code linter
  - repo: https://github.com/PyCQA/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
        name: flake8
        types: [python]
        args:
          - --max-line-length=88
          - --ignore=E203,E501,W503
```

4. Run `pre-commit install` to install the **Git hooks**:

> This will take some minutes to install required configs...

```sh
pre-commit install
```

5. Now commit your changes as usual in your repository. The pre-commit hooks will run automatically before the commit is created.

6. **For Testing**: If you want to test the `pre-commit` you can do it by running below command. But first you need to **add all your changes to the staging area** with `git add .` command.  
   Because this will read only those files which are present at staging area of your repository.

```sh
pre-commit run
```

7. Finally, if `pre-commit` get some issue in your code while committing then it will print those in your console right away. And then you can fix them manually and commit those fixes into the repository.

> 📄 If you want more information about **`pre-commit`** read [this blog](https://dev.to/techishdeep/maximize-your-python-efficiency-with-pre-commit-a-complete-but-concise-guide-39a5).

## 🧑‍🏫 Learn `Makefile`

Check this [Makefile](Makefile) which I copied and configured for my own purpose.

This is a amazing yet confusing (for the beginners) way to automate and to improve your experience regarding repetitive tasks. You have to just define many sequential command in the find and assign a good name to it and then run `make awesome-name` as command in your terminal and boom you get all your work done in a go.

> Copied from [this blog](https://dev.to/mmphego/why-you-should-add-makefile-into-your-python-project-20j2).
