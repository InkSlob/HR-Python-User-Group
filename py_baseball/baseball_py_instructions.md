## Virtual Environment

### Installing Virtual Environment

Do you have a virtual environment on your machine?
Check using your terminal:

```
$ virtualenv --version
```

If you get an error, you will have to install the utility. 

Most Linux distributions provide a package for virtualenv. For example, Ubuntu users can install it with this command:

```
$ sudo apt-get install python-virtualenv
```

If you are using Mac OS X, then you can install virtualenv using easy_install:

```
$ sudo easy_install virtualenv
```

If you are using Microsoft Windows or any operating system that does not provide an official virtualenv package, then you have a slightly more complicated install procedure.

Using your web browser, navigate to https://bitbucket.org/pypa/setuptools, the home of the setuptools installer. In that page, look for a link to download the installer script. This is a script called ez_setup.py. Save this file to a temporary folder on your computer, then run the following commands in that folder:

```
$ python ez_setup.py
$ easy_install virtualenv
```

### Creating a Virtual Environment to Use

To create a virtual environment navigate to the directory (folder) that you want to program in.  This virtual environment will be specific to this project.

```$ virtualenv venv```

where **venv** is the name of the virtual environment you just created.

The output from the command above should look something like this:

```
New python executable in venv/bin/python2.7
Also creating executable in venv/bin/python
Installing setuptools............done.
Installing pip...............done.
```

Now you have a venv folder inside the flasky folder with a brand-new virtual environment that contains a private Python interpreter. To start using the virtual environment, you have to “activate” it. If you are using a bash command line (Linux and Mac OS X users), you can activate the virtual environment with this command:

```$ source venv/bin/activate```

If you are using Microsoft Windows, the activation command is:

```$ venv\Scripts\activate```

When a virtual environment is activated, the location of its Python interpreter is added to the PATH, but this change is not permanent; it affects only your current command session. To remind you that you have activated a virtual environment, the activation command modifies the command prompt to include the name of the environment:

```(venv) $```

When you are done working with the virtual environment and want to return to the global Python interpreter, type deactivate at the command prompt.


## Installing Required Packages in the Virtual Environment

**This assumes you are using the Anaconda platform**

If your virtual environment is not activated run the following command.  If it is running skip this step.

```activate 

