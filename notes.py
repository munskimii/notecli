#
# Author:  Michael Monschke
#
# Description:  Just a simple command line interface to provide a notebook type capability - editors being notepad and vim
#

import os
import subprocess as sp
import tempfile
import time

from pathlib import Path

class Task:
    def __init__(this, desc):
        this._desc = desc
        this._notes = []
        time.ctime()
        this._date = time.strftime('%b %d, %Y')

CTX_ROOT=0
CTX_NOTEBOOK=1
CTX_TSK=2

# default settings before program starts
cmd = ""
ctx = CTX_ROOT
notebook = ""
noteshort = ""
task = ""
taskshort = ""
books = []
papers = []
tasks = []
task_list = []

# creates a notebook if not already exists
def createn(mynote):

    try:
        x = int(mynote)
        print("...the notebook name cannot just be a number...")
        return 0
    except ValueError:
        pass

    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if notedir.exists():
        print("... the notebook already exists ...")
    notedir.mkdir(exist_ok=True)
    return 1

# lists the notebooks - that is folders that start with book.
def listn():
    global books

    os.system("cls")
    print("")
    notes = os.listdir()
    i = 1;
    for note in notes: 
        if (note.startswith("book.")):
            print(str(i) + ") " + note[5:])
            books.append(note)
            i += 1

# opens the notebooks - that is folders that start with book.
def openn(mynote):
    global ctx
    global notebook
    global noteshort
    global task
    global taskshort
    global books
    global papers
    global tasks
    global task_list

    mynotebook = "book." + mynote 

    try:
        idx = int(mynote) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(books)):
            print("...you cannot have notebook with just number as name - or index is out of range...")
            return 

        mynotebook = books[idx]
        mynote = books[idx][5:]
    except ValueError:
        pass

    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
    else:
        ctx = CTX_NOTEBOOK
        notebook = mynotebook
        noteshort = mynote
        task = ""
        taskshort = ""
        papers = []
        tasks = []
        task_list = []
        listp(noteshort)

# lists the pads - that is the text files
def listp(mynote):
    global papers
    global tasks

    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    papers = []
    tasks = []

    os.system("cls")
    print("\nPapers:")
    pads = os.listdir(mynotebook)
    for paper in pads: 
        if (paper.startswith("note.")):
            papers.append(paper)
            print("" + str(len(papers)) + ") " + paper[5:(len(paper)-4)])

    print("\nTasks:")
    for task in pads: 
        if (task.startswith("task.") and not task.endswith(".complete.txt")):
            tasks.append(task)
            print("" + str(len(tasks)) + ") " + task[5:(len(task)-4)])

# creates a pad - that is, an empty text file
def createp(mynote, mypad):

    try:
        x = int(mypad)
        print("...the paper name cannot just be a number...")
        return 
    except ValueError:
        pass

    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    mypadtext = mynotebook + "\\note." + mypad + ".txt"
    padfile = Path(mypadtext)
    if padfile.exists():
        print("... the pad already exists ...")
        return

    with open(padfile, mode='a'): pass

# opens the pads - that is the text files in notepad
def openp(mynote, mypad):
    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    # initial setup unless the index pattern works which will replace this line
    mypadtext = mynotebook + "\\note." + mypad + ".txt"

    try:
        idx = int(mypad) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(papers)):
            print("...you cannot have paper with just number as name - or index is out of range...")
            return 

        mypadtext = mynotebook + "\\" + papers[idx]
    except ValueError:
        pass

    padfile = Path(mypadtext)
    if not padfile.exists():
        createp(mynote, mypad)

    sp.Popen(["notepad.exe", mypadtext])

