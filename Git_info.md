# Personal Git Cheat Sheet

## What is git 
 - It is an version control system that keeps track of every change you have made and allows you to back to them. 
    - which changes 
    - who made them 
    - when 
    - why 

## Documentation 

https://git-scm.com/docs 

 ## The process to Add a file 

- git add 
- git commit -m "..."
- git push

 ## Important git commands 

 - git status - Show the working tree status
 - git branch - List, create, or delete branches
 - git switch - Switch branches
 - git fetch -  Download objects and refs from another repository
 - git merge - Join two or more development histories together

## Making changes 
- be in the right derectory
- cd <file path>

#### The process 
- git add -- tell what file to add. the '.' will add all files that have been changed. 
- git commit - Record changes to the repository
- git push - Update remote refs along with associated objects

## How to make a branch 
- git branch <name of branch>


## Branching and Merging
- branch 
- merge
- stash -  Stash the changes in a dirty working directory away


## Sharing and Updating projects
- fetch
- pull
- push

## gitignore

#### Purpose 
- lets Git know that it should ignore certain files and not track them.
#### What it is? 
- a file is a plain text file where each line contains a pattern for files/directories to ignore.