# Environment setup with Virtualenv

Dependencies assumed to be already installed:

- [Python 3]


## Project setup

To install dependencies and setup the project

- [1. Install Python virtualenv](#1-install-python-virtualenv)
- [2. Create virtualenv](#2-create-virtualenv)
- [3. Install Python dependencies](#3-install-python-dependencies)
- [4. Download the test dataset](#4-download-the-test-dataset)


### 1. Install Python virtualenv

```bash
$ pip install virtualenv
```

### 2. Create virtualenv

Create a new virtual env. At the root of this repository:

```bash
$ python3 -m venv ./venv
```

### 3. Install Python dependencies

```bash
# activate virtual env
$ source venv/bin/activate

# first upgrade pip
(venv) $ pip install --upgrade pip

(venv) $ pip install --upgrade -r requirements.txt

# deactivate virtual env
$ deactivate
```

### 4. Download the test dataset

TODO


## Run

Activate virtualenv and run Jupiter Notebook

```bash
$ source venv/bin/activate

(venv) $ jupyter notebook .
```

[Python 3]: https://www.python.org
