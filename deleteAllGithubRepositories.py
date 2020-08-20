# pip3 install pygithub
from github import Github

user = Github(input()).get_user()
for repo in user.get_repos():
    repo.delete()