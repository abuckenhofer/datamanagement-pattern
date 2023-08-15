The repository holds a pattern for a data management project with Python.

# How to setup a Python environment?

Download and install a Python version. It is highly recommended to work with virtual environments. Each virtual environment contains a Python version and specific packages. A great overview of Python virtual environments is in Martin Breuss' [article](https://realpython.com/python-virtual-environments-a-primer/).

```
$ <path to Python version>/python -m venv <path to virtual environment>
```

<path to virtual environment> can be the root of the Python project, e.g. datamanagement-pattern.

When the virtual environment is created, the virtual environment can be activated or deactivated:
```
<venv>/bin/activate
<venv>/bin/deactivate
```

When the virtual environment is active, Python packages can be installed as usual, e.g. navigate to datamanagement-pattern and run:
```
$ pip install --upgrade pip
$ pip install -r requirements.txt
```
