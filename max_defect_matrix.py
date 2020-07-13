LOW = 0
HIGH = 500

def extremidades(arr, row, col):
  oeste = arr[row - 1][col]
  norte = arr[row][col - 1]
  noroeste = arr[row - 1][col - 1]
  return min(oeste, norte, noroeste)

def buscar_max_defect_matrix(matrix):
  size = len(matrix)
  if size < LOW and size > HIGH:
    return

  aux = [[0 for x in range(len(matrix[0]))] for y in range(size)]
  max = 0

  for row in range(1, size):
    for col in range(1, len(matrix[row])):
      if matrix[row][col] == 1:
        aux[row][col] = extremidades(aux, row, col) + 1
        if aux[row][col] > max:
          max = aux[row][col]

  print(max)

factory_line = [
  [0, 1, 0, 1],
  [1, 0, 1, 0],
  [0, 1, 1, 1],
  [0, 0, 1, 1],
  [0, 1, 1, 1]]

buscar_max_defect_matrix(factory_line)
