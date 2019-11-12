                            # QUESTION 10

def magic_square(table):
    
    sum_of_diagonal_1 = sum(table[c][c] for c in range(3))
    sum_of_diagonal_2 = table[2][0] + table[1][1] + table[0][2]
    result = ''
    
    for r in table:
        for c in range(3):
            if sum(r) == sum_of_diagonal_1 and sum(r) == sum_of_diagonal_2:
                if sum(r) == sum(r[c] for r in table):
                    result = 'It is a Lo Shu Magic Square'
                else:
                    result = 'It is not a Lo Shu Magic Square'
    print(result)

magic_square([[4,9,2],[3,5,7],[8,1,6]])