#!./bin/python3

import random
from pysine import sine
from models import themes
from methods import choisirTheme, questionner, jouerFrequence

if __name__ == "__main__":
    choix = choisirTheme(themes)
    theme = themes[choix]
    frequence = random.uniform(theme["frequence_range"][0], theme["frequence_range"][1])
    duree = questionner(theme["questions"])
    jouerFrequence(frequence=frequence, duree=duree)