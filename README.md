# PORTFOLIO

My portfolio website

## Version

1.0

## Installation prerequisities

* A Unix OS

* Python with `pip` : `sudo apt-get install python-pip`

* The virtual environment manager for python `virtualenv`. Installed by default with the latest verions of python, but available, if it is not already installed, using your favorite package manager, as `python-virtualenv` or via` pip`.

  `sudo apt-get install python-virtualenv` or `sudo pip install virtualenv`

## Installation

Create a new folder dedicated to the portfolio. We will call it `project_portfolio` below.

Unpack the archive project in a subfolder `portfolio` or clone the project repository (private for now): `git clone https://github.com/Mascarpone/portfolio.git`.

In order not to install the required modules directly on your system, and do not depend on the current configuration of it, we will create a virtual environment with `virtualenv`. Therefore, use the following command: `virtualenv venv`.

So we now have an environment in the `venv` folder. To launch it, use the command: `. venv/bin/activate` (do not forget the only point at first).

To ensure the proper activation of the virtual environment, ensure the prompt has been changed and now begins with `(venv)`. For example `(venv)user@machine:~/project_portfolio`.

We can now install all dependencies in the virtual environment: `pip install -r portfolio/requirements.txt` (it is possible that administrator rights are required for this).

Then start the server: `python portfolio/app.py` (Use Ctrl + C to quit).

The Portfolio site is now available at http://localhost:8000.

To exit the virtual environment, use the command `deactivate`.

## Some references

http://flask.pocoo.org/docs/0.10/quickstart/

http://jinja.pocoo.org/docs/dev/templates/

http://www.cheat-sheets.org/saved-copy/git-cheat-sheet.pdf

https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-16-04