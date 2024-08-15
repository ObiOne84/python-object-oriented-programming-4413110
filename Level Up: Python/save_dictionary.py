import json
import pickle
import os



test_dict = {1: 'a', 2: 'b', 3: 'c'}
script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, '/workspace/python-object-oriented-programming-4413110/Level Up: Python/test_dict.pickle')
file_path_2 = os.path.join(script_dir, '/workspace/python-object-oriented-programming-4413110/Level Up: Python/test_dict.json')

def save_dictionary_as_JSON(dictionary, path):
  with open(path, 'w') as file:
    json.dump(dictionary, file, indent=4)


# here we decode, but json is not allowing the data to be saved as int, so we need to convert back to int when loading
# use pickle instead.
def load_json_as_dictionary(json_file_path):
  with open(json_file_path, 'r') as file:
    dictionary = json.load(file)
    dictionary = {int(key): value for key, value in dictionary.items()}
  return dictionary


def save_dict(dict_to_save, file_path):
  with open(file_path, 'wb') as file:
    pickle.dump(dict_to_save, file)


def load_dict(file_path):
  with open(file_path, 'rb') as file:
    return pickle.load(file)


# save_dict(test_dict, file_path)
# recovered = load_dict(file_path)
# print(recovered)
# save_dictionary_as_JSON(test_dict, file_path_2)
recovered = load_json_as_dictionary(file_path_2)
print(recovered)