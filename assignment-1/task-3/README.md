# Virtualenv in Python

Virtual environment are essential because they keep the packages local to our project instead of installing system-wide which will cause trouble when running other project with same packages but different versions.

This is accomplished by creating a new folder for our site packages to store and use that package when we run our project and also a local python.exe file to run the python source code.

### Installing virtualenv in Python 

We can install virtualenv in python by using pip

```
pip install --user virtualenv
```

Here , I have used `--user` flag to install the package only to my user profile.

### Creating a virtual environment using virtualenv 

To create a virtual environment , run :

```
virtualenv env_name
```

### Activating the virtual environment

To activate the virtual environment, run :

```
.\env_name\Scripts\activate
```

This will create a python virtual environment of the same version as the virtualenv 

---