# edits the pads with vim - that is the text files
def editp(mynote, mypad, mylog=False):
    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    mypadtext = mynotebook + "\\note." + mypad + ".txt"

    try:
        idx = int(mypad) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(papers)):
            print("...you cannot have paper with just number as name - or index is out of range...")
            return 

        mypadtext = mynotebook + "\\" + papers[idx]
    except ValueError:
        pass

    padfile = Path(mypadtext)
    if not padfile.exists():
        createp(mynote, mypad)

    if mylog:
        original_text = ""
        with open(mypadtext, "r") as myfile:
            original_text = myfile.read()
        with open(mypadtext, "w") as myfile:
            time.ctime()
            mydate = time.strftime('%b %d, %Y')
            myfile.write("====  " + mydate + "\n\n\n")
            myfile.write(original_text)

    sp.call(["vim.exe", mypadtext])

# prints the paper to the screen
def morep(mynote, mypad):
    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    mypadtext = mynotebook + "\\note." + mypad + ".txt"

    try:
        idx = int(mypad) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(papers)):
            print("...you cannot have paper with just number as name - or index is out of range...")
            return 

        mypadtext = mynotebook + "\\" + papers[idx]
    except ValueError:
        pass

    padfile = Path(mypadtext)
    if not padfile.exists():
        return

    with open(mypadtext, "r") as myfile:
        print("")
        print(myfile.read())

# creates (if needed) artifacts folder and opens the folder
def artifactsp(mynote, mypad):
    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    mypadfolder = mynotebook + "\\note." + mypad

    try:
        idx = int(mypad) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(papers)):
            print("...you cannot have paper with just number as name - or index is out of range...")
            return 

        mypadfolder = mynotebook + "\\" + papers[idx][0:-4] # removing the ".txt" from the file to get the folder name
    except ValueError:
        pass

    # first check we have a related paper, if not, we shouldn't try to create related artifact folder
    padtextfile = Path(mypadfolder + ".txt")
    if not padtextfile.exists():
        print("...you cannot create artifact folder for non-existant paper...")
        return

    padfolder = Path(mypadfolder)
    if not padfolder.exists():
        padfolder.mkdir(exist_ok=True)

    sp.Popen(["explorer", ".\\" + mypadfolder])


# loads the task file, called upon open and reload after manual
def loadt(tskfile):
    global task_list

    task_list = []

    with open(tskfile, mode='r') as myfile: 
        while True:
            line = myfile.readline()
            if len(line) == 0:
                break
            if line.startswith("==  "):
                mytask = line[4:].split("    ~||")[0]
                mytaskdate = line[4:].split("    ~||")[1][:-3]
                me = Task(mytask)
                me._date = mytaskdate
                task_list.append(me)

                while (True):
                    line = myfile.readline()
                    if (line.startswith("  *  ")): # should be note or empty line to move to the next one
                        me._notes.append(line[5:-1])
                    else:
                        break

# re-writes the tasks to the task file
def writet():
    global task
    global task_list

    with open(task, mode='w') as myfile: 
        for tsk in task_list:
            myfile.write("==  " + tsk._desc + "    ~||" + tsk._date + "||~\n")
            for note in tsk._notes:
                myfile.write("  *  " + note + "\n")
            myfile.write("\n")

# lists the tasks that are pulled into memory
def listt():
    global task_list

    os.system("cls")
    i = 1
    print("")
    for tsk in task_list:
        print(str(i) + ") " + tsk._desc)
        i += 1

# creates the tasks in the task list and re-writes task file
def createt(newtaskdesc):
    global task_list

    me = Task(newtaskdesc)
    task_list.append(me)
    writet()

# updates the tasks in the task list with a note and re-writes task file
def updatet(index, notedesc):
    global task_list

    try:
        idx = int(index) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(task_list)):
            print("...index is out of range...")
            return 

    except ValueError:
        print("...invalid index...")
        return

    task_list[idx]._notes.append(notedesc)
    writet()

# deletes a task in the task list and re-writes task file
def deletet(index):
    global task_list

    try:
        idx = int(index) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(task_list)):
            print("...index is out of range...")
            return 

    except ValueError:
        print("...invalid index...")
        return

    task_list.pop(idx)
    writet()
    listt()

