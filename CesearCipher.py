def main():
	def foo(text,shift):
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		message = ""
		for alpha in text:
			if alpha not in alphabet:
				message += alpha
				continue
			n = alphabet.index(alpha)
			if n+shift > 25:
				message += alphabet[n+shift-26]
				continue
			message += alphabet[n+shift]
		return message
		


	text = input("input text: ").lower()
	shift = int(input("input shift: "))
	if shift == 0:
		return text
	return foo(text,shift)

if __name__ == "__main__":
	print(main())
