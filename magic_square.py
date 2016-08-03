#function checks whether or not given square is a 3x3 magic square

def magic_square(square):
    #create list to hold all sums for evaluation
    sums = []

    #create 3x3 matrix
    w, h = 3, 3
    square = [[0 for x in range(w)] for y in range(h)]

    #add colums
    for col in range(3):
        sums.append(sum(row[col] for row in square))

    #add rows
    sums.extend([sum (lines) for lines in square])

    #add diagonal left
    diag_left_sum = 0
    for i in range(0,3):
        diag_left_sum +=square[i][i]
    sums.append(diag_left_sum)

    #add diagonal right
    diag_right_sum = 0
    for i in range(0,3):
        diag_right_sum +=square[i][i]
    sums.append(diag_right_sum)

    #if there is more than one value in the list, return False; else return True
    if len(set(sum_list))>1:
        print False
    print True

#testing code
#print 'test'
