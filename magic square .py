# magic_square=[[8,3,4],[1,5,9],[6,7,2]]
# i=0
# while i<len(magic_square):
#     row=0
#     j=0
#     row=0
#     column=0
#     diagonal=0
#     while j<len(magic_square[i]):
#         row=row+magic_square[i][j]
#         column=column+magic_square[j][i]
#         diagonal=diagonal+magic_square[j][j]
#         j=j+1
#     i=i+1
# print(row,"=sum of row")
# print(column,"=sum of column")
# print(diagonal,"=sum of diagonal")
# if row==column==diagonal:
#     print("magic square")
# else:
#     print("not magic square")


# magic_square = [
# [5, 3, 7],
# [1, 8, 9],
# [6, 4, 2]
# ]

# i=0
# while i<len(magic_square):
#     row=0
#     j=0
#     row=0
#     column=0
#     diagonal=0
#     while j<len(magic_square[i]):
#         row=row+magic_square[i][j]
#         column=column+magic_square[j][i]
#         diagonal=diagonal+magic_square[j][j]
#         j=j+1
#     i=i+1
# print(row,"=sum of row")
# print(column,"=sum of column")
# print(diagonal,"=sum of diagonal")
# if row==column==diagonal:
#     print("magic square")
# else:
#     print("not magic square")



# magic_square = [
# [8, 3, 4, 0],
# [1, 5, 9],
# [6, 7, 2]
# ]
# i=0
# while i<len(magic_square):
#     j=0
#     row=0
#     column=0
#     diagonal=0
#     while j<len(magic_square[i]):
#         row=row+magic_square[i][j]
#         column=column+magic_square[j][i]
#         diagonal=diagonal+magic_square[j][j]
#         j=j+1
#     i=i+1
# print(row,"=sum of row")
# print(column,"=sum of column")
# print(diagonal,"=sum of diagonal")
# if row==column==diagonal:
#     print("magic square")
# else:
#     print("not magic square")

magic_square=[
[25,13,1,19,7], 
[16,9,22,15,3],
[2,5,18,6,24],
[8,21,14,2,20],
[4,17,10,23,11] 
]  
i=0
while i<len(magic_square):
    row=0
    j=0
    row=0
    column=0
    diagonal=0
    while j<len(magic_square[i]):
        row=row+magic_square[i][j]
        column=column+magic_square[j][i]
        diagonal=diagonal+magic_square[j][j]
        j=j+1
    i=i+1
print(row,"=sum of row")
print(column,"=sum of column")
print(diagonal,"=sum of diagonal")
if row==column==diagonal:
    print("magic square")
else:
    print("not magic square")