# views a task in the task list with its notes
def viewt(index):
    global task_list

    try:
        idx = int(index) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(task_list)):
            print("...index is out of range...")
            return 

    except ValueError:
        print("...invalid index...")
        return

    tsk = task_list[idx]
    print("")
    print(tsk._desc)
    for note in tsk._notes:
        print("  *  " + note)

# resolves a task in the task list, appends to complete file and deletes from current list
def resolvedt(index):
    global task
    global task_list

    try:
        idx = int(index) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(task_list)):
            print("...index is out of range...")
            return 

    except ValueError:
        print("...invalid index...")
        return

    tsk = task_list.pop(idx)
    writet()
    listt()

    with open(task + ".complete.txt", mode='a') as myfile: 
        time.ctime()
        enddate = time.strftime('%b %d, %Y')
        myfile.write("==  " + tsk._desc + "    ~||" + tsk._date + "||~~||" + enddate + "||~\n")
        for note in tsk._notes:
            myfile.write("  *  " + note + "\n")
        myfile.write("\n")

# edits the pads with vim - that is the text files
def manualt():
    global task

    sp.call(["vim.exe", task])
    loadt(task)
    listt()

# transfers a task in the task list to another task list
def transfert(index, bumplist):
    global task
    global task_list

    bumpfile = notebook + "\\task." + bumplist + ".txt"
    if not Path(bumpfile).exists():
        print("...invalid list to transfer to...")
        return

    if (index == "all"):

        # write to the new file
        with open(bumpfile, mode='a') as myfile: 

            # loop through each task from top and append to the other file, when done, write out current task file again

            while (len(task_list) > 0):
                # bump task from list and list on screen
                tsk = task_list.pop(0)

                myfile.write("==  " + tsk._desc + "    ~||" + tsk._date + "||~\n")
                for note in tsk._notes:
                    myfile.write("  *  " + note + "\n")
                myfile.write("\n")

        # delete from old list by re-writing
        writet()
        listt()

    else:

        try:
            idx = int(index) - 1 # screen shows 1 based indexes when listing
            
            if (idx >= len(task_list)):
                print("...index is out of range...")
                return 

        except ValueError:
            print("...invalid index...")
            return

        # bump task from list and list on screen
        tsk = task_list.pop(idx)
        listt()

        # write to the new file
        with open(bumpfile, mode='a') as myfile: 
            myfile.write("==  " + tsk._desc + "    ~||" + tsk._date + "||~\n")
            for note in tsk._notes:
                myfile.write("  *  " + note + "\n")
            myfile.write("\n")

        # delete from old list by re-writing
        writet()

# opens the task context
def opent(mynote, mytask):
    global ctx
    global notebook
    global noteshort
    global task
    global taskshort

    mynotebook = "book." + mynote 
    notedir = Path(mynotebook)
    if not notedir.is_dir():
        print("... cannot find the notebook...")
        return

    mytaskfile = mynotebook + "\\task." + mytask + ".txt"

    try:
        idx = int(mytask) - 1 # screen shows 1 based indexes when listing
        
        if (idx >= len(tasks)):
            print("...you cannot have tasklist with just number as name - or index is out of range...")
            return 

        mytaskfile = mynotebook + "\\" + tasks[idx]
        mytask = tasks[idx][5:-4]
    except ValueError:
        pass


    tskfile = Path(mytaskfile)
    if not tskfile.exists():
        with open(tskfile, mode='a'): pass
    else:
        loadt(tskfile)

    ctx = CTX_TSK
    notebook = mynotebook
    noteshort = mynote
    task = mytaskfile
    taskshort = mytask

    listt()

def myhelp():
    readme = "readme.txt"

    helpfile = Path(readme)
    if not helpfile.exists():
        return

    os.system("cls")

    with open(readme, "r") as myfile:
        print("")
        print(myfile.read())


