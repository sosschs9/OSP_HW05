# 2021111849 Song Hyegyeong
# 2022-04-13
import sys

if __name__ == '__main__':
    f = open(sys.argv[1], 'r', encoding='UTF8')
    word = []
    D = {}
    line = f.readlines()
    for i in range(0, len(line)):
        word.extend(line[i].split())

    for i in range(0, len(word)):
        word[i] = ''.join(char for char in word[i] if char.isalnum())
        if (word[i] in D):
            D[word[i]] = D[word[i]] + 1
        else:
            D[word[i]] = 1
    f.close()

    print(D)
