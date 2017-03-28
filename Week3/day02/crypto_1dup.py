def decrypt(file_name):
    content = open(file_name, "r")
#    print(content)
    read_content = content.read()
    file = ""
    for char in range(0, len(read_content)):
        if char % 2 == 0:
            file += read_content[char]
    wfile = open("dupchar.txt", 'w')
    wfile.write(file)
    wfile.close()
    content.close()

    return file


print(decrypt("duplicated_chars.txt"))
