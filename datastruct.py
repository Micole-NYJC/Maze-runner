############################### 72 chars ###############################


class Node:
    """
    Represents a node in a linkedlist.
    Arguments
    ---------
    - data
      The data encapsulated in the node.
    Attributes
    ----------
    - next: Node | None
      The next node in the linkedlist, or None if the node is the tail.
    Methods
    -------
    - get() -> data
      Return the data stored in the node.
    """

    def __init__(self, data):
        # Replace the line below with your code
        self._data = data
        self.next = None
    

    def __repr__(self) -> str:
        return f'Node({self.get()})'

    def get(self):
        """Return the data stored in the node.
        Arguments
        ---------
        None
        Return: data
        """
        return self._data


class LinkedList:
    """
    Represents a sequence of data items.

    Arguments
    ---------
    None

    Attributes
    ----------
    None

    Methods
    -------
    - length() -> int
    - get(index) -> item
    - insert(index, item) -> None
    - append(item) -> None
    - delete(index) -> None
    """

    def __init__(self):
        self._head = None

    def __repr__(self) -> str:
        return 'LinkedList()'

    def length(self) -> int:
        """Returns the number of nodes in the linkedlist.
        Arguments
        ---------
        None
        Return: int
        """
        # Replace the line below with your code
        count = 0
        curr = self._head
        while curr is not None:
          count += 1
          curr = curr.next
        return count

    def get(self, n: int) -> "item":
        """Returns item at n-th node.

        Arguments
        ---------
        - n: int
            sequence number of item to be retrieved.

        Returns: item

        Raises: IndexError if n > length
        """
    # Replace the line below with your code
        curr = self._head
        idx = 0
        while curr:
            if idx == n:
                return curr
            curr = curr.next
            idx += 1
        raise IndexError
        

    def insert(self, n: int, item) -> None:
      """Insert item into linkedlist at position n.
      insert at head -> n == 0
      append -> n == length
      Arguments
      ---------
      - n: int
        sequence number of item to be inserted.
      Returns: None
      Raises: IndexError if n > length
      """
      # Replace the line below with your code
      if n == 0:
        new_node = Node(item)
        new_node.next = head
      current = head
      for x in range(1, n-1):
        current = current.next
      
      if n > self.length():
        raise IndexError
      
      new_node = Node(item)
      new_node.next = current.next
      current.next = new_node

      return None
    

    def append(self, item) -> None:
        """Append item at the end of linkedlist.

        Arguments
        ---------
        - item
          The item to be appended.

        Returns: None
        """
        # Replace the line below with your code
        new_node = Node(item)
        if self._head is None:
            self._head = new_node
            return
        last_node = self._head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        current = self._head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def delete(self, n: int) -> None:
        """Delete n-th item from linkedlist.

        Arguments
        ---------
        - n: int
          sequence number of item to be retrieved.

        Returns: None

        Raises: IndexError if n > length
        """
        # Replace the line below with your code
        if self._head is None:
          raise IndexError

        # Delete head node
        if n == 0:
            self._head = self._head.next
            return

        curr = self._head
        for _ in range(n - 1):
            if curr.next is None:
                raise IndexError
            curr = curr.next

        if curr.next is None:
            raise IndexError

        curr.next = curr.next.next
        
        
       
    def contains(self, item) -> bool:
        """Checks whether an item is in the linkedlist and returns
        a boolean value to indicate the status of the search

        Arguments
        ---------
        - item
          The item to be searched for.

        Returns: True if item is found in the linkedlist,
        otherwise False
        """
        # Replace the line below with your code
        curr = self._head
        while curr != Node(item):
          if curr is None:
            return False
            break
          else:
            curr = curr.next
        return True

if __name__ == "__main__":
  llist = LinkedList()
  llist.append(3)
  llist.append(5)
  llist.append(4)
  llist.append(9)
  print(llist.contains(9))