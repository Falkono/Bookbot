def main():
    path_to_file = "books/frankenstein.txt"
    file_content = get_book_text(path_to_file)
    num_words = countWords(file_content)
    num_letters = numberOfLetters(file_content)
    generateReport(path_to_file, num_words, num_letters)

def countWords(text):
    wordsList = text.split()
    return len(wordsList)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def numberOfLetters(text):
    loweredText = text.lower()
    countDict = {}

    for letter in loweredText:
        if letter in countDict:
            countDict[letter] += 1
        else:
            countDict[letter] = 1
    
    return countDict

def generateReport(path, num_words, num_letters):
    print(f"--- Begin of Report of {path} ---")
    print(f"{num_words} words found in the document")
    newList = generateListOfDict(num_letters)

    for entry in newList:
        if not entry['letter'].isalpha():
            continue
        print(f"The {entry['letter']} character was found {entry['num']} times")
    


def generateListOfDict(dict):
    list = []

    for letter in dict:
        list.append({"letter": letter, "num":  dict[letter]})

    list.sort(reverse=True, key=sort_on)

    return list

def sort_on(dict):
    return dict["num"]



main()