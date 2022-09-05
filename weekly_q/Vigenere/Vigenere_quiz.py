def vigenere(msg: str, key: str, method: bool = True) -> str:
    mode = (int(method) * 2 - 1) * (-1)
    rep_key_word = rep_key(msg,key)
    print(rep_key_word)
    ascii_key = [key_enumerate(a)  for a in list(rep_key_word)]
    new_msg = [chr((ord(a) + b * mode -65)%26 + 65) if ord(a) > 64 and ord(a) < 91 else chr((ord(a) + b * mode-97)%26 + 97) if ord(a) > 95 and ord(a) < 123  else a for a, b in zip(list(msg), ascii_key)]
    return ''.join(new_msg)

def rep_key(msg, key):
    key_word = key
    while len(msg) > len(key_word):
        key_word += key_word
    return key_word[:len(msg)]

def key_enumerate(a):
    if ord(a) > 64 and ord(a) < 91:
        num = ord(a) - 65
    elif ord(a) > 96 and ord(a) < 123:
        num = ord(a) - 97
    else: pass
    return num


print(vigenere("Attack at Dawn", "lemon", False))


# True: Encrypt
# False: Decrypt
