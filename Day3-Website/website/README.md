# README to help with the usage of the makefile and ther website
---------------

# `config.py`
> file must be present and holds the configuration variables for the website

# `generate_website.py`
> This file handles the actual reading of the config file and population of the website
> This is the main file to run (if needed)
> I don't suggest just running this. Run the makefile

# `webformat.py`
> handles the generation of images, urls, and sections for the websites 
> should never have to run this as it just holds misc functions

## `make`
> this command looks for a file `makefile` within the current directory and tries to run it
> The file is simple, and issues basic `sh` commands

# several options are available
> `make clean` <- cleans up the build/ directory and removes any temp files
> `make` or `make all` or `make refresh` <- all do the same thing. Clean up and then rebuild
> `make regen` <- just regens website without cleaning
> `make backup` <- backs up your current website with a unique name
> `make update` <- repulls the git repo and then tries to regen the website
