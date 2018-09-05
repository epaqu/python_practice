f = open("./%s" %("a.mtx.txt"), "r")
for line in f:
    for i in range (len(line.strip().split())):
        stri = line.strip().split()[i]
        print stri
        
"""
def string(matrix):
    result = ""
    result += "Matrix: %s" %matrix._matrix_name
    result += "\nNumber of rows: %-3d, Number of columns: %-3d" % (matrix._numRos, matrix._numCols)
    result += "\n|"
    line = ""
    for rowList in matrix._matrix:
        for i in range (len(rowList)):
            print rowList[i]
            line += "%10.2f" %float(rowList[i])
        result += line
        result += " |"
        line = ""
    return result
    