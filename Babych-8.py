
#start with 2nd round, where every cat in hat
cats_in_hat = [True] * 100
rounds = 100+1

for round in range(2,rounds):
    for cat in range(round-1,len(cats_in_hat),round):
        cats_in_hat[cat] = not cats_in_hat[cat] 

print([i+1 for i in range(len(cats_in_hat)) if cats_in_hat[i] == True])



import math
cats_with_hats = []
    for cat in range(1, 101):
        #perfect square has an odd number of factors 
        if math.sqrt(cat) % 1 == 0: 
            cats_with_hats.append(cat)

print(cats_with_hats)
    