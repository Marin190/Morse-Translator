code = {'a' : '.-', 'b' : '-...', 'c' : '-.-.', 'd' : '-..', 'e' : '.', 'f' : '..-.', 'g' : '--.', 'h' : '....', 'i' : '..', 'j' : '.---', 'k' : '-.-', 'l' : '.-..', 'm' : '--', 'n' : '-.', 'o' : '---', 'p' : '.--.', 'q' : '--.-', 'r' : '.-.', 's' : '...', 't' : '-', 'u' : '..-', 'v' : '...-', 'w' : '.--', 'x' : '-..-', 'y' : '-.--', 'z' : '--..', '.' : '.-.-.-', '?' : '..--..', ',' : '--..--', ' ' : '/'}
result = "\n  "
FileText = input("\n  Use File :\n  [1] yes\n  [2] no\n  > ")
choice = input("\n  [1] text to morse\n  [2] morse to text\n  > ")
if choice == "1":
	if FileText == "1":
		file = input("\n  File name : ")
		with open(file, "r") as f:
			text = f.read()
	elif FileText == "2":
		text = input("\n  Text to translate : ")
	for i in range(len(text)): result = f"{result} {code[text[i]]}"
	if FileText == "1":
		with open(f"translate-{file}", "w+") as f:
			f.write(result)
		print(f"  save on translate-{file}")
	elif FileText == "2":
		print(result)
elif choice == "2":
	if FileText == "1":
		file = input("\n  File name : ")
		with open(file, "r") as f:
			text = f.read()
	elif FileText == "2":
		text = input("\n  Morse to translate : ")
	morse = text.split()
	for i in morse:
		for le, co in code.items():
			if co == i: result = f"{result}{le}"
	if FileText == "1":
		with open(f"translate-{file}", "w+") as f:
			f.write(result)
		print(f"  save on translate-{file}")
	elif FileText == "2":
		print(result)
finish = input("\n\n  Press enter to exit >")