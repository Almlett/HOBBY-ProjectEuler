"""
    Problema 18 de project Euler
"""
def new_line(first_line, second_line):
    """
    Generar una nueva linea a partir de 2
    """
    #first_line = [x,...,n]
    #second_line = [x,...,n + 1]
    result = []
    for index, item in enumerate(first_line):
        if second_line[index] + item > second_line[index + 1] + item:
            result.append(second_line[index] + item)
        else:
            result.append(second_line[index + 1] + item)
    return result

def update_pyramid(values):
    """
    Clase para actualizar las ultimas dos lineas de la piramide
    """
    len_pyramid = len(values)
    if len_pyramid > 1:
        first_line = values[len_pyramid-2]
        second_line = values[len_pyramid-1]
        temp = values
        temp.pop()
        temp[len_pyramid-2] = new_line(first_line,second_line)
        update_pyramid(temp)
    return pyramid

pyramid = [
    [3],
    [7,4],
    [2,4,6],
    [8,5,9,3],
]

pyramid2 = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
]

print(update_pyramid(pyramid))
