# Author: Prince Emmanuel
# GitHub username: emmanueposu
# Date: 7/21/2022
# Description: A Node class that is used by a LinkedList class, which has recursive implementations.
class Node:
    """
    represents a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    a linked list implementation of the list ADT
    """
    def __init__(self):
        self._head = None

    def get_head(self):
        """
        returns the first node in the list
        """
        return self._head

    def rec_add(self, val, current):
        """
        adds a node containing val to the linked list
        """
        if current.next is None:
            current.next = Node(val)
        else:
            return self.rec_add(val, current.next)

    def add(self, val):
        """
        calls rec_add function with the first node as the second parameter
        """
        if self._head is None:
            self._head = Node(val)
        else:
            return self.rec_add(val, self._head)

    def rec_remove(self, val, previous, current):
        """
        removes the node containing val from the linked list
        """
        if current.next is not None and current.data != val:
            previous = current
            current = current.next
            return self.rec_remove(val, previous, current)
        elif current is not None and current.data == val:
            previous.next = current.next

    def remove(self, val):
        """
        calls rec_remove function with the first node as the
        second and third parameter
        """
        if self._head is None:
            return
        if self._head.data == val:
            self._head = self._head.next
        else:
            return self.rec_remove(val, self._head, self._head)

    def rec_contains(self, key, current):
        """
        returns True if the list contains a Node with the value key,
        otherwise returns False
        """
        if current is not None and current.data != key:
            return self.rec_contains(key, current.next)
        elif current is not None and current.data == key:
            return True
        elif current is None:
            return False

    def contains(self, key):
        """
        calls rec_contains function with the first node as the second parameter
        """
        if self._head is None:
            return False
        else:
            return self.rec_contains(key, self._head)

    def rec_insert(self, val, pos, count, current):
        """
        inserts a node containing val into the linked list at position pos
        """
        if current.next is not None and pos != count:
            return self.rec_insert(val, pos, count+1, current.next)
        elif current.next is not None and pos == count:
            temp = current.next
            current.next = Node(val)
            current.next.next = temp
        elif current.next is None:
            current.next = Node(val)

    def insert(self, val, pos):
        """
        calls rec_insert function with one as the third parameter and the
        first mode as the fourth parameter
        """
        if self._head is None:
            self.add(val)
            return
        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            return self.rec_insert(val, pos, 1, self._head)

    def rec_reverse(self, previous, current):
        """
        reverses the linked list
        """
        if current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
            self._head = previous
            return self.rec_reverse(previous, current)

    def reverse(self):
        """
        calls rec_reverse function with None as the first parameter and
        the first node as the second parameter
        """
        return self.rec_reverse(None, self._head)

    def rec_to_plain_list(self, current):
        """
        returns a regular Python list containing the same values,
        in the same order, as the linked list
        """
        result = []
        if current is not None:
            result = [current.data] + self.rec_to_plain_list(current.next)
        return result

    def to_plain_list(self):
        """
        calls rec_to_plain_list function with the first node as a parameter
        """
        return self.rec_to_plain_list(self._head)

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self._head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

# testing code -- comment out before submitting
def main():
     my_list = LinkedList()
     my_list.add(13)
     my_list.add(9)
     my_list.add(81)
     my_list.add(7)
     my_list.display() # should be: 13 9 81 7
     my_list.remove(81)
     my_list.display() # should be: 13 9 7
     # print(my_list.contains(9))
      # print(my_list.contains(5))
     my_list.insert(0, 2) # should be: 13, 9, 7, 2
     my_list.display()
     my_list.reverse()
     # my_list.display() # should be: 7 9 3 13
     # print(my_list.to_plain_list()) # should be: [7, 9, 3, 13]


if __name__ == '__main__':
     main()


