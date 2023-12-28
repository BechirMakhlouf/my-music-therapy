#!/usr/bin/python3

from models import *
from methods import *

if __name__ == '__main__':
    choix = choisirTheme(themes)
    duree = questionner(themes[choix]["questions"])
    print(duree)
