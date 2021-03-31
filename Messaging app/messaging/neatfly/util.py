import hashlib
import random

def hash(name):
    name = bytes(name, 'utf-8')
    allowed = [
        'sha224',
        'sha256',
        'sha384',
        'sha3_224',
        'sha3_256',
        'sha3_384',
        'sha3_512',
        'sha512'
    ]
    num = random.randint(0, 7)
    _ = getattr(hashlib,allowed[num])
    return _(name).hexdigest())