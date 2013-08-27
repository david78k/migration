alias showdstat="pgrep -fl dstat"
alias psdstat="pgrep -fl dstat"
alias killdstat="pgrep -fl dstat| awk '{print $1}' | xargs kill -9"
alias pskernel='ps -ef | grep kernel'
alias pf='ps -ef | grep '

alias checkstatus='ps -ef | grep exp; ps -ef | grep qemu; ps -ef |grep kernel; ps -ef |grep dstat; netstat -tunlp | grep 5555; ps -ef |grep 5555'
