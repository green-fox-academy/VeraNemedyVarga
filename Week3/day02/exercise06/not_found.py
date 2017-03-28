def ask_for_file():
    try:
        filename = input()
        askforfile = open(filename, "r")
        read_content = askforfile.readlines()
        print(len(read_content))
    except FileNotFoundError:
        print("Bena vagy")
ask_for_file()
