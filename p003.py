def main():
    with open('p003_data.txt') as f:
        data = f.read().replace('\n', '')
    
    print(''.join([data[i + 4] for i, letter in enumerate(data[0:-8]) if data[i+1:i+1+3].isupper() and data[i:i+9:4].islower() and data[i+5:i+5+3].isupper()]))

if __name__ == '__main__':
    main()

