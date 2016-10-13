import zipfile

def next_nothing(file, name):
    comment = file.getinfo(name + '.txt').comment.decode('utf-8')
    num = file.read(name + '.txt').split()[-1].decode('utf-8')
    if num.isdigit():
        return num, comment
    else:
        return None, comment

def main():
    nothings = ['90052']
    comments = []
    with zipfile.ZipFile('p006_data.zip') as file:
        while nothings[-1]:
            num, comment = next_nothing(file, nothings[-1])
            nothings.append(num)
            comments.append(comment)

    print(''.join(comments))

if __name__ == '__main__':
    main()