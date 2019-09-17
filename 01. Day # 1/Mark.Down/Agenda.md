![programmimngDays](http://programmingdays.com/img/62c218d0-fda7-4dd2-b49f-8628130c4c8f.png "programmingDays")

# python workshop : Day 1

Table Of Contents

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=6 orderedList=false} -->

<!-- code_chunk_output -->

- [python workshop : Day 1](#python-workshop--day-1)
  - [Why this workshop?](#why-this-workshop)
  - [Modern day programming languages and Python](#modern-day-programming-languages-and-python)
    - [Development of Python over time](#development-of-python-over-time)
  - [Installing Python and running Programs](#installing-python-and-running-programs)
    - [Windows](#windows)
      - [Step 1: Download the Python 3 Installer](#step-1-download-the-python-3-installer)
      - [Step 2: Run the Installer](#step-2-run-the-installer)
    - [Linux (Ubuntu only)](#linux-ubuntu-only)
    - [macOS / Mac OS X](#macos--mac-os-x)
      - [Step 1: Install Homebrew (Part 1)](#step-1-install-homebrew-part-1)
      - [Step 2: Install Homebrew (Part 2)](#step-2-install-homebrew-part-2)
      - [Step 3: Install Python](#step-3-install-python)
    - [Online Python Interpreters](#online-python-interpreters)
    - [Using Python Interpreter](#using-python-interpreter)
      - [Executing Python Code](#executing-python-code)
      - [Exiting the Interpreter](#exiting-the-interpreter)
    - [Interacting with Python through an IDE](#interacting-with-python-through-an-ide)
      - [Start a New Python Program](#start-a-new-python-program)
      - [Running Python Code](#running-python-code)
  - [Variable, literal, operators and expressions.​](#variable-literal-operators-and-expressions%e2%80%8b)
  - [Debugging a Python program.​](#debugging-a-python-program%e2%80%8b)

<!-- /code_chunk_output -->

Hello &#x1F44B;

Welcome to a (not so boring 😆) workshop in Python. lets ove forward 👇


## Why this workshop?

Any computer programming workshop is basically more or less a problem solving exercise. This time we will discuss why we need to have another Python workshop. Few reasons to have a Python workshop are as follows:-

1. Easy nature of Python.

```C++
#include <iostream>
#include <cstdlib>
using namespace std;

int main ( int argc, char ** argv[]){
    std::cout<< "Hello World";
    return EXIT_SUCCESS;
}
```
compared to

```python
print ("Hello World")
```

2. Web development and Computer Graphics

    - The usability of Python for Web development can be understood from following projects:-
        - Youtube
        - DropBox
        - Google Search
    - The usability of Python in Computer graphics can be understood from following projects and libraries:-
        - PyGame
        - KTinker
        - Blackhole image generation.
        - Bokeh
        - Matplotlib

3.  Data Science and Machine Learning

     As it is quite easy to learn and work with Python is a natural choice for the data scientist and the machine learning engineers. Some of the popular Data Science and Machine Learning libraries are:-

    - NumPy
    - Theano
    - Keras
    - PyTorch
    - SciPy
    - Pandas
    - scikit-learn

If you have read upto here you can check _quite a big list_ of [success stories](https://www.python.org/about/success/) of projects done using Python.

## Modern day programming languages and Python

To understand why and how Python stood, where it is now we need to delve a bit into the history of Python. The points below discuss timeline of Python.

### Development of Python over time

- Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands 🇳🇱.
![Guido Van Rossum](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png)

- Python 2.0 was released on 16 October 2000 with many major new features, including a cycle-detecting garbage collector and support for Unicode.

- Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible.



## Installing Python and running Programs
In this section we will discuss how we can download and install python in following operating systems i.e.:-
- Windows.
- macOS.
- Linux.

### Windows
It is highly unlikely that your Windows system shipped with Python already installed. Windows systems typically do not.

#### Step 1: Download the Python 3 Installer
1. Open a browser window and navigate to the [Download page for Windows](https://www.python.org/downloads/windows/) at python.org.
2. Underneath the heading at the top that says **Python Releases for Windows**, click on the link for the **Latest Python 3 Release - Python 3.x.x**.
3. Scroll to the bottom and select either **Windows x86-64 executable installer** for 64-bit or **Windows x86 executable installer** for 32-bit.

#### Step 2: Run the Installer

Once you have chosen and downloaded an installer, simply run it by double-clicking on the downloaded file. A dialog should appear that looks something like this:

![Installer](https://files.realpython.com/media/win-install-dialog.40e3ded144b0.png)


Then just click Install Now. That should be all there is to it. A few minutes later you should have a **working Python 3 installation on your system**.

### Linux (Ubuntu only)

- **Ubuntu 17.10, Ubuntu 18.04 (and above)** come with Python 3.6 by default. You should be able to invoke it with the command **`python3`**.

- **Ubuntu 16.10 and 17.04** do not come with Python 3.6 by default, but it is in the Universe repository. You should be able to install it with the following commands:

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

You can then invoke it with the command python3.6.

- If you are using Ubuntu 14.04 or 16.04, Python 3.6 is not in the Universe repository, and you need to get it from a Personal Package Archive (PPA). For example, to install Python from the “deadsnakes” PPA, do the following:

```bash
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt-get update
$ sudo apt-get install python3.6
```

### macOS / Mac OS X
While current versions of macOS (previously known as “Mac OS X”) include a version of Python 2, this tutorial series uses Python 3, so let’s get you upgraded to that.

The best way we found to install Python 3 on macOS is through the [Homebrew package manager](https://brew.sh/).

#### Step 1: Install Homebrew (Part 1)

To get started, you first want to install Homebrew:

1. Open a browser and navigate to http://brew.sh/. After the page has finished loading, select the Homebrew bootstrap code under “Install Homebrew”. Then hit `Cmd+C` to copy it to the clipboard. Make sure you’ve captured the text of the complete command because otherwise the installation will fail.

2. Now you need to open a Terminal.app window, paste the Homebrew bootstrap code, and then hit Enter. This will begin the Homebrew installation.

3. If you’re doing this on a fresh install of macOS, you may get a pop up alert asking you to install Apple’s **“command line developer tools”**. You’ll need those to continue with the installation, so please confirm the dialog box by clicking on “Install”.

#### Step 2: Install Homebrew (Part 2)
You can continue installing Homebrew and then Python after the command line developer tools installation is complete:

1. Confirm the “The software was installed” dialog from the developer tools installer.
Back in the terminal, hit `Enter` to continue with the Homebrew installation.
2. Homebrew asks you to enter your password so it can finalize the installation. **Enter your user account password and hit Enter to continue**.
3. Depending on your internet connection, Homebrew will take a few minutes to download its required files. Once the installation is complete, you’ll end up back at the command prompt in your terminal window.

#### Step 3: Install Python
Once Homebrew has finished installing, **return to your terminal and run the following command**:

```bash
brew install python3
```
This will download and install the latest version of Python.

### Online Python Interpreters

Without installing Python on your machine, there are several web sites available where you can interact with a Python interpreter online:

- Python.org Online Console: www.python.org/shell
- Python Fiddle: pythonfiddle.com
- Repl.it: repl.it
- Trinket: trinket.io
- Python Anywhere: www.pythonanywhere.com

### Using Python Interpreter

In a GUI desktop environment, it is likely that the installation process placed an icon on the desktop or an item in the desktop menu system that starts Python.

For example, in Windows, there will likely be a program group in the Start menu labeled Python 3.x, and under it a menu item labeled Python 3.x (32-bit), or something similar depending on the particular installation you chose.

Clicking on that item will start the Python interpreter:
![Python Interpreter](https://files.realpython.com/media/python-interpreter-window.24c17cb2fd60.png)

Alternatively, you can open a terminal window and run the interpreter from the command line. How you go about opening a terminal window varies depending on which operating system you’re using:

- In Windows, it is called **Command Prompt**.
- In macOS or Linux, it should be called **Terminal**.
Using your operating system’s search function to search for “command” in Windows or “terminal” in macOS or Linux should find it.

Once a terminal window is open, if paths have been set up properly by the Python install process, you should be able to just type python. Then, you should see a response from the Python interpreter.

```bash
C:\Users\proDays>python
Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```
If you are not seeing the >>> prompt, then you are not talking to the Python interpreter. This could be because Python is either not installed or not in your terminal window session’s path. It’s also possible that you just haven’t found the correct command to execute it.

#### Executing Python Code

If you are seeing the prompt, you’re off and running! The next step is to execute the statement that displays Hello, World! to the console:

1. Ensure that the >>> prompt is displayed, and the cursor is positioned after it.
2. Type the command print("Hello, World!") exactly as shown.
3. Press the Enter key.

The interpreter’s response should appear on the next line. You can tell it is console output because the >>> prompt is absent:

```python
>>> print("Hello World!")
Hello World!
```

Did something go wrong? Perhaps you made one of these mistakes:

You forgot to enclose the string to be printed in quotation marks:

```python
>>> print(Hello, World!)
  File "<stdin>", line 1
    print(Hello, World!)
                      ^
SyntaxError: invalid syntax
```

You remembered the opening quotation mark but forgot the closing one:

```python
>>> print("Hello, World!)
  File "<stdin>", line 1
    print("Hello, World!)
                        ^
SyntaxError: EOL while scanning string literal
```

You used different opening and closing quotation marks:

```python
>>> print("Hello, World!')
  File "<stdin>", line 1
    print("Hello, World!')
                         ^
SyntaxError: EOL while scanning string literal
```

You forgot the parentheses:

```python
>>> print "Hello, World!"
  File "<stdin>", line 1
    print "Hello, World!"
                        ^
SyntaxError: Missing parentheses in call to 'print'
```

You entered extra whitespace characters before the command:

```python
>>>     print("Hello, World!")
  File "<stdin>", line 1
    print("Hello, World!")
    ^
IndentationError: unexpected indent
```

#### Exiting the Interpreter

When you are finished interacting with the interpreter, you can exit a REPL session in several ways:

Type exit() and press Enter:

```python
>>> exit()
C:\Users\proDays>
```

In Windows, type Ctrl+Z and press Enter:

```python
>>> ^Z
C:\Users\proDays>
```
In Linux or macOS, type Ctrl+D. The interpreter terminates immediately; pressing Enter is not needed.

If all else fails, you can simply close the interpreter window. This isn’t the best way, but it will get the job done.

### Interacting with Python through an IDE
An Integrated Development Environment (IDE) is an application that more or less combines all the functionality you have seen so far. IDEs usually provide REPL capability as well as an editor with which you can create and modify code to then submit to the interpreter for execution.

You may also find cool features such as:

- Syntax highlighting: IDEs often colorize different syntax elements in the code to make it easier to read.
- Context-sensitive help: Advanced IDEs can display related information from the Python documentation or even suggested fixes for common types of code errors.
- Code-completion: Some IDEs can complete partially typed pieces of code (like function names) for you—a great time-saver and convenience feature.
- Debugging: A debugger allows you to run code step-by-step and inspect program data as you go. This is invaluable when you are trying to determine why a program is behaving improperly, as will inevitably happen.

The IDE we are discussing here is **Visual Studio Code**

ne of the coolest code editors available to programmers, [Visual Studio Code](https://code.visualstudio.com/docs), is an open-source, extensible, light-weight editor available on all platforms. It’s these qualities that make Visual Studio Code from Microsoft very popular, and a great platform for Python development.

**In this article, you’ll learn about Python development in Visual Studio Code, including how to:**

- Install Visual Studio Code
- Discover and install extensions that make Python development easy
- Write a simple Python application
- Learn how to run and debug existing Python programs in VS Code

Installing Visual Studio Code is [very accessible](https://code.visualstudio.com/docs/setup/setup-overview) on any platform. Full instructions for Windows, Mac, and Linux are available, and the editor is updated monthly with new features and bug fixes. You can find everything at the [Visual Studio Code website](https://code.visualstudio.com/):

![Visual Studio Code](https://files.realpython.com/media/vscode-website.491c40d9d828.png)

Visual Studio Code has built-in support for multiple languages and an extension model with a rich ecosystem of support for others. VS Code is updated monthly, and you can keep up to date at the [Microsoft Python blog](http://aka.ms/pythonblog).

![Visual Studio Code Home](https://files.realpython.com/media/vscode-welcome-screen.c64afd719b3e.png)

VS Code supports development in multiple programming languages through a well-documented extension model. The Python extension enables Python development in Visual Studio Code, with the following features:

- Support for Python 3.4 and higher, as well as Python 2.7
- Code completion with IntelliSense
- Linting
- Debugging support
- Code snippets
- Unit testing support
- Automatic use of conda and virtual environments
- Code editing in Jupyter environments and Jupyter Notebooks

![Python Extension](https://files.realpython.com/media/python-extension-webpage.d2a7d3b6d636.png)

#### Start a New Python Program

Let’s start our exploration of Python development in Visual Studio Code with a new Python program. In VS Code, type `Ctrl+N` to open a new File. (You can also select File, New from the menu.)

> Note: The Visual Studio Code UI provides the Command Palette, from which you can search and execute any command without leaving the keyboard. Open the Command Palette using Ctrl+Shift+P, type File: New File, and hit Enter to open a new file.

No matter how you get there, you should see a VS Code window that looks similar to the following:

![Visual Studio Window](https://files.realpython.com/media/vscode-new-file.39cc7b9e485d.png)

For our test code, let’s quickly code up `Hello World`. Begin typing the following code in the new tab you just opened:

```python
print("Hello World")
```
![Visual Studio Window](https://files.realpython.com/media/vscode-new-file.39cc7b9e485d.png)

Wait, what’s going on? Why isn’t Visual Studio Code doing any keyword highlighting, any auto-formatting, or anything really helpful? What gives?

The answer is that, right now, VS Code doesn’t know what kind of file it’s dealing with. The buffer is called Untitled-1, and if you look in the lower right corner of the window, you’ll see the words Plain Text.

To activate the Python extension, save the file (by selecting File, Save from the menu, File:Save File from the Command Palette, or just using Ctrl+S) as hello.py. VS Code will see the .py extension and correctly interpret the file as Python code. Now your window should look like this:

![Visual Studio Code home screen](https://files.realpython.com/media/vscode-formatted-code.312b8d79fbe7.png)

That’s much better! VS Code automatically reformats the file as Python, which you can verify by inspecting the language mode in the lower left corner.

If you have multiple Python installations (like Python 2.7, Python 3.x, or Anaconda), you can change which Python interpreter VS Code uses by clicking the language mode indicator, or selecting Python: Select Interpreter from the Command Palette. VS Code supports formatting using pep8 by default, but you can select black or yapf if you wish.

#### Running Python Code

Now that the code is complete, you can run it. There is no need to leave the editor to do this: Visual Studio Code can run this program directly in the editor. Save the file (using Ctrl+S), then right-click in the editor window and select Run Python File in Terminal:

![Running the Python source file](https://files.realpython.com/media/vscode-run-python-file.d6a0255cd190.gif)

## Variable, literal, operators and expressions.​

## Debugging a Python program.​
