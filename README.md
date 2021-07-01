# Portfolio

My portfolio website.
It describes my education, skills, career and inspirations.


## Installation prerequisities

 * A Unix OS
 * Python with `pip` : `sudo apt-get install python-pip`


## Installation

Install all dependencies with `pip install -r requirements.txt`.

The Portfolio webapp can run as a server with `python app.py` (Use Ctrl + C to quit). It is then available at http://localhost:8000.

Otherwise, it can be generated as a static website with `python static.py`. I use this way to publish it on GitHub Pages.

## Data

My portfolio is very personal but one can use the template with his own data.

All the displayed data comes from the *bdd.yaml* file at the root of the repository.


## Some references

This website is using awesome community tools: [Flask](http://flask.pocoo.org/docs/0.10/quickstart/), [Jinja](http://jinja.pocoo.org/docs/dev/templates/) and [Bootstrap](https://getbootstrap.com/docs/3.4/getting-started/).
