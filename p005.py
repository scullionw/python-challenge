import pickle

def main():
    with open('p005_data.p', 'rb') as f:
        data = pickle.load(f)
        
    for line in data:
        for letter, amount in line:
            print(letter * amount, end='')
        print()

if __name__ == '__main__':
    main()