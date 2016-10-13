def letter_mapping(string):
    return ''.join([chr(((ord(letter) - 97 + 2) % 26) + 97) if 97 <= ord(letter) <= 123 else letter for letter in string])

def main():
    with open('p001_data.txt') as f:
        string = f.read()

    print(letter_mapping(string))
    print(letter_mapping('map'))

if __name__ == '__main__':
    main()