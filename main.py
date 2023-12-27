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

modele_gamma_questions = [
    {
        "question": "Penses-tu que ces pauses ont un impact sur ta vigilance ?",
        "reponses": ["oui", "non"],
    },
    {
        "question": "Penses-tu que l'environnement a un impact sur ton niveau d'éveil?",
        "reponses": ["oui", "non"],
    },
    {
        "questions": "Penses-tu que l'engagement dans une tâche spécifique influence ton niveau d'éveil?",
        "reponses": ["oui", "non"],
    },

    {
        "question": "As-tu ressenti de la fatigue ou de la somnolence récemment",
        "reponses": ["oui", "non"],
    },
    {
        "question": "As-tu l'impression d'avoir suffisamment dormi ?",
        "reponses": ["oui", "non"],
    },
    {
        "question": "Suis-tu une routine de sommeil régulière ?",
        "reponses": ["oui", "non"],
    },

]

modele_alpha_questions = [ 
 { "question": "As-tu ressenti une diminution de stress récemment ?", },
 { "question": "Trouves-tu certaines activités particulièrement relaxantes ?", },
 { "question": "Pratiques-tu des techniques de relaxation, comme la méditation ou la respiration profonde ?", },
 { "question": "Penses-tu que ton environnement actuel contribue à la relaxation ?", },
 { "question": "Penses-tu que la qualité de ton sommeil influence ta détente ?", },
 { "question": "Peux-tu identifier des signes physiques qui indiquent que tu es détendu ?"  },
 { "question": "Prends-tu le temps de te détendre dans ta journée ?" }
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
