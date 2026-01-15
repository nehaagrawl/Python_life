# class ShoppingList:
#     def __init__(self):
#         self.items = []

#     def add_item(self, item):
#         self.items.append(item)
#         print(f"Added: {item}")

#     def remove_item(self, item):
#         if item in self.items:
#             self.items.remove(item)
#             print(f"Removed: {item}")
#         else:
#             print(f"{item} not found in the list")

#     def display_list(self):
#         if self.items:
#             print("Shopping List:")
#             for i, item in enumerate(self.items, 1):
#                 print(f"{i}. {item}")
#         else:
#             print("Shopping list is empty")

#     def clear_list(self):
#         self.items = []
#         print("Shopping list cleared")

# # Example usage
# shopping_list = ShoppingList()
# shopping_list.add_item("tops")
# shopping_list.add_item("chocolates")
# shopping_list.add_item("gold 1kg")
# shopping_list.display_list()
# shopping_list.remove_item("gold 1kg")
# shopping_list.display_list()

# # Detailed examples of Python list methods
# print("\n" + "="*50)
# print("Detailed Examples of Python List Methods")
# print("="*50)

# # 1. append() - Adds an element to the end of the list
# my_list = [1, 2, 3]
# print(f"Original list: {my_list}")
# my_list.append(4)
# print(f"After append(4): {my_list}")

# # 2. extend() - Adds all elements of an iterable to the end
# my_list.extend([5, 6])
# print(f"After extend([5, 6]): {my_list}")

# # 3. insert() - Inserts an element at a specific position
# my_list.insert(2, 'inserted')
# print(f"After insert(2, 'inserted'): {my_list}")

# # 4. remove() - Removes the first occurrence of a value
# my_list.remove('inserted')
# print(f"After remove('inserted'): {my_list}")

# # 5. pop() - Removes and returns the element at a specific index (default last)
# popped = my_list.pop()
# print(f"After pop(): {my_list}, popped element: {popped}")

# popped = my_list.pop(0)
# print(f"After pop(0): {my_list}, popped element: {popped}")

# # 6. index() - Returns the index of the first occurrence of a value
# my_list = ['a', 'b', 'c', 'b']
# index_b = my_list.index('b')
# print(f"Index of 'b': {index_b}")

# # 7. count() - Returns the number of occurrences of a value
# count_b = my_list.count('b')
# print(f"Count of 'b': {count_b}")

# # 8. sort() - Sorts the list in place
# unsorted = [3, 1, 4, 1, 5]
# unsorted.sort()
# print(f"After sort(): {unsorted}")

# # 9. reverse() - Reverses the list in place
# unsorted.reverse()
# print(f"After reverse(): {unsorted}")

# # 10. copy() - Returns a shallow copy of the list
# original = [1, 2, [3, 4]]
# copied = original.copy()
# print(f"Original: {original}, Copied: {copied}")

# # 11. clear() - Removes all elements from the list
# copied.clear()
# print(f"After clear(): {copied}")

# # 12. len() - Built-in function to get length
# print(f"Length of my_list: {len(my_list)}")

# # 13. List comprehension example
# squares = [x**2 for x in range(5)]
# print(f"List comprehension - squares: {squares}")

# # 14. Slicing
# numbers = [0, 1, 2, 3, 4, 5]
# print(f"Original: {numbers}")
# print(f"Slice [1:4]: {numbers[1:4]}")
# print(f"Slice [::2]: {numbers[::2]}")  # Every other element


class Shopping_list:
    def __init__(self):
        self.items=[]    
    def add_items(self,item):
        self.items.append(item)
        print("item added:",item)


    def remove_item(self,item):
        if item in self.items:
            self.items.remove(item)
            print(f"{item} is removed")
        else:
            print(f"{item} is not in the list")




    def display_list(self):
        for i in self.items:
            print(i)

sl=Shopping_list()

sl.add_items("gold")
sl.add_items("silver")
sl.add_items("platinum")
sl.display_list()


            


