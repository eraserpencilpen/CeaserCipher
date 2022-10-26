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
		for i in range(1,101):
			print(foo(text,i))
		for j in range(-101):
			print(foo(text,j))
	print(foo(text,shift))

if __name__ == "__main__":
	main()