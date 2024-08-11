A simple python script to help manage notes and tasks.  
The note manager will function as a simple command line interface.  
The note manager expects "vim" and "notepad" apps are available in the env path.  
  
The only future additions foreseen would be a schedulder cli.  
  
The notes can be managed in an editor vim or notepad. The task list will be
managed in a separate formatted text file, with the intent that you mainly
interface via the command line, but with an option to open the file and manage
holistically (so format should be user friendly, but manual editing requires
the rules of formatting to be followed).  
  
The application is fairly simple and will be defined simply by its commands.  
You only have to be aware of three terms.  
- (n)otebook - a folder that contains the text files (tasks and papers)  
- (p)aper - a text file that contains the information being noted  
  - the user formats into sections as needed (cli just opens files for editing)  
  - task - a task list mode to create, read, update, delete, and complete tasks  
    - you move into Task Context from Notebook Context or paper commands  
  
The command list is below, the command line expections are different based on context.  
  
# Context Anywhere  
notebook : pulls you back to root context, closes current notebook if open  
(n)otebook (l)ist : list all the notebooks  
(n)otebook (c)reate [notebook name] : creates a new notebook (or folder)  
(n)otebook (o)pen [notebook name or index] : opens the context to given notebook  
(p)aper (l)ist [notebook name] : lists all text files in notebook  
(p)aper (c)reate [notebook name] [paper name] : creates an empty file in the notebook  
(p)aper (o)pen [notebook name] [paper name] : opens text file in notepad  
(p)aper (e)dit [notebook name] [paper name] : opens text file in vim ("vi" is alternative)  
(p)aper (j)ournal [notebook name] [paper name] : opens journal file in vim, log date added  
(p)aper (m)ore [notebook name] [paper name] : writes the paper to the screen  
(p)aper (a)rtifacts [notebook name] [paper name] : creates folder (if not exists) in relation to notebook paper and opens windows explorer  
(p)aper (t)asklist [notebook name] [task list name] : opens task list in task mode  
(cls) : clears the screen  
(f)older : opens windows explorer folder (root or within notebook, depends on context)  
(q)uit : quits the program (or quits notebook/task list if in notebook/task context)  
(h)elp : clears the screen then dumps this readme.txt file to the user screen  
  
# Context Root (no notebook is opened)  
Same "notebook" commands found in "Context Anywhere", just remove "notebook" from command line  
  
# Context Notebook (notebook is opened)  
Same "paper" commands in "Context Anywhere", just remove "paper" from command line and don't pass the notebook name, since it is part of context already.  
  
Also, you can pass index in a number of cases for reference of paper or tasklist instead of name.  
  
# Context Task (task list is opened - task lists are found within a specific notebook)  
(l)ist : lists the tasks in the task list (index list for most commands)  
(c)reate "<your task details>" : creates a new task  
(u)pdate [index] : provides an update, a new note to append to task  
(d)elete [index] : deletes the task   
(v)iew [index] : provides a view of the task and all its updates (notes)  
(r)esolved [index] : completes task, archives to a done file  
(t)ransfer [index or "all"] [tasklistname]: transfers task (or all tasks) to another task list (advanced)  
(m)anual : opens the task file in vim to allow manual updates  
(q)uit : quits the task list  
