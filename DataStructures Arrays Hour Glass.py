
def hourglasssum(matrix, row, col):
    a = []
    sum = 0
    sum+=matrix[row-1][col-1]
    sum+=matrix[row-1][col]
    sum+=matrix[row-1][col+1]
    sum+=matrix[row][col]
    sum+=matrix[row+1][col-1]
    sum+=matrix[row+1][col]
    sum+=matrix[row+1][col+1]
    return sum

arr = []
for i in range(6):
    arr.append(list(map(int,input().split())))

max_sum = -63
for i in range(1,5):
    for j in range(1,5):
        current_sum = hourglasssum(arr,i,j)
        if current_sum > max_sum:
            max_sum = current_sum
print(max_sum)
