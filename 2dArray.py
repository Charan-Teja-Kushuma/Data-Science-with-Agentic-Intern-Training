import numpy as np

list_2d = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
           [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
x = np.array(list_2d)
print("2D Array:" , x[0:1,4:8])