import sys
import os

input_file = sys.argv[1]
with open(input_file) as f:
    content = f.read().splitlines()
    
nb_cases = int(content[0])

output_file = os.path.splitext(input_file)[0] + ".out"

def solve(vect1, vect2):
    vect1.sort()
    vect2.sort(reverse=True)
    res = 0
    for i in range(len(vect1)):
        res += vect1[i] * vect2[i]
    return res

i = 0
with open(output_file, 'w') as f:
    while nb_cases > 0:
        nb_cases -= 1
        i += 1
        size = int(content[i])
        i += 1
        vec1 = [int(elt) for elt in content[i].split(' ')]
        i += 1
        vec2 = [int(elt) for elt in content[i].split(' ')]
        
        sol = solve(vec1,vec2)

        f.write('Case #' + str((i)/3) + ': ' + str(sol ) + '\n')
        


