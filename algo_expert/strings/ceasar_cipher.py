import string

def caesarCipherEncryptor(text, key):
    lower_cases = string.ascii_uppercase
    upper_cases = string.ascii_lowercase
    enc = ""
    for ch in text:
        if ch in lower_cases:
            new_idx = (lower_cases.index(ch) + key) % 26
            enc += lower_cases[new_idx]
        elif ch in upper_cases:
            new_idx = (upper_cases.index(ch) + key) % 26
            enc += upper_cases[new_idx]            
        else:
            enc += ch
    return enc