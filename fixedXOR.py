import codecs

def xord_byte_strings(str1, str2):
    decode_1 = codecs.decode(str1, 'hex')
    decode_2 = codecs.decode(str2, 'hex')
    xord_bytes = b''
    for b1, b2 in zip(decode_1, decode_2):
        xord_bytes += bytes([b1 ^ b2])
    xord = codecs.encode(xord_bytes, 'hex').decode()
    return xord

def main():
    str1 = '1c0111001f010100061a024b53535009181c'
    str2 = '686974207468652062756c6c277320657965'
    print(xord_byte_strings(str1, str2))

if __name__ == '__main__':
    main()
