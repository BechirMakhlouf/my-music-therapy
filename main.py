#!/usr/bin/python3

modele_delta_questions = [
    {
        "question": "As-tu récemment eu des rêves qui t'ont semblé effrayants ou dérangeants ? oui/nonAs-tu récemment eu des rêves qui t'ont semblé effrayants ou dérangeants ?",
        "reponses": ["oui", "non"],
    },
    {
        "question": "est-ce que tu as des cauchemars qui ont un impact sur ta vie quotidienne?",
        "reponses": ["oui", "non"],
    },
]
modele_beta_questions = [
    {
        "question": "Y a-t-il des moments particuliers de la journée où tu te sens plus concentré(e) ou moins concentré(e) ?",
        "reponses": ["oui", "non"],
    },
    {
        "question": "Penses-tu que la qualité de ton sommeil influence ta vigilance pendant la journée ?",
        "reponses": ["oui", "non"],
    },
    {
        "question": "As-tu des stratégies spécifiques pour gérer le stress qui ont un effet positif sur ta concentration ?",
        "reponses": ["oui", "non"],
    },
]
modele_theta_questions = [
    {
        "question": " Y a-t-il des émotions spécifiques que tu ressens fréquemment ces derniers temps ? ",
        "reponses": ["oui", "non"],
    },
    {
        "question": " Comment réagis-tu face aux situations stressantes ou difficiles?",
        "reponses": ["oui", "non"],
    },
]

themes = [
    {
        "theme": "une phase de sommeil plus profonde",
        "questions": modele_delta_questions,
    },
    {
        "theme": "La concentration et la vigilance",
        "question": modele_beta_questions,
    },
    {
        "theme": "améliorer la méditation, la créativité",
        "questions": modele_theta_questions,
    },
]

reponse1 = input()
