x = 0
while x < 5:
    print(f'x = {x}')
    x = x + 1
else:
    print("x is not less than 5")
 
# break continue and pass

name = 'pari bhandarkar'
for letter in name:
    if letter == 'a':
        continue   
    print(f'the letter is {letter}')


name = 'pari bhandarkar'
for letter in name:
    if letter == 'h':
        break   
    print(f'the letter is {letter}')
