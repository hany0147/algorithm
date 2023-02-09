words = input()

if 'c=' in words:
    words = words.replace('c=', '1')
if 'c-' in words:
    words = words.replace('c-', '2')
if 'dz=' in words:
    words = words.replace('dz=', '3')    
if 'd-' in words:
    words = words.replace('d-', '4')
if 'lj' in words:
    words = words.replace('lj', '5')
if 'nj' in words:
    words = words.replace('nj', '6')
if 's=' in words:
    words = words.replace('s=', '7')
if 'z=' in words:
    words = words.replace('z=', '8')

# print(words)
print(len(words))