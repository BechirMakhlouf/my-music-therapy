#!./bin/python3

from models import *
from methods import *
from pysine import *

if __name__ == "__main__":
    choix = choisirTheme(themes)
    duree = questionner(themes[choix]["questions"])
    # sine(frequency=440.0, duration=1.0)
    print(duree)