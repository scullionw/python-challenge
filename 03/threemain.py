__author__ = 'williamscullion'


file = open('threetxt.txt')
file_text = "".join(file.read().splitlines())
capital_letters = []
letters = []
answers = []
answer = []
for i in range(26):

    capital_letters.append(chr(65+i))
    letters.append(chr(97+i))

for v, i in enumerate(file_text[4:len(file_text)-4], start=4):

    if i in letters:

        cond1 = all([file_text[v - j] in capital_letters for j in range(1, 4)])
        cond2 = all([file_text[v + j] in capital_letters for j in range(1, 4)])
        cond3 = all([file_text[v - 4] in letters, file_text[v + 4] in letters])

        if all([cond1, cond2, cond3]):

            answers.append(file_text[v-4:v+5])
            answer.append(i)

print(answers)
print("".join(answer))
