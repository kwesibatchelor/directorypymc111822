def main():
    family_directory = {
        'Kandia': 'sister',
        'Sekou': 'brother',
        'Kamara': 'youngest brother',
    }

    while True:
        word = input("Enter a word: ")
        if word == "":
            break
        if word in family_directory:
            print(word, ":", family_directory[word])

main()