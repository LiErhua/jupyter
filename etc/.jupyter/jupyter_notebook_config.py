# https://jupyter-notebook.readthedocs.io/en/stable/config.html
from os import environ
from notebook.auth import passwd
_pw = environ.get("PASSWORD")
c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 80
c.NotebookApp.allow_root = True
c.NotebookApp.open_browser = False
c.NotebookApp.password = "ABCabc123*#06#" if _pw is None else passwd(_pw)
c.NotebookApp.token = ""