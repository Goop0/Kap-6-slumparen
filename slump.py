över = ['jacka', 'tröja']
under = ['vinterskor', 'gympadojormedokayu på']

import random

outfits = []

for i in range(0, 7):
    outfit = []

outfit.append(över[random.randint(0, len(över)-1)])
outfit.append(under[random.randint(0, len(under)-1)])

if i == 0:
    
    if outfits[i] == outfits[i-1]:
        print('samma kläder')
    else:
        outfits.append(outfit)
        print(outfits)
#ignorera, detta är oklart och inte den riktiga uppgiften