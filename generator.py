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

def generate_story(data):
    subject = weight_random(data["subjects"])
    verb = weight_random(data["verbs"])
    complement = weight_random(data["complements"])

    # sentence_1 = f"{subject} encontró {complement}.".capitalize()
    # sentence_2 = f"Luego {subject} {verb} aquel secreto."
    # sentence_3 = f"Y ahí fue cuando descubrió algo que lo impresiono."

    # sentences = [sentence_1, sentence_2, sentence_3]

    # Beginning of the story
    pool_beginning = [
        f"Mientras caminaba, {subject} vio {complement}.",
        f"Un día {subject} encontró {complement}."
    ]

    # Possible intermediate events
    pool_development = [
        f"Por eso {subject} intentó {verb}.",
        f"Entonces {subject} decidió {verb}.",
        f"{complement} es algo que {subject} tiene que proteger.",
        f"Sin pensarlo, {subject} comenzó a {verb}."
    ]
    
    # The end
    pool_end = [
        "Y ahí fue cuando descubrió algo impresionante.",
        f"Desde entonces {subject} no volvió a ser igual."
    ]

    sentences = []

    # Choose start
    sentences.append(random.choice(pool_beginning))

    # Choose middle
    options_middle = random.randint(2, 3)
    choose_middle = random.sample(pool_development, k=options_middle)

    for i in choose_middle:
        sentences.append(i)

    # Choose end
    sentences.append(random.choice(pool_end))

    return sentences