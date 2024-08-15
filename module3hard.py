data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(data_structure):
  sum_ = 0
  if isinstance(data_structure, (list, tuple, set)):
    for item in data_structure:
      sum_ += calculate_structure_sum(item)
  elif isinstance(data_structure, dict):
    for key, value in data_structure.items():
      sum_ += calculate_structure_sum(key)
      sum_ += calculate_structure_sum(value)
  elif isinstance(data_structure, (int, float)):
    sum_ += data_structure
  elif isinstance(data_structure, str):
    sum_ += len(data_structure)
  return sum_


result = calculate_structure_sum(data_structure)
print(result)
