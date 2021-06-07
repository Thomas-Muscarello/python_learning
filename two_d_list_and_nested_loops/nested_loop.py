number_grid=[
    [1,2,3],
    [4,5,6,66],
    [7,8,9],
    [0]
]

#For loop inside a For loop
#parse through a 2D List

#Print each row
for row in number_grid:
        print(row)

#Access each idividual attribute in each array
for row in number_grid:
    for column in row:
        print(column)