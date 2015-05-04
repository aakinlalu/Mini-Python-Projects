"""
File management
---------------
The goal of this exercise is to practice manipulating your file system:
creating folders and files, moving them around, and erasing them.

One piece of information to know about is that each python script contains its
own namespace. Such that, when in a script you define a = 1, a gets added to
the script namespace. But there are other variables that are added to that
namespace automatically: One example is __file__, which contains the filepath
to the current script.

1. Print the path to the current file/script and its containing folder.

2. In the same directory as this exercise, create a new directory called
`analysis`.

Hints: Why it isn't enough to just run:
>>> os.mkdir("analysis")
Where would that folder be? Build its absolute path to create it. Also note
that if the folder already exists, mkdir will raise an error if the folder
doesn't get removed before being created again. To remove a folder, compare the
following functions: `shutil.rmtree` and `os.rmdir`.

3. Create, wherever you are, a set of files with the names and content
described in the dictionary `contents` provided to you. Then, move all these
files into the `analysis` folder. For this, the `copy` function of the module
`shutil` will be useful.

4. Print the absolute path of all the Python `.py` files in this `analysis`
directory.

Hint: Using IPython's ? to remind yourself of what exactly os.path.splitext
returns.

Bonus
~~~~~
Turn your script into a function that takes an arbitrary directory path
and returns a list of Python files. Use it on the newly created analysis
folder.

Bonus Bonus
~~~~~~~~~~~
Let's do the same with a nice function of the os module: use os.walk to find
all Python files contained in all subdirectories of the folder containing this
current script. Again, test it on the analysis folder you created.
"""

import os
import shutil

contents = {
    'data.csv': 'Date,High,Low,Close\n'
                '4-Apr-2014,124,105,111\n'
                '5-Apr-2014,132,125,130\n'
                '6-Apr-2014,112,95,95\n'
                '7-Apr-2014,124,105,110\n',
    'script1.py': 'def bar(x):\n'
              '        print x\n',
    'script2.py': 'def foo(x):\n'
              '        print x*x\n',
    'readme.txt': 'This folder contains the data files scrapped off the web\n'
                  'from financial websites in csv formar as well as python\n'
                  'scripts for analyzing them.\n',
}

# 1. Print the path to the current file/script and its containing folder.
print "This file is located at:", __file__
current_script_container = os.path.dirname(__file__)
print "This script is located inside the folder:", current_script_container

# 2. In the same directory as this exercise, create a new directory called
# `analysis`.
# If we were just running os.mkdir("analysis"), we would get what we want if
# and only if the python session's current working directory was the folder
# of the current script. That isn't necessarily the case (depends where python
# was started, and/or if you used ipython's cd commands to take it to the right
# place). Let's see where we are:
print "Current working directory:", os.getcwd()

# Let's create the folder that we want independently of where our session is by
# building its absolute path. That is the concatenation of this script's
# location and "analysis".
target_folder = os.path.join(current_script_container, "analysis")
# We can't create a folder that already exists
if os.path.exists(target_folder):
    # The folder already exists, let's remove it first. To remove a folder, the
    # easiest is shutil.rmtree since os.rmdir requires for the folder to be
    # empty.
    shutil.rmtree(target_folder)
os.mkdir(target_folder)

# 3. Create, wherever you are, a set of files with the names and content
# described in the dictionary `contents` provided to you. Then, move all these
# files into the `analysis` folder.

# Let's loop over the dictionary grabbing the keys (filenames) and the values
# (content of the file) and create the file with it.
for file_name, content in contents.items():
    with open(file_name, "w") as f:
        f.write(content)

# Let's now move them to the folder we just created (and bonus points for those
# of you who remembered to clean up the local files):
for file_name in contents.keys():
    # file_name here refers necessarily to the local copy we just created.
    shutil.copy(file_name, target_folder)
    os.remove(file_name)

# 4. Print the absolute path of all the Python `.py` files in this `analysis`
# directory.
# Let's look at the content of the folder we created. listdir returns only the
# name of the files, so their full path must be created.
for file_name in os.listdir(target_folder):
    # Extract the file extension.
    ext = os.path.splitext(file_name)[1]
    if ext == '.py':
        # We are explicitly calling the abspath function to make sure we get
        # the absolute path below even though that isn't necessary since
        # target_folder is already an absolute path.
        print os.path.abspath(os.path.join(target_folder, file_name))


# Bonus
# This pretty much requires to indent the previous answer and add a function
# name above: the only difference is that we need to build a list of files to
# return rather than just printing the paths.
def search_python_files(folder_name):
    """ Providing a folder, return a list of the python files found inside.
    """
    py_files = []
    for file_name in os.listdir(target_folder):
        ext = os.path.splitext(file_name)[1]
        if ext == '.py':
            py_files.append(os.path.abspath(os.path.join(target_folder,
                                                         file_name)))
    return py_files

print "Function test:", search_python_files(target_folder)

# Bonus Bonus
# Reminder: os.walk returns a generator which yields the path of each subfolder
# of the provided path, its subfolders, and the files it contains.
for folder, subfolders, files in os.walk(target_folder):
    print "{} contains the following folders: {}".format(folder, subfolders)
    py_files = [filename for filename in files
                if os.path.splitext(filename)[1] == ".py"]
    print "{} contains the following python files: {}".format(folder, py_files)
