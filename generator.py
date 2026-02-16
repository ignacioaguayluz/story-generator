import random

def generate_sentence(subjects, verbs, complements):
    """
    Generates a random sentence using provided word lists.

    Args:
        subjects (list): List of subjects strings.
        verbs (list): List of verbs strings.
        complements (list): List of complement strings.

    Returns:
        str: A generated sentence.

    Raises:
        ValueError: If any of the lists are empty.
    """

    if not subjects or not verbs or not complements:
        raise ValueError("All input lists must contain at least one element.")

    subject = random.choice(subjects)
    verb = random.choice(verbs)
    complement = random.choice(complements)

    sentence = f'{subject} {verb} {complement}.'
    return sentence.capitalize()

