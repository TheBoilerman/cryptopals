import requests
from textwrap import wrap

def hamming(str1, str2):
	# make a list of the individual bytes in each input byte string
	bstr1 = str1.encode()
	bstr2 = str2.encode()

	bytes_1 = [byte for byte in bstr1]
	bytes_2 = [byte for byte in bstr2]

	# make a list of xor'd value for each byte pair in the two lists of bytes
	xor_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]

	# get the difference in the bits
	diff = 0
	for byte in xor_bytes:
		diff += sum([1 for bit in bin(byte) if bit == '1'])
	
	return diff


str1 = b'this is a test'
str2 = b'wokka wokka!!!'
x = hamming(str1, str2)
print(x)

'''
Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes, 
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key. 
You could proceed perhaps with the smallest 2-3 KEYSIZE values. 
Or take 4 KEYSIZE blocks instead of 2 and average the distances.
'''
cypher = 'HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS'
KEYSIZE = 2

# break up the cypher string into chunks of size == KEYSIZE into list called chunks
chunks = [cypher[i:i+KEYSIZE] for i in range(0, len(cypher), KEYSIZE)]
print(chunks)

x = hamming(chunks[0], chunks[1])
print(x)


url = 'https://cryptopals.com/static/challenge-data/6.txt'
lines = requests.get(url).text.rsplit()