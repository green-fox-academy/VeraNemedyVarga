# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    from builtins import ascii
    content = open(file_name, 'r')
    read_content = content.read()

    decrypted = ""
    for letter in read_content:
        if letter == " ":
            decrypted += " "
        elif letter == '\n':
            decrypted += "\n"
        elif letter == "\t":
            decrypted += ""
        else:
            numify = ord(letter)
            numify -= 1
            textify = chr(numify)
            decrypted += textify

    wfile = open("solution.txt", 'w')
    wfile.write(decrypted)
    wfile.close()
    content.close()

    return decrypted

print(decrypt("encoded_lines.txt"))

"""encoded = "Cfbvujgvm jt cfuufs uibo vhmz/ Fyqmjdju jt cfuufs uibo jnqmjdju/"
decrypted = ""
for letter in encoded:
    if letter == " ":
        decrypted += " "
    numify = ord(letter)
    numify -= 1
    textify = chr(numify)
    decrypted += textify
print(decrypted)"""


#char index asciiban i = i + 1 legyen.
