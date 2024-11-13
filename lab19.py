import pickle

T1 = tuple(range(10, 100, 3))

filtered_elements = [x for x in T1 if x % 3 != 0]

with open('filtered_elements.bin', 'wb') as f:
    pickle.dump(filtered_elements, f)

print('Дані записані в файл filtered_elements.bin')

import pickle

with open('filtered_elements.bin', 'rb') as f:
    filtered_elements = pickle.load(f)

print('Элементи кортежу, які не діляться на 3:')
print(filtered_elements)

