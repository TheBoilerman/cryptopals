import requests
import pprint
from math import gcd

def hamming(str1, str2):
	# make a list of the individual bytes in each input byte string
	bstr1 = str1.encode('utf-8')
	bstr2 = str2.encode('utf-8')

	bytes_1 = [byte for byte in bstr1]
	bytes_2 = [byte for byte in bstr2]

	# make a list of xor'd value for each byte pair in the two lists of bytes
	xor_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]

	# get the difference in the bits
	diff = 0
	for byte in xor_bytes:
		diff += sum([1 for bit in bin(byte) if bit == '1'])

	return diff

'''
Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.

For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE worth of bytes,
and find the edit distance between them. Normalize this result by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key.
You could proceed perhaps with the smallest 2-3 KEYSIZE values.
Or take 4 KEYSIZE blocks instead of 2 and average the distances.
'''

'''
we read a couple bytes of our ciphertext, then the next two bytes and get the Hamming Distance. 
We can repeat this up to the end of the ciphertext and average all the values together, 
divide by the number of bytes (two initially), that's the "normalization" part. 
We repeat this for three bytes, then four, then five and so on, up to 14 bytes for this string, 
since it's length is 28 bytes and we need to difference two strings of bytes.
'''



cypher = 'HUIfTQsPAh9PE048GmllH0kcDk4TAQsHThsBFkU2AB4BSWQgVB0dQzNTTmVS'
url = 'https://cryptopals.com/static/challenge-data/6.txt'
lines = requests.get(url).text.rsplit()
KEYSIZE = 2

# break up the cypher string into chunks of size == KEYSIZE into list called chunks
data = {}
for KEYSIZE in range(2, int(len(cypher)/2)):
	scores = []
	chunks = [cypher[i:i+KEYSIZE] for i in range(0, len(cypher), KEYSIZE)]
	while True:
		try:
			chunk1 = chunks[0]
			chunk2 = chunks[1]

			score = hamming(chunk1, chunk2)
			scores.append(score)

			del chunks[0]
			del chunks[1]
		except:
			break
	avg_scores = sum(scores)/len(scores)
	norm_scores = avg_scores/KEYSIZE
	data[KEYSIZE] = norm_scores

sort_data = sorted(data.items(), key=lambda x: x[1])
new_list = []
for tup in sort_data:
	if len(new_list) < 5:	
		new_list.append(tup)
	else:
		break
x = new_list[0][1]
y = new_list[1][1]
print(gcd(x,y))

pprint.pprint(sort_data, indent=4)
print(new_list)