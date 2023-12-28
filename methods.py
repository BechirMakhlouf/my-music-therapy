from typing import Dict, List

def choisirTheme(themes) -> int:
    print("---------------------|MENU|---------------------")
    for i in range(len(themes)):
        print(f'{i + 1}-  {themes[i]["theme"]}')
        pass

    choix: int = 0
    while True:
        print("- Donner votre choix mon ami: ")
        choix = int(input())
        if choix in range(1, len(themes) + 1):
            break
    return choix - 1


def questionner(questionsList: List) -> int:
    duree: int = 30
    for questionDict in questionsList:
        question: str = questionDict["question"]
        reponses: List[float] = questionDict["reponses"]

        print(question)
        while True:
            result = 0
            for i in range(len(reponses)):
                print(f"{i + 1}: {reponses[i]}")
            result = int(input())
            if result in range(1, len(reponses) + 1):
                if result == 1:
                    duree += 30
                    pass
                break
        pass
    return duree

