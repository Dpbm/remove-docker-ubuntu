[ ![docker](https://www.docker.com/wp-content/uploads/2022/01/Docker-Logo-White-RGB_Horizontal-730x189-1.png.webp) ](https://www.docker.com/)

# Remove [Docker](https://www.docker.com/) from [Ubuntu](https://ubuntu.com/) based distros

## Remove all dependencies and remaining files from docker

<br />
<br />

To `run` use:

```bash
chmod +x remove-docker.py
sudo ./remove-docker.py

or 

sudo python3 remove-docker.py
```

`SUDO` is needed, without superuser access we can't remove some files and docker configs

<br />
<br />


## Explanations

* This script will not remove plugins and files from vim, oh-my-zsh, compose, and other files created by user, unless if these files are in any target directories.

* Be Careful, use this script if you know what are you doing, maybe it can break other stuffs that you might want to use


<br />
<br />


### Made with 🥰 by [Dpbm](https://github.com/Dpbm)
