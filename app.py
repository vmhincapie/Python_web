def find_pairs(numbers):
  """
  Encuentra las parejas de números en `numbers` que suman 12.

  Args:
    numbers: Una lista de números.

  Returns:
    Una lista de parejas de números que suman 12.
  """

  pairs = []
  for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
      if numbers[i] + numbers[j] == 12:
        pairs.append((numbers[i], numbers[j]))
  return pairs


numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
pairs = find_pairs(numbers)

print(pairs)
