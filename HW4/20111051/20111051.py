
class CS101Matrix(object):
    """ This class should provide matrix arithmetic operations, such as +, -, * if possible.
        Also it provides unary operations, such as transpose and negation.
        When the matrix is a vector, which has only one row or column,
        it should be able to calculate some sort of products with corresponding vectors.
        Notice that all the operations should be performed on proper matrix(es).
    """
    #self._matrix_name = ""     # string, virtual matrix name
    #self._matrix = []          # list of list, representing matrix itself
    #self._numRos = 0           # int, number of rows
    #self._numCols = 0          # int, number of columns
    #self._isValid = True       # bool, indicator whether it is correctly constructed or not
                                # when user created empty matrix object with his/her intention it is assumed to be valid
    pass

def initialize(matrixFile = None):
    """
    Part I.
    Given "matrixFile" as file name, you should create CS101MAtrix class instance and its attributes accordingly.
    You should check the validity of the file description about the matrix.
    If invalid form, for example skewed matrix, you should return None.
    
    Mandatory attributes as follows:
       _matrix_name: string, virtual matrix name
       _matrix: list of list, representing matrix itself
                elements of _matrix are considered as floating values
       _numRows: int, number of rows
       _numCols: int, number of columns
       _isValid: bool, indicator whether it is correctly constructed or not
                 when user created empty matrix object with his/her intention it is assumed to be valid
    """
    if matrixFile == None:
        result_matrix = CS101Matrix()
        result_matrix._matrix_name = None
        result_matrix._isValid = True
        result_matrix._matrix = []
        result_matrix._numCols = 0
        result_matrix._numRows = 0
        return result_matrix
    else:
        f = open("./%s" %(matrixFile), "r")
        row = []
        result_matrix = CS101Matrix()
        result_matrix._matrix_name = f.readline().strip().split()[-1]
        result_matrix._matrix = []
        result_matrix._numRows = 0
        result_matrix._numCols = 0
        result_matrix._isValid = True
        for line in f:
            row = line.strip().replace('\"', "").split()
            if result_matrix._numCols != len(row) and result_matrix._numRows > 0 and len(row) != 0:
                result_matrix._numCols = len(row)
                result_matrix._isValid = False
                result_matrix._numRows += 1
                break
            elif result_matrix._numCols != len(row) and result_matrix._numRows == 0:
                result_matrix._numCols = len(row)
                result_matrix._matrix.append(row)
                result_matrix._numRows += 1
            elif result_matrix._numCols == len(row) and result_matrix._numRows > 0:
                result_matrix._matrix.append(row)
                result_matrix._numRows += 1
    return result_matrix
    
def string(matrix):
    result = ""
    """ Part II.
    Display CS101Matrix object nicely.
    First, you should show _matrix_name attribute of the form "Matrix: ..."
    Second, you should show _numRows and _numCols attributes of the form
    "Number of rows: ..., Number of columns: ..."
    Then, "|" followed by proper space and each element enclosed with "|" in a row
    Notice that every element shoud be displays only to two decimal places.
    """
    result += "Matrix: %s" %matrix._matrix_name
    result += "\nNumber of rows: %3d, Number of columns: %-3d" % (matrix._numRows, matrix._numCols)
    line = ""
    for rowList in matrix._matrix:
        for i in range (len(rowList)):
            line += "%10.2f" %float(rowList[i])
        result += "\n|"
        result += line
        result += " |\n"
        line = ""
    return result

def getElement(matrix, x, y):
    if not matrix._isValid:
        return None
    elif x > matrix._numRows or y > matrix._numCols or x <= 0 or y <= 0:
        return None
    return float(matrix._matrix[x - 1][y - 1])

def negate(matrix):
    """ Part III
    Sign of every element in the matrix should be inversed.
    """
    for rowVectors in matrix._matrix:
        for i in range(len(rowVectors)):
            rowVectors[i] = (-1) * float(rowVectors[i])

def add(leftMatrix, rightMatrix):
    """ Part IV - 1
    Add two matrices, say matrix A & matrix B.
    This operation should be performed only when the size of two matrices are the same.
    You might be careful that when the result is displayed on the console, the result should be nicely either.
    """
    newMatrix = CS101Matrix()
    newMatrix._matrix = []
    newMatrix._matrix_name = "Result of Matrix Addition (%s + %s)" % (leftMatrix._matrix_name, rightMatrix._matrix_name)
    newMatrix._numRows = leftMatrix._numRows
    newMatrix._numCols = leftMatrix._numCols
    newMatrix._isValid = True
    row = []
    if leftMatrix._numRows != rightMatrix._numRows or leftMatrix._numCols != rightMatrix._numCols:
        print "Matrices of different sizes cannot be added."
        return None
    else:
        for i in range (len(leftMatrix._matrix)):
            for j in range (len(leftMatrix._matrix[i])):
                row.append(float(leftMatrix._matrix[i][j]) + float(rightMatrix._matrix[i][j]))
            newMatrix._matrix.append(row)
            row = []
        return newMatrix

def subtract(leftMatrix, rightMatrix):
    """ Part IV - 2
    Subtract rightMatrix from leftMatrix and resturn the resulting matrix by creating new CS101Matrix object.
    """
    newMatrix = CS101Matrix()
    newMatrix._matrix = []
    newMatrix._matrix_name = "Result of Matrix Subtraction (%s + %s)" % (leftMatrix._matrix_name, rightMatrix._matrix_name)
    newMatrix._numRows = leftMatrix._numRows
    newMatrix._numCols = leftMatrix._numCols
    newMatrix._isValid = True
    row = []
    if leftMatrix._numRows != rightMatrix._numRows or leftMatrix._numCols != rightMatrix._numCols:
        print "Matrices of different sizes cannot be subtracted."
        return None
    else:
        for i in range (len(leftMatrix._matrix)):
            for j in range (len(leftMatrix._matrix[i])):
                row.append(float(leftMatrix._matrix[i][j]) - float(rightMatrix._matrix[i][j]))
            newMatrix._matrix.append(row)
            row = []
        return newMatrix
        
