def main():
    with open('p002_data.txt') as f:
        data = f.read()

    letters = {}
    for index, el in enumerate(data):
        if el not in letters:
            letters[el] = [index, 0]
        else:
            letters[el][1] += 1
            
    print(sorted(letters, key=lambda item: (letters[item][1], letters[item][0])))


if __name__ == '__main__':
    main()