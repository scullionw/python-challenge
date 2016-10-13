import requests

def nothing(string):
    num = string.split(' ')[-1]
    if num.isdigit():
        return int(num)

def newurl(nothing):
    return 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + str(nothing)

def main():
    nothings = [12345]

    while nothings[-1]:
        nothings.append(nothing(requests.get(newurl(nothings[-1])).text))
    else:
        nothings.append(nothings[-2] // 2)
    while nothings[-1]:
        nothings.append(nothing(requests.get(newurl(nothings[-1])).text))

    print(newurl(nothings[-2]))
    
if __name__ == '__main__':
    main()