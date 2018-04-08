# The original version is saved in .bash_profile.pysave

export PATH="/usr/local/bin:/usr/local/sbin:/usr/sbin:/sbin:/Library/Frameworks/Python.framework/Versions/3.6/bin:$PATH"

# Add git branch to prompts
parse_git_branch() {
     git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
source ~/.git-prompt.sh
source ~/.git-completion.bash

export PS1="\D{%F %T}\n\[\033[1;32m\]\u\[\033[1;32m\]@\[\033[1;32m\]\h\[\033[1;32m\] \[\033[32m\]\w\[\033[35m\]\$(parse_git_branch)\[\033[00m\] $"

#source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenv
echo ${VIRTUAL_ENV:+[`basename $VIRTUAL_ENV`]}
#someenv

export PROJECT_HOME=~/projects
export WORKON_HOME=~/.virtualenvs
source /Library/Frameworks/Python.framework/Versions/3.6/bin/virtualenvwrapper.sh