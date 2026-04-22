marks = [35, 44, 57, 89, 80, 12, 4]
marks2 = [10, 12, 14, 3, 4, 2, 66]

# APPEND: Adds a single element to the end of the list
marks.append(23)
print(marks)

# COPY: Returns a shallow copy of the list (original list unchanged)
copy_marks = marks.copy()
print(copy_marks)

# COUNT: Returns how many times a value appears in the list
print(marks.count(89))

# EXTEND: Adds all elements of another list to the end
marks.extend(marks2)
print(marks)

# INDEX: Returns index of first occurrence of a value
print(f"The index of 89 in the list is: {marks.index(89)}")

# INSERT: Inserts element at a specific index
marks.insert(4, 'Sanchal')
print(marks)

# POP: Removes and returns element (default = last element)
removed_item = marks.pop()
print("Removed:", removed_item)
print(marks)

# REMOVE: Removes first occurrence of a value
marks.remove(44)
print(marks)

# SORT: Sorts list in ascending order (modifies original list)
marks2.sort()
print(marks2)

# REVERSE: Reverses the list order (in-place)
marks.reverse()
print(marks)

# CLEAR: Removes all elements from the list (makes it empty)
marks.clear()
print(marks)