def clean_line(phrase):
    from string import punctuation
    punctuation = punctuation.replace("-", "")

    phrase = phrase.lower()

    for c in punctuation:
        phrase = phrase.replace(c, "")

    return phrase