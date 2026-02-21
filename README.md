# practise_1

sudo apt update, sudp apt install -y git, git --version (to check version)

git init    -  initializes a new git repo in the cwd. starts tracking the folder

(one time setup for name, email) - used to set or verify the identity when making commits, --global means applies to all repos in the system

git config --global user.name "<name>"    -  to set name for the git commit

git config --global user.email "<mailid>"    -  to set email address for commits

git config --global --list      - displays all global git configuration settings

git status      -    displays current state of the working directory and staging area (modified - if a file changes, changes to be committed - after staging area, untracked - if new file is created, to know if working tree is clean)

git add <file>      -   stages spacified files for the next commit

git add .      -    stages all untracked files for the commit

git commit -m"commits"    -  saves a checkpoint

git remote add origin <repo-url>    -  to connect your local git repo to the remote repository.so, it is like "When I push or pull using origin, go to this URL"

git remote set-url origin <repo-url>    -  to update the remote repository for the origin

git remote -v    -  shows the remote repositories configured for your local repo

git push -u origin <branch>    -  to push the local commits/changes to specified branch on the remote repository

git branch      -  lists all specified branches (branch - a copy to try changes safely

git branch branchname    -  creates a new branch  

git switch branchname    -  to switch to a new branch

git checkout -b branchname    -  creates and switches to the new branch

git switch main      -    to switch to another branch

git merge <branch_name>    -  to merge the data from specified branch to current branch(main)

git clone <repo-url>      -  copies a remote repo to your local machine

git restore --staged <file>    -  unstages a file from the next commit

git log      -   shows all saved versions

git log --oneline    -  show all saved versions in oneline

git diff    -  to see what changed, means show changes between versions

git log --oneline --decorate    -  show all versions (history)

git show <commit_id>:<file_name>    -  this shows the file as it was in that version

git checkout <commit_id>    -  to go back to an older version ( we can see only that version lines/files exist. we can also go to latest version of files (git checkout <latest_commit_id>). jump to an old time state

git restore --source <commit_id> file_path    - to restore old version of file (permanent restore). bring old content back


<h4>Stashing</h4>

git stash    -  temporarily saves uncommitted changes to work on something else

git stash list    -  lists all stashed changes

git stash apply    -  reapplies the most recent stash without removing it

git stash pop    -  reapplies the most recent stash and removes it from the stash list



