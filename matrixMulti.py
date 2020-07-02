import numpy
from matrixMulitplicationLib import dotProduct

A = [ [1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]  ]


B = [ [1, 0, 0],
      [0, 1, 0],
      [0, 0, 1]  ]

endProduct = [ [0, 0, 0],
               [0, 0, 0],
               [0, 0, 0]  ]

dotProduct(A, B)