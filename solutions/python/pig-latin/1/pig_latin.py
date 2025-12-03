def translate(text):
    vowels = "aeiou"
    special_vowel_start = ("xr", "yt")

    def convert_word(w):
        # --- 1) Strip off any leading/trailing non‑alphanumerics ---
        prefix, suffix = "", ""
        core = w
        while core and not core[0].isalnum():
            prefix += core[0]
            core = core[1:]
        while core and not core[-1].isalnum():
            suffix = core[-1] + suffix
            core = core[:-1]
        if not core:
            return w  # punctuation‑only

        # --- 2) Remember capitalization ---
        was_cap = core[0].isupper()

        # Work in lowercase for logic
        lower = core.lower()

        # --- 3) Pig Latin logic ---
        if lower.startswith(special_vowel_start) or lower[0] in vowels:
            pig = lower + "ay"
        else:
            # handle “qu” clusters
            if lower.startswith("qu"):
                idx = 2
            elif len(lower) > 2 and lower[1:3] == "qu":
                idx = 3
            else:
                # consonant cluster until first vowel or ‘y’ after pos 0
                idx = 0
                while idx < len(lower) and not (
                    lower[idx] in vowels or (lower[idx] == "y" and idx > 0)
                ):
                    idx += 1
            pig = lower[idx:] + lower[:idx] + "ay"

        # --- 4) Restore capitalization if needed ---
        if was_cap:
            pig = pig.capitalize()

        # --- 5) Reattach punctuation and return ---
        return prefix + pig + suffix

    return " ".join(convert_word(word) for word in text.split())
