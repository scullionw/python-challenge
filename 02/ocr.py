__author__ = 'williamscullion'

a = open('hello.txt')
g = a.read()
ocr_set = set()
remove_set = set()
remove_set = {'\n'}
for i in g:
    ocr_set.add(i)

for i in (ocr_set - remove_set):
    print(i, end="  ")

print(len(ocr_set-remove_set))