words = input()
check = 'CAMBRIDGE'

for word in words:
  if word in check:
    new_word = words.replace(word, "")
    words = new_word

print(words) 