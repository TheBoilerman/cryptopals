import codecs

def hex_to_b64(hex):
    b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
    return b64

hex = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
b64 = hex_to_b64(hex)
print(b64)
