from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_der_x509_certificate
from cryptography.hazmat.backends.openssl.rsa import _RSAPublicKey
from gzip import GzipFile
from base64 import b64decode

def parseder(derbytes):
    cert = load_der_x509_certificate(derbytes,default_backend())
    key = cert.public_key()
    if isinstance(key,_RSAPublicKey):
        n = key.public_numbers().n
        e = key.public_numbers().e
        return (n,e)
    return None

def parse_cert_tarball(tarball):
    with GzipFile(tarball) as gzfile:
        for line in gzfile:
            hexstring, b64der = str(line,encoding='UTF-8').strip().split(',')
            result = parseder(b64decode(b64der))
            if result is not None:
                n,e = result
