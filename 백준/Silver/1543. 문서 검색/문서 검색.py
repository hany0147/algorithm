words = input()
answer = input()

# 문자열 메서드
# 원하는 문자를 "-"으로 대체하고 -의 개수를 센다.

new_words = words.replace(answer, '-')

print(new_words.count('-'))