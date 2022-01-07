# The Tower of Hanoi is a mathematical puzzle. 
# It consists of three poles and a number of disks of different sizes which can slide onto any poles. 
# The puzzle starts with the disk in a neat stack in ascending order of size in one pole, 
# the smallest at the top thus making a conical shape. 
# The objective of the puzzle is to move all the disks from one pole (say ‘source pole’) 
# to another pole (say ‘destination pole’) with the help of the third pole (say auxiliary pole).

#The puzzle has the following two rules:
#      1. You can’t place a larger disk onto a smaller disk 
#      2. Only one disk can be moved at a time


# Assuming n-th disk is
# bottom disk (count down)
def tower(n, sourcePole, destinationPole, auxiliaryPole):
 
    # Base case (termination condition)
    if(0 == n):
        return
     
    # Move first n-1 disks
    # from source pole
    # to auxiliary pole
    # using destination as
    # temporary pole
    tower(n-1, sourcePole, auxiliaryPole, destinationPole)
     
    # Move the remaining
    # disk from source
    # pole to destination pole
    print("Move the disk",sourcePole,"from",sourcePole,"to",destinationPole)
     
    # Move the n-1 disks from
    # auxiliary (now source)
    # pole to destination pole
    # using source pole as
    # temporary (auxiliary) pole
    tower(n-1, auxiliaryPole, destinationPole,sourcePole)
 
 
# Driver code

print("Tower of Hanoi with 3 disks")
tower(3, 'S', 'D', 'A')

print("Tower of Hanoi with 4 disks")
tower(4, 'S', 'D', 'A')


