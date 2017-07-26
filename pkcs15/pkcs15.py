from hashlib import md5, sha1, sha256,sha384, sha512
HASH_ASN1 = {
            'MD5': b'\x30\x20\x30\x0c\x06\x08\x2a\x86'
            b'\x48\x86\xf7\x0d\x02\x05\x05\x00\x04\x10',
            'SHA-1': b'\x30\x21\x30\x09\x06\x05\x2b\x0e'
            b'\x03\x02\x1a\x05\x00\x04\x14',
            'SHA-256': b'\x30\x31\x30\x0d\x06\x09\x60\x86'
            b'\x48\x01\x65\x03\x04\x02\x01\x05\x00\x04\x20',
            'SHA-384': b'\x30\x41\x30\x0d\x06\x09\x60\x86'
            b'\x48\x01\x65\x03\x04\x02\x02\x05\x00\x04\x30',
            'SHA-512': b'\x30\x51\x30\x0d\x06\x09\x60\x86'
            b'\x48\x01\x65\x03\x04\x02\x03\x05\x00\x04\x40',
}

HASH_FUNCTION = {
            'MD5': md5,
            'SHA-1': sha1,
            'SHA-256': sha256,
            'SHA-384': sha384,
            'SHA-512': sha512
}

def pkcs15pad(message, hashchoice, bitlength):
    assert bitlength > 256 and bitlength % 256 == 0
    digest = HASH_FUNCTION[hashchoice](message).digest()
    bytelength = bitlength >> 3
    flength = bytelength - 3 - len(digest) - len(HASH_ASN1[hashchoice])
    return b'\x00\x01'+b'\xff'*flength+b'\x00'+HASH_ASN1[hashchoice]+digest
