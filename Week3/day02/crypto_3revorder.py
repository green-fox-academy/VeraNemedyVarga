# Create a method that decrypts texts/reversed_zen_order.txt
def decrypt(file_name):
    content = open(file_name, 'r')
    read_content = content.readlines()
    result = ""
    for row in range(len(read_content)-1, 0, -1):
        result += read_content[row]
    revord = open("revorder.txt", 'w')
    revord.write(result)
    revord.close()
    content.close()
    return result

print(decrypt("reversed_order.txt"))