def multiply(leftMatrix, rightMatrix):
    """ Part V
    This operation should be performed
    only when the number of columns of leftMatrix._matrix attribute and
    the number of rows of rightMatrix._matrix attribute of right-hand side object are equal.
    """
    newMatrix = CS101Matrix()
    newMatrix._matrix_name = "Result of Matrix Multiplication (%s * %s)" % (leftMatrix._matrix_name, rightMatrix._matrix_name)
    newMatrix._matrix = []
    newMatrix._numRows = leftMatrix._numRows
    newMatrix._numCols = rightMatrix._numCols
    newMatrix._isValid = True
    row = []
    sum = 0
    if leftMatrix._numCols != rightMatrix._numRows:
        print "The number of columns of the left matrix and the number of rows of the right matrix have to be equal"
        return None
    else:
        for i in range (len(leftMatrix._matrix)):
            for j in range (len(leftMatrix._matrix[i])):
                for k in range (len(leftMatrix._matrix[i])):
                    sum += (float(leftMatrix._matrix[i][k]) * float(rightMatrix._matrix[k][j]))
                row.append(sum)
                sum = 0
            newMatrix._matrix.append(row)
            row = []
    return newMatrix

def equal(leftMatrix, rightMatrix):
    """ Part VI
    This operation compare every element of leftMatrix._matrix attribute with the rightMatrix object.
    If all the values of the elements and the size is identical, the return True.
    Otherwise, return False
    """
    if leftMatrix._numRows != rightMatrix._numRows or leftMatrix._numCols != rightMatrix._numCols:
        return False
    else:
        for i in range (len(leftMatrix._matrix)):
            for j in range (len(leftMatrix._matrix[i])):
                if leftMatrix._matrix[i][j] != rightMatrix._matrix[i][j]:
                    return False
    return True
    
def transpose(matrix):
    """ Part VII
    Transpose _matrix attribute of matrix CS101Matrix object.
    In other words, value of matrix._matrix[x][y] before transpose should be
    the value of matrix._matrix[y][x] for any x and y within the range.
    """
    newMatrix = CS101Matrix()
    newMatrix._matrix = []
    newMatrix._matrix_name = "Transposed Matrix (%st)" % (matrix._matrix_name)
    newMatrix._numRows = matrix._numCols
    newMatrix._numCols = matrix._numRows
    newMatrix._isValid = True
    row = []
    for i in range (newMatrix._numRows):
        for j in range (newMatrix._numCols):
            row.append(matrix._matrix[j][i])
        newMatrix._matrix.append(row)
        row = []
    return newMatrix
    
def scalarProduct(scale, matrix):
    """ Part IIX
    This operations should be performed on every element of the matrix object.
    As a result, every element in matrix is multiplied by scale.
    .
    """
    newMatrix = CS101Matrix()
    newMatrix._matrix = []
    newMatrix._matrix_name = "Matrix %s multiplied by %d" % (matrix._matrix_name, scale)
    newMatrix._numRows = matrix._numRows
    newMatrix._numCols = matrix._numCols
    newMatrix._isValid = True
    row = []
    for i in range (newMatrix._numRows):
        for j in range (newMatrix._numCols):
            row.append(scale * float(matrix._matrix[i][j]))
        newMatrix._matrix.append(row)
        row = []
    return newMatrix

def innerProduct(leftMatrix, rightMatrix):
    """ Part IX
    This operations should be performed only when both of _matrix in this and rightMatrix object is vector.
    When vector _matrix of leftMatrix object is represented as vec(A) and vector _matrix of rightMatrix object as vec(B), and
    the angle two vectors make as ang(A, B), then the result of this operation is as follows:
       result = |vec(A)| * |vec(B)| * cos(ang(A, B))
    """
    result = 0
    if leftMatrix._numRows == rightMatrix._numRows and leftMatrix._numCols == rightMatrix._numCols:
        if leftMatrix._numRows == 1 or leftMatrix._numCols ==1:
            for i in range (len(leftMatrix._matrix)):
                for j in range (len(leftMatrix._matrix[i])):
                    result += (float(leftMatrix._matrix[i][j]) * float(rightMatrix._matrix[i][j])) 
            return float(result)
    else:
        return None


a = initialize("a.mtx.txt")
b = initialize("b.mtx.txt")
c = initialize("c.mtx.txt")

print string(a)
f = open("test.info.txt", "w")
f.write(string(a))
f.close()

negate(a)
print string(a)

a = initialize("a.mtx.txt")
print string(add(a, b))

print string(a)
print string(transpose(a))

""
a = initialize("a.mtx.txt")
b = initialize("b.mtx.txt")
c = initialize("c.mtx.txt")
d = initialize("HW4_20111051(a).mtx.txt")
e = initialize("HW4_20111051(b).mtx.txt")

f = open("test.info.txt", "w")
f.write(string(a))
f.write(string(add(a,b)))
f.write(string(subtract(a,b)))
f.write(string(multiply(a,b)))
print innerProduct(d,e)
f.write(string(scalarProduct(3,b)))
f.write(string(transpose(a)))
negate(a)
f.write(string(a))
f.write(string(multiply(a,b)))
print getElement(a, 2, 1)
negate(a)
print getElement(a, 1, 1)
print equal(a, b)
print equal(a, d)
print equal(d, d)
a = initialize("a.mtx.txt")
f.write(string(a))
f.close()
