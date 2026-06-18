def is_wake_word(text):

    if not text:
        return False

    text = text.lower().strip()

    wake_words = [
        "hey friday",
        "hi friday",
        "hello friday",
        "friday"
    ]

    return any(word in text for word in wake_words)