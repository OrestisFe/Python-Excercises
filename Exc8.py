'''
Γράψτε ένα πρόγραμμα σε Python το οποίο προσομοιώνει 3 έξυπνα φανάρια στα οποία υπάρχει τυχαία ροή αυτοκινήτων.
Τα τρία φανάρια ξεκινάνε με ένα τυχαίο πλήθος αυτοκινήτων.
Πράσινο έχει πάντα το φανάρι με τα περισσότερα αυτοκίνητα, αν είναι παραπάνω διαλέγουμε ένα στην τύχη.
Σε κάθε άναμα του φαναριού μπορούν να φύγουν αυτοκίνητα (τυχαία από 5-10) από αυτό που είναι κόκκινο,
ενώ παράλληλα έρχονται και στα άλλα δύο αυτοκίνητα (0-5).
Το πρόγραμμά σας εμφανίζει σε κάθε άναμα πράσινου τα αυτοκίνητα που έχει το κάθε φανάρι και πόσα έρχονται/φεύγουν.
'''
import random
from operator import itemgetter

#light = [numberOfCars, State, PreviousChange, Name]
light1 = [random.randint(1,100), "RED", 0, "light1"]
light2 = [random.randint(1,100), "RED", 0, "light2"]
light3 = [random.randint(1,100), "RED", 0, "light3"]

lights = [light1,light2,light3]

def printStatus():
    #Figuring out the position of each light in the list
    positions = [0, 0, 0]
    for i in range(len(lights)):
        if lights[i][3]=="light1":
            positions[0] = i
        elif lights[i][3]=="light2":
            positions[1] = i
        else:
            positions[2] = i
    #Printing data
    print("Light1:"+lights[positions[0]][1]+" Cars:"+str(lights[positions[0]][0])+ " ("+str(lights[positions[0]][2])+") "+
    "| Light2:"+lights[positions[1]][1]+" Cars:"+str(lights[positions[1]][0])+" ("+str(lights[positions[1]][2])+") "+
    "| Light3:"+lights[positions[2]][1]+" Cars:"+str(lights[positions[2]][0])+" ("+str(lights[positions[2]][2])+")")


printStatus()
while(light1[0]>0 and light2[0]>0 and light3[0]>0):
    #Sorting the list
    lights.sort(reverse=True)
    #Setting the light with the largest number of cars GREEN and the others RED
    lights[0][1] = "GREEN"
    lights[1][1] = "RED"
    lights[2][1] = "RED"
    #Setting randomly how many cars will come and go
    lights[0][2] = "-"+str(random.randint(5, 10))
    lights[1][2] = "+"+str(random.randint(1, 5))
    lights[2][2] = "+"+str(random.randint(1, 5))
    #Making adjustments to the numberOfCars
    if (lights[0][0]-int(lights[0][2][1:]))<0:#Setting count=0 when there is no more cars left to leave the light
        lights[0][0] = 0
    else:
        lights[0][0] -= int(lights[0][2][1:])
    lights[1][0] += int(lights[1][2][1:])
    lights[2][0] += int(lights[2][2][1:])
    #Printing the data
    printStatus()
