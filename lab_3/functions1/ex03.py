""" 
    r + c = 35     (1 1 | 35)               (1  1 | 35)                (1 1 | 35)              (1 0 | 12)
    4r + 2c = 94   (4 2 | 94)  R2->-4R1+R2  (0 -2 |-46)  R2->-(1/2)R2  (0 1 | 23)  R1->-R2+R1  (0 1 | 23) 

    (r) = (12)
    (c) = (35)

    by formula: c = -(numleg-4*numhead)/2,  r = numhead-c
"""

def solve(numheads, numlegs):
    c = -(numlegs-4*numheads)/2
    r = numheads-c
    return r, c

print(solve(35, 94))