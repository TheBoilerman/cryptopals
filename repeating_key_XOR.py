def repeating_key_xor(message, key):
	#byte_text = message.encode()
	cypher = b''
	index = 0
	for letter in message:
		cypher += bytes([letter ^ key[index]])
		if (index + 1) == len(key):
			index = 0
		else:
			index += 1
	return cypher

def main():
	text = b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key = b'ICE'
	cypher = repeating_key_xor(text, key)
	print(cypher.hex())

if __name__ == '__main__':
	main()