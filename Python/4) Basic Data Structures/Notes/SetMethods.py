# <Method>	                             <Shortcut>     	                <Description>
# add()	 	                                                                Adds an element to the set
# clear()	 	                                                            Removes all the elements from the set
# copy()	 	                                                            Returns a copy of the set
# difference()		                         -                              Returns a set containing the difference between two or more sets
# difference_update()		                 -=                             Removes the items in this set that are also included in another, specified set
# discard()	 	                                                            Remove the specified item
# intersection()		                     &                              Returns a set, that is the intersection of two other sets
# intersection_update()		                 &=                             Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	                                                        Returns whether two sets have a intersection or not
# issubset()		                         <=                             Returns whether another set contains this set or not
#  		                                     <                              Returns whether all items in this set is present in other, specified set(s)
# issuperset()		                         >=                             Returns whether this set contains another set or not
#  		                                     >                              Returns whether all items in other, specified set(s) is present in this set
# pop()	 	                                                                Removes an element from the set
# remove()	 	                                                            Removes the specified element
# symmetric_difference()		             ^                              Returns a set with the symmetric differences of two sets
# symmetric_difference_update()		         ^=                             Inserts the symmetric differences from this set and another
# union()		                             |                              Return a set containing the union of sets
# update()		                             |=                             Update the set with the union of this set and others

# Create two sets for demonstration
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {8, 9, 10}

# 1. add() - Adds an element to the set
set1.add(6)
print("After add():", set1)  # Output: {1, 2, 3, 4, 5, 6}

# 2. clear() - Removes all the elements from the set
set1.clear()
print("After clear():", set1)  # Output: set()

# 3. copy() - Returns a copy of the set
set1 = {1, 2, 3,4}
set_copy = set1.copy()
print("After copy():", set_copy)  # Output: {1, 2, 3}

# 4. difference() - Returns the difference between two sets
difference_set = set2.difference(set1)
print("After difference():", difference_set)  # Output: {4, 5, 6, 7, 8}

# 5. difference_update() - Removes items in this set that are also in another set
set2.difference_update(set1)
print("After difference_update():", set2)  # Output: {4, 5, 6, 7, 8}

# 6. discard() - Removes the specified item (no error if item doesn't exist)
set2.discard(7)
print("After discard(7):", set2)  # Output: {4, 5, 6, 8}

# 7. intersection() - Returns the intersection of two sets
intersection_set = set1.intersection(set2)
print("After intersection():", intersection_set)  # Output: set()

# 8. intersection_update() - Removes items not in the intersection
set2.intersection_update(set1)
print("After intersection_update():", set2)  # Output: set()

# 9. isdisjoint() - Returns True if two sets have no intersection
is_disjoint = set1.isdisjoint(set2)
print("After isdisjoint():", is_disjoint)  # Output: True

# 10. issubset() - Returns True if set1 is a subset of set2
is_subset = set1.issubset(set2)
print("After issubset():", is_subset)  # Output: False

# 11. < (Subset check using the '<' operator)
is_proper_subset = set1 < set2
print("After < (Proper subset check):", is_proper_subset)  # Output: False

# 12. issuperset() - Returns True if set1 is a superset of set2
is_superset = set1.issuperset(set2)
print("After issuperset():", is_superset)  # Output: False

# 13. > (Superset check using the '>' operator)
is_proper_superset = set1 > set2
print("After > (Proper superset check):", is_proper_superset)  # Output: False

# 14. pop() - Removes an arbitrary element from the set
set1 = {1, 2, 3}
popped_element = set1.pop()
print("After pop():", set1, "Popped Element:", popped_element)  # Output: {2, 3} and popped element will be 1

# 15. remove() - Removes the specified element (raises an error if element doesn't exist)
set1.remove(2)
print("After remove(2):", set1)  # Output: {3}

# 16. symmetric_difference() - Returns the symmetric difference of two sets
sym_diff_set = set2.symmetric_difference(set3)
print("After symmetric_difference():", sym_diff_set)  # Output: {6, 7, 9, 10}

# 17. symmetric_difference_update() - Updates the set with the symmetric difference
set2.symmetric_difference_update(set3)
print("After symmetric_difference_update():", set2)  # Output: {6, 7, 9, 10}

# 18. union() - Returns the union of two sets
union_set = set1.union(set2)
print("After union():", union_set)  # Output: {3, 6, 7, 9, 10}

# 19. update() - Updates the set with the union of this set and others
set1.update(set3)
print("After update():", set1)  # Output: {3, 9, 10}