os.system("cls")
listn()

# loop going through the command request and executing, will quit with command "quit"
while (not cmd.startswith("q") or ctx != CTX_ROOT):
    
    if (cmd == ""):
        pass
    elif (cmd == "cls"):
        os.system("cls")
    elif (cmd.startswith("h")):
        myhelp()
    elif (cmd.startswith("n")):
        args = cmd.split()
        if (len(args) == 1):
            ctx = CTX_ROOT
            notebook = ""
            noteshort = ""
            task = ""
            taskshort = ""
            books = []
            papers = []
            tasks = []
            task_list = []
            listn()
        elif (len(args) == 3 and args[1].startswith("c")):
            if (createn(args[2]) == 1):
                openn(args[2])
        elif (len(args) == 3 and args[1].startswith("o")):
            openn(args[2])
        elif (len(args) == 2 and args[1].startswith("l")):
            listn()
    elif (cmd.startswith("p")):
        args = cmd.split()
        if (len(args) == 4 and args[1].startswith("c")):
            createp(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("o")):
            openp(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("j")):
            editp(args[2], args[3], True)
        elif (len(args) == 4 and args[1].startswith("e")):
            editp(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("vi")):
            editp(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("m")):
            morep(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("a")):
            artifactsp(args[2], args[3])
        elif (len(args) == 4 and args[1].startswith("t")):
            opent(args[2], args[3])
        elif (len(args) == 3 and args[1].startswith("l")):
            listp(args[2])
    elif (cmd.startswith("f")):
        
        if (len(notebook) > 0):
            sp.Popen(["explorer", ".\\" + notebook])
        else:
            sp.Popen(["explorer", "."])
    elif (ctx == CTX_ROOT):
        args = cmd.split()
        if (len(args) == 2 and args[0].startswith("c")):
            if (createn(args[1]) == 1):
                openn(args[1])
        elif (len(args) == 2 and args[0].startswith("o")):
            openn(args[1])
        elif (len(args) == 1 and args[0].startswith("l")):
            listn()
    elif (ctx == CTX_NOTEBOOK):
        args = cmd.split()
        if (len(args) == 1 and args[0].startswith("q")):
            ctx = CTX_ROOT
            notebook = ""
            noteshort = ""
            task = ""
            taskshort = ""
            books = []
            papers = []
            tasks = []
            task_list = []
            listn()
        elif (len(args) == 2 and args[0].startswith("c")):
            createp(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("o")):
            openp(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("j")):
            editp(noteshort, args[1], True)
        elif (len(args) == 2 and args[0].startswith("e")):
            editp(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("vi")):
            editp(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("m")):
            morep(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("a")):
            artifactsp(noteshort, args[1])
        elif (len(args) == 2 and args[0].startswith("t")):
            opent(noteshort, args[1])
        elif (len(args) == 1 and args[0].startswith("l")):
            listp(noteshort)
    elif (ctx == CTX_TSK):
        args = cmd.split()
        if (len(args) == 1 and args[0].startswith("q")):
            ctx = CTX_NOTEBOOK
            task = ""
            taskshort = ""
            task_list = []
        elif (len(args) == 1 and args[0].startswith("l")):
            listt()
        elif (len(args) > 1 and args[0].startswith("c")):
            createt(" ".join(args[1:]))
        elif (len(args) > 2 and args[0].startswith("u")):
            updatet(args[1], " ".join(args[2:]))
        elif (len(args) == 2 and args[0].startswith("d")):
            deletet(args[1])
        elif (len(args) == 2 and args[0].startswith("v")):
            viewt(args[1])
        elif (len(args) == 2 and args[0].startswith("r")):
            resolvedt(args[1])
        elif (len(args) == 1 and args[0].startswith("m")):
            manualt()
        elif (len(args) == 3 and args[0].startswith("t")):
            transfert(args[1], args[2])

    print("")
    cmd = input(noteshort + "/" + taskshort + ">")
