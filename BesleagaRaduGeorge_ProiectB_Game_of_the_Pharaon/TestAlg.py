
matrix = [ [ 0 for i in range(8) ] for j in range(8) ]
matrix_size=8

def setupMatrix(size):
    for i in range(0,size):
        for j in range(0,size):
            matrix[i][j]=0

def columnFull(columnIndex):
    if matrix[0][columnIndex]!=0 : return True
    return False

def firstEmptyRow(columnIndex):
    for i in reversed(range(0,matrix_size)):
        if matrix[i][columnIndex]==0:
            return i

def addInColumn(columnIndex,value):
    if columnFull(int(columnIndex)): return False
    row=firstEmptyRow(int(columnIndex))
    matrix[row][int(columnIndex)]=value
    return True

def latitude(row,column):
    i=-1
    j=1
    color=matrix[row][column]
    sum=1
    while column+i >= 0 and matrix[row][column+i] == color:
        sum+=1
        i=i-1
    while column+j < matrix_size and matrix[row][column+j] == color:
        sum+=1
        j=j+1
    if sum >= 4:
        return True
    return False

def longitude(row,column):
    i=-1
    j=1
    color=matrix[row][column]
    sum=1
    while row+i >= 0 and matrix[row+i][column] == color:
        sum=sum+1
        i-=1
    while row+j < matrix_size and matrix[row+j][column] == color:
        sum+=1
        j+=1
    if sum >= 4:
        return True
    return False

def diagonal(row,column):
    color=matrix[row][column]

    sum1=1
    i1=-1
    j1=1
    while row+i1>=0 and column+i1>=0 and matrix[row+i1][column+i1]==color:
        i1=i1-1
        sum1+=1
    while row+j1<matrix_size and column+j1<matrix_size and matrix[row+j1][column+j1]==color:
        j1=j1+1
        sum1+=1
    if sum1>=4 :return True

    sum2=1
    i2=-1
    j2=1
    while row+i2>=0 and column-i2<matrix_size and matrix[row+i2][column-i2]==color:
        i2=i2-1
        sum2+=1
    while row+j2<matrix_size and column-j2>=0 and matrix[row-j2][column+j2]==color:
        j2=j2+1
        sum2+=1
    if sum2>=4 : return True
    return False

def fourInRow(row,column):
    if matrix[row][column]==0 : return False
    if latitude(row,column) :return True
    if diagonal(row,column) :return True
    if longitude(row,column):return True
    return False

def endGame():
    for i in range(0,matrix_size):
        for j in range(0,matrix_size):
            if fourInRow(i,j)==True:
                return matrix[i][j]
    return 0

i=1
setupMatrix(matrix_size)
while endGame()==0:
    if i==1 : i=2
    else :i=1
    row = input("Chose First the row")
    addInColumn(row,i)
    for j in matrix:
        print(j)
print("EndGame")