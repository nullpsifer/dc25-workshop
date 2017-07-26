def xor_strings(string1, string2):
    return ''.join(map(lambda x,y: chr(ord(x)^ord(y)),string1,string2))

def xor_hextrings(hextring1, hexstring2):
    return xor_string(hexstring1.decode('hex'), hexstring2.decode('hex')).encode('hex')
