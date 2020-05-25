import base64, os

name = input("Enter file: ")
file = os.path.splitext(name)
if file[1].lower() != ".png" or not os.path.exists(name):
	exit("File Not PNG OR File Not found.")

f = open(name, 'rb').read()
n = f.find(base64.b64decode(b"SUVORK5CYII=")) + 8

if n == len(f):
	k = open(file[0] + "-Out" + file[1], "wb")
	k.write(f + input("File Not Modified, Enter text: ").encode("utf-8"))
	k.close()
	print("Success! Result File: \"" + file[0] + "-Out" + file[1] + "\"")
else:
	f = open(name, "rb")
	f.read(n)
	print("Result: " + f.read().decode("utf-8"))
	f.close()
