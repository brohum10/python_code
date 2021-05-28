cars = ["Ford", "Volvo", "BMW"]


# 1  append() Adds an element at the end of the list
cars.append("Ford")
print(cars)
print("\n---\n")


# 2  clear() Removes all the elements from the list
cars.clear()
print(cars)
print("\n---\n")


# 3  copy() Returns a copy of the list
x  =  cars.copy()
print(x)
print("\n---\n")


# 4  count()	Returns the number of elements with the specified value
x = cars.count("Ford")
print(x)
print("\n---\n")


# 5 extend() Add the elements of a list (or any iterable), to the end of the current list
x = cars.extend("Ford")
print(x)
print("\n---\n")


#6   index() Returns the index of the first element with the specified value
x = cars.index("Ford")
print(x)
print("\n---\n")


#7  insert() Adds an element at the specified position
cars.insert(1, "Tesla")
print(cars)


# 8  pop() Removes the element at the specified position
cars.pop(0)
print(cars)
print("\n---\n")


# 9  remove() Removes the first item with the specified value
cars.remove("Ford")
print(cars)
print("\n---\n")


# 10 reverse() Reverses the order of the list
cars.reverse()
print(cars)
print("\n---\n")


# 11  sort() Sorts the list
cars.sort()
print(cars)
