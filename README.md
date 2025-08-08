The task 2 is about Create a To-Do list application (Console-Based)
The program is a console-based To-Do list manager

1. File Handling ---> Reading file and writing file
                          ---> Persistent storage : Tasks are kept in tasks.txt even after the program ends.

2. Lists ---> Store tasks in memory 
    tasks = [ ]
    tasks.append(task)
    tasks.pop(index)
    Lists allow adding / removing / viewing tasks easily

3. String Manipulation :
    ---> Strip() : Removes unwanted spaces / newlines from input and file data.
    ---> Concatenation (+) : Adds \n when writing to file
    ---> f - strings : Formats Output :
    print (f" {index} . {task}")
