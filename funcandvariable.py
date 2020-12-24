matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16]
        ]

winner_matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
    [1,5,9,13],
    [2,6,10,14],
    [3,7,11,15],
    [4,8,12,16],
    [4,7,10,13],
    [1,6,11,16]
]

gamers=["A","B"]

index=0

def winner(matrix,gamer):
    global winner_matrix
    current = []
    indexl=1
    for i in matrix:
        for j in i:
            if j==gamer:
                current.append(indexl)
            indexl+=1
    for i in winner_matrix:
        count=0
        for x in current:
            for y in i:
                if y==x:
                    count+=1
                    if count==4:
                        return True
    return False