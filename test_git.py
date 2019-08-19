def push(repo_dir):
    import os
    from git import Repo

    # set working directory
    os.chdir("XXX")

    #repo_dir = 'Pantone'
    repo = Repo(repo_dir)
    file_list = [
        "index.html",
        "Data/colors.csv"
    ]
    commit_message = 'Adding new color'
    repo.index.add(file_list)
    repo.index.commit(commit_message)
    origin = repo.remote('origin')
    origin.push()


PATH = "./"
HTTPS_REMOTE_URL = "https://7c934514291d56c69f5c8d969129fb434fc2107b:x-oauth-basic@github.com/ralfg/ralfg.github.io"
COMMIT_MESSAGE = 'Update moFF documentation'


import git
from git import Repo

def git_push_all(path, message):
    #try:
    repo = Repo(path)
    repo.git.add(all=True)
    repo.index.commit(message)
    origin = repo.remote(name='origin')
    origin.push()
    #except:
    #    print('Some error occured while pushing the code')


#git.Git("test_repo/").clone(HTTPS_REMOTE_URL)

#git.Git("./").fetch(HTTPS_REMOTE_URL)

git_push_all(PATH, COMMIT_MESSAGE)
#git.Git("./").add(A=True)
#
# 
# git.Git("./").index.commit(COMMIT_MESSAGE)
#origin = 
#it.Git("./").push(HTTPS_REMOTE_URL)

