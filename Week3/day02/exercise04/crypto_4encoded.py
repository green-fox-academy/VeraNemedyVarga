# Create a method that decrypts texts/encoded_zen_lines.txt
def decrypt(file_name):
    from builtins import ascii
    content = open(file_name, 'r')
    read_content = content.read()
    new_text = ""
    for char in (0, len(read_content)):
        char += 1
        new_text += read_content[char]
    print(new_text)

decrypt(encoded_lines.txt)



#char index asciiban i = i + 1 legyen.
