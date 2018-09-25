# install packages
xargs -0 apt install -y < <(tr \\n \\0 < mypackages.txt)
