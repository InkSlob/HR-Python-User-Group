# Python, Analytics, & Baseball

This instruction file is to help one conduct the tutorial referenced below.  The tutorial does not cover how to setup your computer, how to install the packages needed, or how to record your work to GitHub.  I will try to guide you through that part.

### What is the tutorial about?

The tutorial describes itself as follows:

>The Python programming language is a great option for data science and predictive analytics, as it comes equipped with multiple packages which cover most of your data analysis needs. For machine learning in Python, Scikit-learn (sklearn) is a great option and is built on NumPy, SciPy, and Matplotlib (N-dimensional arrays, scientific computing, and data visualization respectively).

In this tutorial, you’ll see how you can easily load in data from a database with sqlite3, how you can explore your data and improve its data quality with pandas and matplotlib, and how you can then use the Scikit-Learn package to extract some valid insights out of your data.  

It is assumed you have Python intalled on your computer, but if not go to [Anaconda Install Webpage](https://docs.continuum.io/anaconda/install). We will use a virtual environment to ensure that you always have the proper Python environment to execute the analysis.  

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

To create a virtual environment navigate to the directory (folder) that you want to program in.  This virtual environment will be specific to this project.  **The directory (folder) needs to be the directory (folder) that you linked to your GitHub repository.**   

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


### Activate Virtual Environment

If your virtual environment is not activated run the following command.  If it is running skip this step.

```$ source venv/bin/activate```

### Python Package Installation

Because you are using Anaconda your Python environment should include all the packages you need for this tutorial.

For more details on what packages are included in your Anaconda Python environment check out their webpage explaining packages.  [Anaconda Packages](https://docs.continuum.io/anaconda/pkg-docs)

## Incorporating GitHub

You want to record your work and share it with others, so we will use GitHub.  

### I have GitHub but no Repository

Follow the following guidance provided by Github on this, email me if you have issues with this. It has been my experience that Git is very challenging.  [GitHub Guide](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)

For now just do step 4.  

```$ git init```

We will do the rest of this guide on GitHub after we complete the tutorial.

## The Tutorial

For this tutorial we are using [Datacamp](https://www.datacamp.com/community/tutorials/scikit-learn-tutorial-baseball-1#gs.null) it is a python tutorial that uses sci-kit learn (Python package) and MLB data.  The data used is from [Sean Lahman Website](http://www.seanlahman.com/baseball-archive/statistics/).  

### Part 1: Predicting MLB Team Wins per Season

This is a good tutorial and much of the code is explained online.  Type the code into your program and run locally.  You will be tempted to copy and paste the code, but do not do this.  You will learn much more actually typing it in and reading it to see where you missed a detail.

### Tutorial Complete, Now What?

Congrats, you finished the tutorial.  That is great!  Now go back to the GitHub committing to a repo guide and push you code.
[In case you forgot it is here](https://help.github.com/articles/adding-an-existing-project-to-github-using-the-command-line/)
