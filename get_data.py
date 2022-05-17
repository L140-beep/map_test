import time
import sys
import math

dict = {}

with open("py_data.dat", 'w') as output:

    for i in range(0, 6):

        j = math.pow(10, i)
        dict.clear()

        start = time.time()

        for k in range(0, int(j)):
            dict[k] = k

        output.write(f"10^{i}" + '\t' + str(round((time.time() - start) * 1000, 3)) + '\t' + str(sys.getsizeof(dict)) + '\n')
    