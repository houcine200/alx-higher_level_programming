"""function that read from a txt file"""
def read_file(filename=""):
    """read file and print its content"""
    with open (filename, "r") as file:
        print(file.read())
        