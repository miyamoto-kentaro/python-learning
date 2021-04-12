init git -> create .git file
$ git init

you put file on stage
# git add <dir_name>
$ git add .

save github name email
git config --global user.email "your@email"
git config --global user.name "user name"

save file changes
$ git commit -m <your_message>

save git remote repo
$ git remote add origin <remote_repo_url>

push file to remote
$ git push <remote_name> <branch_name>
$ git push origin <branch_name>

