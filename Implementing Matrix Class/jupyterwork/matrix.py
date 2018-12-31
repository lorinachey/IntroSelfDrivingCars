import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def get_row(matrix, row):
    """
    Returns the row as a list at the specified row number in the matrix.
    """
    return matrix[row]
    
def get_column(matrix, column_number):
    """
    Returns the column at the specified column_number of the matrix.
    """    
    column = [] 
    for i in range(0, len(matrix)):
            for j in range(len(matrix[i])):
                if (j == column_number):
                    column.append(matrix[i][j])
    return column;

def dot_product(v1, v2):
    """
    Returns the result of the dot product of the two vectors passed in.
    """
    if len(v1) != len(v2):
        print("error! Vectors must have same length")
    result = 0
    
    for i in range(len(v1)):
        value_1 = v1[i]
        value_2 = v2[i]
        result += value_1 * value_2
    return result

class Matrix(object):

    # Constructor
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #
    # Primary matrix math methods
    #############################
 
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
        if self.h > 2:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices largerer than 2x2.")
        
        if (self.w == 1 and self.h == 1):
            return self.g[0]
        else:
            cross_multiplier = ((self.g[0][0] * self.g[1][1]) - (self.g[1][0] * self.g[0][1]))
            return cross_multiplier

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        """
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")
        
        ## Format suggested from this project's code review:
        return sum(self.g[i][i] for i in range(self.h))

    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
        if self.h > 2:
            raise(NotImplementedError, "inversion not implemented for matrices larger than 2x2.")    
    
        matrix = self.g
        inverse = []

        if (len(matrix) == 1):
            inverse.append([1/matrix[0][0]])
        else: 
            #The following code was suggested from this project's code review:
            #find identity matrix
            I = identity(2)
            #find trace
            tr = self.trace()
            #find the determinant with the previously computed function.
            det = self.determinant()
            #perform inverse
        return 1.0 / det * (tr * I - self)

    def T(self):
        """
        Returns a transposed copy of this Matrix.
        """
        transpose = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                transpose.g[j][i] = self.g[i][j] 

        return transpose
    
    def is_square(self):
        return self.h == self.w

    #
    # Begin Operator Overloading
    ############################
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for row in self.g:
            s += " ".join(["{} ".format(x) for x in row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        new_matrix = zeroes(self.h, self.w)

        for i in range(self.h):
            for j in range(self.w):
                new_matrix[i][j] = self.g[i][j] + other.g[i][j]
                
        return new_matrix
        

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        
        neg_matrix = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                neg_matrix[i][j] = -1 * self.g[i][j] 
        
        return neg_matrix

    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        new_matrix = zeroes(self.h, self.w)
        
        for i in range(self.h):
            for j in range(self.w):
                new_matrix.g[i][j] = self.g[i][j] - other.g[i][j]
                
        return new_matrix

    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        """

        m_rows = len(self.g)
        p_columns = len(other.g[0])

        result = []
        row_result = []
   
        for i in range(0, m_rows):
            row = get_row(self.g, i)
            for j in range(0, p_columns):
                col = get_column(other.g, j)
                row_result.append(dot_product(row, col))
            result.append(row_result)
            row_result = []        
        return Matrix(result)
        

    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is not a matrix.

        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
        """
        if isinstance(other, numbers.Number):
            pass
            
            new_matrix = zeroes(self.h, self.w)
        
            for i in range(self.h):
                for j in range(self.w):
                    new_matrix[i][j] = other * self.g[i][j]
                
        return new_matrix
            