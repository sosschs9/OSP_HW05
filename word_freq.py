# 2021111849 Song Hyegyeong
# 2022-04-13
import sys

if __name__ == '__main__':
    # 파일 열기
    f = open(sys.argv[1], 'r', encoding='UTF8')
    # 파일에서 문장을 읽어서 line에 리스트 형식으로 저장
    line = f.readlines()
    f.close()

    word = []
    D = {}
    # 띄어쓰기를 기준으로 단어 분리 후 word 리스트에 저잘
    for i in range(0, len(line)):
        word.extend(line[i].split())

    for i in range(0, len(word)):
        # 특수문자 제거
        word[i] = ''.join(char for char in word[i] if char.isalnum())
        # word[i]가 딕셔너리 안에 있으면 value값 +1, 없으면 생성
        if (word[i] in D):
            D[word[i]] = D[word[i]] + 1
        else:
            D[word[i]] = 1
    # 내림차순으로 count수 정렬
    sorted_D = sorted(D.items(), key=lambda x: x[1], reverse=True)
    # 출력
    for i in range(0, int(sys.argv[2])):
        print("{0: <7}".format(sorted_D[i][0]) + "{0: >7}".format(sorted_D[i][1]))