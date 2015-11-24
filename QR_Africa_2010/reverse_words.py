import sys
import os

input_file = sys.argv[1]

with open(input_file) as f:
    content = f.read().splitlines()
    
nb_cases = int(content[0])

output_file = os.path.splitext(input_file)[0] + ".out"

i = 0

with open(output_file, 'w') as f:
    while nb_cases > 0:
        i += 1
        nb_cases -= 1
        objects = content[i].split(' ')[::-1]
        f.write('Case #' + str(i) + ': ' + ' '.join(objects) + '\n')