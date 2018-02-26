#Euler Problem 5 Lowest common multiple
# Michael Garvey
# credits: https://gist.github.com/PEZ/47534

i = 1
for k in (range(1, 21)): #using range to test numbers 1 to 20
  if i % k > 0: 
    for j in range(1, 21): 
      if (i*j) % k == 0: 
        i *= j 
        break 

print (i)