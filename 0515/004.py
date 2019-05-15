plain_text = "Love will find a way."
plain_text = "암호문을 만들어 봅시다."

encrypted_text = ""

def caesar(text, offset=1):
    enc = ""
    for c in text:
        enc += chr(offset+ord(c))
    return enc

print(caesar(plain_text))