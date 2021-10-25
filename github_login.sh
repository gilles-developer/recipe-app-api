
# run with 'source ./github_login.sh'
eval `ssh-agent -s`
ssh-add ~/.ssh/github_key
ssh -T git@github.com