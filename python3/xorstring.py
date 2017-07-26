from base64 import b16decode, b16encode
def xor_strings(string1, string2):
    return bytes(map(lambda x,y: x^y, string1, string2))

def xor_hexstrings(hexstring1, hexstring2):
    return b16encode(xor_strings(b16decode(hexstring1),b16decode(hexstring2)))
