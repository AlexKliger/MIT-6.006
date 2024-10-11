class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        #Construct new doubly linked list storing x
        new_head = Doubly_Linked_List_Node(x)
        # If no head exists, then the list is empty
        if self.head == None:
            # Link head and tail pointers
            self.head = new_head
            self.tail = new_head
            return
        # Link next new head's next pointer to old head
        new_head.next = self.head
        # Link old head's prev pointer to new head
        self.head.prev = new_head
        # Link list's head pointer to new new head
        self.head = new_head

    def insert_last(self, x):
        # Construct a new doubly linked list node storing x
        new_tail = Doubly_Linked_List_Node(x)
        # If no tail exists, then the list is empty
        if self.tail == None:
            # Link head and tail pointers
            self.head = new_tail
            self.tail = new_tail
            return
        # Link new tail's prev pointer to old tail
        new_tail.prev = self.tail
        # Link old tail's next pointer to new tail
        self.tail.next = new_tail
        # Link list's tail node to new tail
        self.tail = new_tail

    def delete_first(self):
        # Extract list's old head
        x = self.head
        # Link list's head pointer to old head's next pointer
        self.head = x.next
        # If new head points to None, the list only had a length of 1
        if self.head == None:
            # Set list's tail to None too
            self.tail = None
        else:
            # Set new head's prev pointer to None
            self.head.prev = None

        return x.item

    def delete_last(self):
        # Extract list's old tail
        x = self.tail
        # Link list's tail pointer to old tail's prev pointer
        self.tail = x.prev
        # If old tail's prev value is None, then the list only had a length of 1
        if self.tail == None:
            # Set list's head pointer to None too
            self.head = None
        else:
            # ELse set new tail's next pointer to None
            self.tail.next = None

        return x.item

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        ###########################
        # Part (b): Implement me! # 
        ###########################
        return L2

    def splice(self, x, L2):
        ###########################
        # Part (c): Implement me! # 
        ###########################
        pass
