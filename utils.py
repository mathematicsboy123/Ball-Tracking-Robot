import numpy as np

def center_average(hsv):
    avg = np.array([0, 0, 0])
    for i in range(10):
        x = int(len(hsv)/2)
        row = hsv[x]
        y = int(len(row)/2) 
        y += i

        pixel = row[y]
        avg += pixel
    
    divided = avg/10
    for i in range(0, 3):
        divided[i] = int(divided[i])
    print(divided)
