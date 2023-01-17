# Getting Started with Python and GitHub
In this project, you will:
- Demonstrate that you have installed the correct software necessary for this course
- Show that you can download starter files from GitHub and upload finished code when you are done
- Demonstrate that you have configured a working development environment for writing code
- Show that you understand the directory structure of your Operating System  (OS)
- Understand the relationship of a command line interface (CLI) with your Operating System (OS)
- Evaluate a simple program to fix errors and pass all required tests 

[comment]: <> (The final step asks you to write a menu application to demonstrate that you can understand user input, Java mathematical statements, and control flow.)

## Step 1 - Create a GitHub account
Go to the [GitHub website](https://github.com) and create an account. They have [student packs](https://education.github.com/pack) that give you access to many things that would otherwise be very expensive, so I recommend you sign up using your `american.edu` email address. You can associate a GitHub account with multiple email addresses.

## Step 2 - Get git
1. Visit the Git [website](https://git-scm.com/downloads) and download the latest Git release for your operating system.
2. Install it, using default settings.
3. As a reference for how to use git, I suggest [Coding Domain](http://codingdomain.com/git/), as it avoids some of the more complicated theory behind git and focuses on the bare minimum practicalities. There are also many good videos, but we will go over some basics in class.

**Deliverable:** Modify the responses.md file so that your name and newly obtained GitHub profile name replaces the text that says *REPLACE_THIS*.

## Step 2.5 - Become familiar with the CLI for your OS

Each Operating System (OS) has at least one primary interface for navigating the system through the command line. These are powerful applications, and allow you to install programs and software libraries or run the programs that you will develop in this course. Every developer should have at least a rudimentary knowledge of how to use the command line application on your system. There are fairly decent introductory videos for how to use the command line options. Many of the commands for both systems are the same (e.g., `cd`, `cat`, `ls`, `python`) but there will be some differences in presentation and overall capability. At this point, you do not need to become a master of your CLI, but a working knowledge of the basic commands is essential. A general overview and history of CLIs can be found in [Keyboards & Command Line Interfaces: Crash Course Computer Science #22](https://www.youtube.com/watch?v=4RPtJ9UyHS0&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=24).

- On macOS, this application is called **Terminal**. [Absolute BEGINNER Guide to the macOS Terminal
  ](https://www.youtube.com/watch?v=aKRYQsKR46I)
- On Windows, this application is called **Powershell**. [Basic Powershell Commands For Beginners](https://www.youtube.com/watch?v=j9wtAezZ9x0). Windows also has the Command Prompt, which is simpler but a bit less powerful. It also shares fewer commands with the terminal on macOS/Linux. But, if the Powershell interface proves overwhelming, it's always an option. I recommend learning one of them well, but you do not need to know both (especially at this point) [Windows Command Line Tutorial - 1 - Introduction to the Command Prompt](https://www.youtube.com/watch?v=MBBWVgE0ewk). 

> Note, understanding how a CLI work relies on you first understanding files and the file system of a desktop computer. If you are unfamiliar with how the file system of your OS operates, you may want to back up and check out some information on file formats and organization. I recommend Crash Course, such as this excellent video on [Files & File Systems: Crash Course Computer Science #20](https://www.youtube.com/watch?v=KN8YgJnShPM&list=PL8dPuuaLjXtNlUrzyH5r6jN9ulIgZBpdo&index=21).
 
**Deliverable:** Modify the responses.md file and answer the questions about your CLI.

## Step 3 - Demonstrate you have Python installed. 
Python is an active and evolving language - new versions are released frequently. This course uses the most recent version of Python 3.x. You can easily obtain [Python](https://www.python.org/downloads/) all by itself, or install it as part of a larger collection of useful modules. One of the most popular is [Anaconda](https://www.anaconda.com/products/distribution), which includes a massive assortment of libraries that can be useful for data science but takes up a lot of space on your computer.

Whatever you do, **do not** install a version of Python 2.x for this course. There are huge differences between them, and none of the examples in class or in the book(s) will line up with 2.x. Assignments will also not be accepted if they are submitted using 2.x syntax.

Typing `python --version` into your CLI verifies that you have done this successfully. Here is correct output for an older version that was popular around 2002: 

```terminal 
Python 2.2.2
```

**Deliverable:** Modify the responses.md to the output from when you type `python --version` into your CLI.

## Step 4 - Download and install an IDE
As we discussed in class, you should download and install a powerful IDE or text editor. An IDE will make it easier to perform many coding tasks, but they are more complex applications, and it will be more challenging to become familiar with all the features. There is also a risk that developing all your code in an IDE may make it more challenging to learn the details of writing code on your own - many automated processes that will not always be available exams or technical interviews.

#### IDE

In this course, you will utilize an Integrated Development Environment (IDE) to write code. While many IDEs exist, examples and in-class support videos will utilize [PyCharm by Jetbrains](https://www.jetbrains.com/). It is freely available to students through an academic license and supports all the software development features that we will use in this course. It is not sufficient to develop your code in this course through the command line or through an online notebook environment (e.g., Jupyter).

**Deliverable:** In this directory, save a screenshot image (e.g., a .jpeg or .png file) showing your installed IDE or text editor open. If you do not know how to take a screenshot on your computer, then learn how from the PCMag article ["How to Take a Screenshot on Any Device"](https://www.pcmag.com/news/how-to-take-a-screenshot-on-any-device). Then modify the responses.md file to indicate which IDE you are using.

## Step 5 - Clone your Repo locally

Because you can see these instructions, that means that you have already followed the link and accepted the assignment. GitHub classroom has automatically created a repository for you on GitHub and imported the starting code into it. You may be reading this in a browser tab or on your phone. For the next steps, you will move this project onto your computer so that you can write and edit code in your IDE. 
1. On this page, there is a big button labeled Code. If you click it, you get the web URL for this online repo.
2. Open PyCharm. Click `Git > Clone` in the menu. 
3. In the window that pops up, paste the URL from the **Code** button in the box labelled **URL**.
4. Press the Clone button. The project will be created in the projects directory on your computer. You might then be asked if you want to open to project. Go ahead and take a look!

## Step 6 - Correct Errors

### Syntax Errors

You should also see a simple - but definitely broken - program in the `/src` directory. How do you know it's broken? Well, a couple of ways. _Syntax errors_ should stand out due to the red underline in your code editor window. Placing the mouse pointer over the error should give you some insight into what is wrong with the code and potentially how to fix it. Using your existing knowledge of the language, correct the syntax errors. 

### Logic Errors

Your code compiles, but how can you be sure that it does what it is supposed to be doing? We use **test cases**. These test cases provide instant feedback that your system runs appropriately and provides the right output for a given input. These tests are included in the test directory, and they follow a pretty straightforward pattern. Each file tests a different method in the starter program, and contains multiple static methods to test the program in a different way. A test method is declared as void, then it sets up a simple version of the problem you are asked to solve. In the example below, the test runs the `addTwoNumbers` method in the `HelloWorld` class and checks that the program does in fact return 2. It does that using `assertEquals`, which is a special _unit test_ command for testing that the results of a method are what we believe they should be. 

Tests can be run by right-clicking the test file and selecting `Run` from the popup menu. Alternatively, you can run all test at once by right-clicking on the test directory and clicking `Run All Tests` from the popup menu. Once you have corrected all the syntax errors, you will have left some logic errors in the code - methods are not returning what is expected. If you run all tests, many tests are failing, and the IDE will tell you what was expected and what was actually returned from the method called in each test.

Throughout this class the starter code that you are given in assignments will contain many test files. As you build the code, the test will give you feedback on whether your solution is logically correct or not. In some projects, you will also experiment with creating test cases of your own, but for now **do not alter** the files in the test directory. 

You will know that you are done fixing syntax and logic errors when all tests pass successfully.

> The testing component of this project is far easier to accomplish using an IDE like the suggested PyCharm. While it is possible to get the tests running without it, it is not recommended and neither the TA nor the Instructors will necessarily be able to help you if you use an alternative method. 

**Deliverable:** All tests pass.

## Step 7 - Update your local repo and push to GitHub

Once you have the code where you want it, correcting as many logical and syntax errors as you can, you need to submit it back to us for grading through GitHub. The easiest way to do this is directly through PyCharm. 

1. On the menu bar of icons next to the `run` command is a green check mark. Clicking this icon initiates a `commit`. A window will pop up. Enter a meaningful comment in the text box to indicate your progress so far. These are useful for us to understand what's working and what's not. Once you have a good message, click the `commit` button on the bottom. After a commit, you have effectively saved a local backup. Commit as many changes as you want - these are useful in case you really mess something up and need to go back to a working version of the code (we will discuss later in class how to restore these backups). But, your instructor does not have access to these commits until you `push` them.
2. Next to the check mark is a green arrow that points up and to the right. Click this to initiate a `push`. Another window will pop up, asking if you want to push any/all commits that you have made but have not yet pushed. For this project, this will be pretty simple - just click `push`. This will push committed changes from your local repository back to GitHub. Now your instructor and TA can see them.

Alternatively, you can commit and push your changes directly through the CLI. Regardless of the method, you will need to become familiar with a very common cycle of making changes to your local repository then pushing those changes back to GitHub where your instructor can review them and assign grades. Each time you make changes to your files, you will save them through your text editor (either through File->Save or Ctrl+S). This saves a copy of the changes you have made to your system, but have not saved them to your local repository or made them available online to us.

1. `git add .` This command will stage the changes you have made to the local repository and add any new files to the repo.
2. `git commit -m replace_with_commit_message_in_quotes` This will commit staged changes to your local repository. Make sure to change the _commit_message_ to some meaningful reminder about the changes you have made.
3. `git push` This will push committed changes from your local repository back to GitHub. Now your instructor and TA can see them.

You should get used to using these commands frequently. Much of the challenge of developing complex software is learning to read error messages and feedback from the command line. If you type the command `git status` the command line will print out the current status of the repo. This will usually give you a clue for what you need to do next.

**Deliverable:** The corrected project pushed to the online repo.

# Deliverables and Grading
Please refer to the learning management system (LMS) for the assignment grading rubric. 

# Getting Stuck
There are times when you might get stuck on some part of an assignment. It happens to the best of us. If you need assistance on a specific part of your code, then be sure to try to `commit` AND `push` the most recent version of your files to GitHub. It makes it much easier for your instructor and TA to provide specific feedback on individual lines of code in the files that you submit. 
