# Greed is a dice game played with five six-sided dice.
# Your mission, should you choose to accept it, is to score a throw according to these rules.
# You will always be given an array with five six-sided dice values.

#  Three 1's => 1000 points
#  Three 6's =>  600 points
#  Three 5's =>  500 points
#  Three 4's =>  400 points
#  Three 3's =>  300 points
#  Three 2's =>  200 points
#  One   1   =>  100 points
#  One   5   =>   50 point

# A single die can only be counted once in each roll.
# For example, a given "5" can only count as part of a triplet (contributing to the 500 points)
# or as a single 50 points, but not both in the same roll.

def score(dice):
    threes = {1:1000, 6:600, 5:500, 4:400, 3:300, 2:200}
    
    ones = {1:100, 5:50}
    
    counted = []
    points = 0
    
    for sided in dice:
        if sided not in counted:
            credit = dice.count(sided)
            counted.append(sided)
            while credit != 0:
                print(credit)
                if credit >=3 and sided in threes.keys():
                    points += threes.get(sided)
                    credit -= 3
                elif sided in ones.keys():
                    points += ones.get(sided)
                    credit -= 1
                else:
                    break
            
    return points  
            
print(score([1, 1, 1, 3, 1,]))