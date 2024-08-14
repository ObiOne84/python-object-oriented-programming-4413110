numbers = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]

def index_all(arr, item):
  indices = []
  # enumarate(arr) gives both the index and the value of each element in the list
  for index, value in enumerate(arr):
    # check for matching value
    if value == item:
      # if value equal item append indext to list as list
      indices.append([index])
      # if the value is a list, call the function again to search that list
    elif isinstance(arr[index], list):
      # for each result append indext + i to consturct full path 
      for i in index_all(arr[index], item):
        indices.append([index] + i)
  return indices

print(index_all(numbers, 2))