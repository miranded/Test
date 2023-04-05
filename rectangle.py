# Author: Torin Perkins
# GitHub username: torin-perkins
# Date: 07-23-22
# Description: contains methods and classes for recursively defined linked list
class Node:
    """
    defines a node in a linked list
    """
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """
    defines a linked list
    """
    def __init__(self):
        self.__head = None

    def get_head(self):
        """
        :return: the node at the beginning of the linked list
        """
        return self.__head

    def add(self, val, iterations=0, current=None):
        """
        adds a value to the linked list recursively
        :param val: the value to be added
        :param iterations: default argument for iterations
        :param current: default argument for the current value
        :return: none
        """
        if self.__head is None:  # check if the linked list is empty
            self.__head = Node(val)  # assign the head as the value
        else:
            if iterations == 0:
                current = self.__head  # on the first iteration assign current as the head
            if current.next is not None:  # check that current exists
                current = current.next  # move to the next value
                return self.add(val, iterations + 1, current)  # iterate
            current.next = Node(val)  # base case reached

    def remove(self, val, iterations=0, current=None, previous=None):
        """
        removes a value from the linked list recursively
        :param val: the value to be removed
        :param iterations: default argument for iterations
        :param current: default argument for the current value
        :param previous: default argument for the previous value
        :return: none
        """
        if self.__head is None:  # check if the linked list is empty
            return
        if self.__head.data == val:  # check if the head is the value that needs tobe removed
            self.__head = self.__head.next
        else:
            if iterations == 0: # on the first iterations assign current as the head
                current = self.__head
            if current is not None and current.data != val:  # check if current exists and the data is not the value
                previous = current
                current = current.next
                return self.remove(val, iterations + 1, current, previous)  # iterate with new values
            if current is not None:  # base case reached
                previous.next = current.next

    def contains(self, val, iterations=0, current=None):
        """
        checks if a value is contained in the linked list recursively
        :param val: the value to be checked for
        :param iterations: default argument for the iterations
        :param current: default argument for the current value
        :return: Boolean of the status of the value within the linked list
        """
        if self.__head is None:  # check if the linked list is empty
            return
        else:
            if iterations == 0:  # on the first iteration assign current as th head
                current = self.__head
            if current is not None and current.data != val:  # check if current exists and is not equal to the value
                current = current.next
                return self.contains(val, iterations + 1, current)  # iterate with new values
            elif current is not None and current.data == val:  # check if current exists and is the value
                return True
            else:  # no value found
                return False

    def insert(self, val, pos, iterations=0, current=None):
        """
        inserts a value into the linked list recursively
        :param val: the value to be added
        :param pos: the position where it should be added
        :param iterations: defaults argument for the iterations
        :param current: default argument for the current value
        :return: none
        """
        if self.__head is None:  # check if the linked list is empty
            self.add(val)
            return
        if pos == 0:  # check if the desired position is 0
            temp = self.__head
            self.__head = Node(val)
            self.__head.next = temp
        else:
            if iterations == 0:
                current = self.__head  # on the first iteration assign current as the head
            if iterations < pos - 1:  # looping condition
                if current.next is None:  # check if end of list reached
                    current.next = Node(val)  # assign value and return
                    return
                current = current.next
                return self.insert(val, pos, iterations + 1, current)  # iterate with new values
            else:  # base case reached
                temp = current.next
                current.next = Node(val)
                current.next.next = temp

    def reverse(self, iterations=0, current=None, previous=None):
        """
        reverses the linked list recursively
        :param iterations: default argument for the iterations
        :param current: default argument for the current value
        :param previous: default argument for the previous value
        :return: none
        """
        if iterations == 0:  # on the first iterations assign current as the head, and previous as None
            previous = None
            current = self.__head
        if current is not None:  # check if current exists
            following = current.next
            current.next = previous
            previous = current
            current = following
            return self.reverse(iterations + 1, current, previous)  # iterate with new values for reversal
        else:  # base case reached
            self.__head = previous  # finish reverse

    def to_plain_list(self, iterations=0, current=None, result=None):
        """
        converts the linked list to a list recursively
        :param iterations: default argument for the iterations
        :param current: default argument for the current value
        :param result: default argument for the resulting list
        :return: a python list of the linked list
        """
        if iterations == 0:  # on the first iteration create result as an empty list and assign current as the head
            result = []
            current = self.__head
        if current is not None:  # check if current exists
            result.append(current.data)  # add to the list
            current = current.next
            return self.to_plain_list(iterations + 1, current, result)  # iterate with new values
        else:  # base case reached
            return result

    def display(self):
        """
        Prints out the values in the linked list
        """
        current = self.__head
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
