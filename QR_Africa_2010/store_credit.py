import sys
import os

input_file = sys.argv[1]
with open(input_file) as f:
    content = f.read().splitlines()
    
nb_cases = int(content[0])

output_file = os.path.splitext(input_file)[0] + ".out"

def solve(credit, objects):
    cheapest = min(objects)
    candidates = [elt for elt in objects if elt + cheapest <= credit]
    for i in range(len(objects)):
        for j in reversed(range((i+1),len(objects))):
            if (objects[i] + objects[j]) == credit:
                return objects[i], objects[j]

i = 1
with open(output_file, 'w') as f:
    while nb_cases > 0:
        nb_cases -= 1
        credit = int(content[i])
        i += 1
        nb_objects = int(content[i])
        i += 1
        objects = [int(elt) for elt in content[i].split(' ')]
        i += 1
        
        object1, object2 = solve(credit,objects)
        sol = [objects.index(object1), len(objects) - objects[::-1].index(object2) - 1]
        sol.sort()
        
        f.write('Case #' + str((i-1)/3) + ': ' + str(sol[0]+1) + ' ' + str(sol[1]+1) + '\n')
        
        assert(credit==(object1+object2))
        assert(sol[0] < sol[1])


