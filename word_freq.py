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
    print(word)
    f.close()
    # line.count(word[1])
