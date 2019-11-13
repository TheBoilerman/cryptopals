import requests
import pprint

# returns the XOR'd byte list of byte_string and an integer byte_int
def single_byte_check(byte_string, byte_int):
    blist = b''
    for b in byte_string:
        blist += bytes([b ^ byte_int])
    return blist

# scores each byte in input_bytes, then returns the sum of the scores
def engl_check(input_bytes):
    # frequencies of each letter in the English language
    char_frequencies = {
        'a' : 0.08167, 'b' : 0.01492, 'c' : 0.02782, 'd' : 0.04253,
        'e' : 0.12702, 'f' : 0.02228, 'g' : 0.02015, 'h' : 0.06094,
        'i' : 0.06966, 'j' : 0.00153, 'k' : 0.00772, 'l' : 0.04025,
        'm' : 0.02406, 'n' : 0.06749, 'o' : 0.07507, 'p' : 0.01929,
        'q' : 0.00095, 'r' : 0.05987, 's' : 0.06327, 't' : 0.09056,
        'u' : 0.02758, 'v' : 0.00978, 'w' : 0.02360, 'x' : 0.00150,
        'y' : 0.01974, 'z' : 0.00074, ' ' : 0.13000
    }
    scores = []
    # for each byte in the input byte_string...
    for byte in input_bytes.lower():
        val = char_frequencies.get(chr(byte), 0)
        scores.append(val)
    return sum(scores)


def decrypt(input_string):
    byte_string = bytes.fromhex(input_string)
    scores_dict = dict()
    for i in range(256):
        x = single_byte_check(byte_string, i)
        val = engl_check(x)
        scores_dict[i] = val

    # finds the key with the greatest score (most likely to be English)
    greatest = 0
    ans = 0
    for key in scores_dict:
        if scores_dict[key] > greatest:
            greatest = scores_dict[key]
            ans = key
        else:
            continue

    
    return greatest, ans

def main():
    # get the text from the website, strip it at the newline
    url = 'https://cryptopals.com/static/challenge-data/4.txt'
    data = requests.get(url).text
    lines = data.rsplit()


    for line in lines:
        x, y = decrypt(line)
        print(x, y)


if __name__ == '__main__':
    main()
