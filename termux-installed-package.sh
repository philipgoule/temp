# generate installed package list
dpkg --get-selections | cut -f1 > mypackages.txt
