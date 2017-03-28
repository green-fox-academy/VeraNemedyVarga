# Create a method that decrypts texts/reversed_zen_lines.txt
def decrypt(file_name):
    content = open(file_name, "r")
    #print(content)
    read_content = content.read()

    reversed = ""
    for char in range(len(read_content)-1, 0, -1):
        reversed += read_content[char]

    wfile = open("reversed.txt", 'w')
    wfile.write(reversed)
    wfile.close()
    proporder = open("reversed.txt", 'r')
    lista = proporder.readlines()
    result = ""
    for row in range(len(lista)-1, 0, -1):
        result += lista[row]

    solution = open("solution.txt", 'w')
    solution.write(result)
    solution.close()
    content.close()
    return result

print(decrypt("reversed_lines.txt"))
