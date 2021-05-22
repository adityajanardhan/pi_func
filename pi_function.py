import sys
import json
import random
import math

# main
param_1= int(sys.argv[1])
param_2= int(sys.argv[2])


def pie_calc():
    shots= int(sys.argv[1])
    report= int(sys.argv[2])

    per_round = int(shots/report)

    output = []

    for i in range(0, per_round):
        incircle = 0
        for i in range(0, report):
            random1 = random.uniform(-1.0, 1.0)
            random2 = random.uniform(-1.0, 1.0)
            if( ( random1*random1 + random2*random2 ) < 1 ):
                incircle += 1

        output.append(incircle)
    #pi_val = 4.0 * incircle/shots


    return output

print(pie_calc())
