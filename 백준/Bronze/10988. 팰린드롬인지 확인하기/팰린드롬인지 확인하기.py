string = input() # 알파벳 소문자로만 이루어진 단어가 주어진다. 
# 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램 -> if 문

if string[0:] == string[::-1]:
    print(1)
else:
    print(0)