import requests

url = 'https://cryptopals.com/static/challenge-data/6.txt'
lines = requests.get(url).text.rsplit()

def hamming(bstr1, bstr2):
	diff = 0
	
	bytes_1 = [byte for byte in bstr1]
	bytes_2 = [byte for byte in bstr2]
	xor_bytes = [b1 ^ b2 for b1, b2 in zip(bytes_1, bytes_2)]
	for byte in xor_bytes:
		diff += sum([1 for bit in bin(byte) if bit == '1'])
	return diff


str1 = b'this is a test'
str2 = b'wokka wokka!!!'
x = hamming(str1, str2)
print(x)