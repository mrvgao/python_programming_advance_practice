#------------------
# User Instructions
#
# Hopper, Kay, Liskov, Perlis, and Ritchie live on 
# different floors of a five-floor apartment building. 
#
# Hopper does not live on the top floor. 
# Kay does not live on the bottom floor. 
# Liskov does not live on either the top or the bottom floor. 
# Perlis lives on a higher floor than does Kay. 
# Ritchie does not live on a floor adjacent to Liskov's. 
# Liskov does not live on a floor adjacent to Kay's. 
# 
# Where does everyone live?  
# 
# Write a function floor_puzzle() that returns a list of
# five floor numbers denoting the floor of Hopper, Kay, 
# Liskov, Perlis, and Ritchie.

import itertools

def floor_puzzle():
    # Your code here
   
    TOP = 5
    BOTTOM = 1
    result = next((Hopper, Kay, Liskov, Perlis, Ritchie)
            for Hopper, Kay, Liskov, Perlis, Ritchie in itertools.permutations(range(BOTTOM, TOP+1))
            if  Hopper is not TOP
                and Kay is not BOTTOM
                and Liskov is not TOP and Liskov is not BOTTOM
                and Perlis - Kay > 0
                and abs(Ritchie - Liskov) != 1
                and abs(Liskov - Kay) != 1
            )
    return list(result)

print(floor_puzzle())
