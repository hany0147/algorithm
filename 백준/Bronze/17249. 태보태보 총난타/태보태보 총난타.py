taebo = input()
left = 0
right = 0

for lef in taebo[:taebo.index('(')]:
    if lef == '@':
        left += 1
for rig in taebo[taebo.index(')'):]:
    if rig == '@':
        right += 1

print(left, right)