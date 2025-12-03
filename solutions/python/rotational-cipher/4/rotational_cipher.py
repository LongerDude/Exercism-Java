import string


def rotate(text, key):
    """Encode text using Rotation Cipher."""
    plain = string.ascii_lowercase
    cipher = "".join((plain[key:], plain[:key]))
    mytable = str.maketrans(plain + plain.upper(), cipher + cipher.upper())
    return text.translate(mytable)