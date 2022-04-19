alphabet = 'abcdefghijklmnopqrstuvwxyz ,?'
alphaD = {}

for letter in alphabet:
    alphaD[letter] = 0
    
text = 'i must stop forgetting my earbuds and shoes in rooms in the school as they get stolen or i worry too much'

for letter in text:
    alphaD[letter] += 1

for key in alphaD:
    print(key, alphaD[key])
