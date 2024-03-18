def main():
    path_to_file = "books/frankenstein.txt"


    with open(path_to_file) as file:
        file_content = file.read()
        print(file_content)


main()