class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        self.length += 1

        if self.head == None:
            self.head = new_node
            return self

        cur = self.head
        while not (cur.next == None):
            cur = cur.next
        cur.next = new_node
        return self

    def prepend(self, value):
        new_node = Node(value)
        self.length += 1

        new_node.next = self.head
        self.head = new_node
        return self

    def insert(self, value, position):
        if position == self.length + 1:
            self.append(value)
            return self
        if position == 1:
            self.prepend(value)
            return self
        if position > self.length + 1 or position < 1:
            print('Invalid position')
            return self

        new_node = Node(value)
        cur = self.head
        count = 1
        while count < position - 1:
            cur = cur.next
            count += 1

        next = cur.next
        cur.next = new_node
        new_node.next = next
        self.length += 1
        print(self.length)
        return self

    def display(self):
        cur = self.head
        while not (cur == None):
            print(cur.value, end=", ")
            cur = cur.next
        print('')
        return self

    def get(self, position):
        if position == 1:
            print(self.head.value)
            return self
        if position > self.length or position < 1:
            print('Invalid position')
            return self

        cur = self.head
        count = 1
        while count < position:
            cur = cur.next
            count += 1
        return self

    def remove_from_front(self):
        self.head = self.head.next
        self.length -= 1
        return self
    
    def remove_from_end(self):
        cur = self.head
        while not (cur.next.next == None):
            cur = cur.next
        cur.next = None
        self.length -= 1
        return self
        
    def remove(self, position):
        if position == 1:
            self.head = self.head.next
            self.length -= 1
            return self
        if position > self.length or position < 1:
            print('Invalid position')
            return self

        cur = self.head
        count = 1
        while count < position - 1:
            cur = cur.next
            count += 1

        next = cur.next
        cur.next = next.next 
        self.length -= 1
        print(self.length)
        return self

list = LinkedList()

list.append('2').append('3').prepend('1').append('4').append('5').prepend('real_first').display().remove_from_end().display().remove_from_front().display().remove(2).display()

print(list.length)