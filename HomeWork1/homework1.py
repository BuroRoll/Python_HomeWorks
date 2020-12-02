import numpy

# Создание массива случайных значений и поиск максимального из них
arr = numpy.random.randint(0, 1000, 1000)
print(arr)
max_element = numpy.amax(arr)
print('Наибольший элемент массива случайных значений равен ' + str(max_element))
