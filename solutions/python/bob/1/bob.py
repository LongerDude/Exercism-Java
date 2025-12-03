def response(text):
    New_text = text.strip()

    # 1) Silence
    if not New_text:
        return "Fine. Be that way!"

    # 2) Question (possibly shouted question)
    is_question = New_text.endswith('?')
    has_letters  = any(c.isalpha() for c in New_text)
    is_shout     = has_letters and New_text.upper() == New_text

    if is_question:
        if is_shout:
            return "Calm down, I know what I'm doing!"
        else:
            return "Sure."

    # 3) Shouting (non‑question)
    if is_shout:
        return "Whoa, chill out!"

    # 4) Everything else
    return "Whatever."
