import random

def weight_random(word_key):
    """
    Selects a random key from a dictionary using weights.
    """
    words = list(word_key.keys())
    weights = list(word_key.values())

    return random.choices(words, weights=weights, k=1)[0]



def generate_sentence(data_words):

    subjects = data_words["subjects"]
    verbs = data_words["verbs"]
    complements = data_words["complements"]

    subject = weight_random(subjects)
    verb = weight_random(verbs)
    complement = weight_random(complements)

    templates =[
        "{subject} {verb} {complement}.",
        "Un día, {subject} {verb} {complement}.",
        "De repente, {subject} {verb} {complement}."
    ]

    template = random.choice(templates)

    sentence = template.format(
        subject=subject,
        verb=verb,
        complement=complement
    )
    return sentence.capitalize()