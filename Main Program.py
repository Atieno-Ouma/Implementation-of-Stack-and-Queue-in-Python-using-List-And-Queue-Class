class Queue:
    def __init__(self,length=10):
        self.length=length
        self.q_items=list()
    def lenq(self):
        return len(self.q_items)

    def is_empty(self):
        return self.q_items==[]

    def is_full(self):
        return len(self.q_items)==self.length

    def push(self,item):
        if not self.is_full():
            self.q_items=self.q_items+[item]
        else:
            return self.q_items

    def pop(self):
        if not self.is_empty():
            ele=self.q_items[0]
            del self.q_items[0]
            return ele
        else:
            pass

    def pop_index(self,index):
        x=self.q_items[index]
        del self.q_items[index]
        return x

    def push_index(self,index,elem):
        self.q_items.insert(index,elem)
        return self.q_items



    def peek(self):
        return self.q_items[-1]

    def q_sort(self):
        n = len (self.q_items)
        for i in range (0, n - 1):
            flag = 0
            for j in range (0, n - 1 - i):
                if self.q_items[j] > self.q_items[j + 1]:
                    temp = self.q_items[j]
                    self.q_items[j] = self.q_items[j + 1]
                    self.q_items[j + 1] = temp
                    flag = 1
            if flag == 0:
                break
        return self.q_items

    def display(self):
        print(self.q_items)

class Stack:
    def __init__(self, maxsize=10):
        self.maxsize = maxsize
        self.items = list()

    def is_Empty(self):
        if len (self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if not self.is_Full():
            self.items.append(item)

    def pop(self):
        if not self.is_Empty ():
            return self.items.pop ()
        else:
            print ("err: the stack is already empty")

    def is_Full(self):
        return len(self.items)==self.maxsize

    def display(self):
        print (self.items)


class Q_Stack:
    def __init__(self):
        self.queue=Queue()

    def is_empty(self):
        self.queue.is_empty()

    def is_full(self):
        return self.queue.is_full()

    def pop(self):
        x=self.queue.pop_index((self.queue.lenq())-1)
        return x

    def push(self,item):
        self.queue.push(item)

    def display(self):
        self.queue.display()


queue=Queue()
queue.display()
queue.push(3)
queue.display()
queue.push(2)
queue.display()
queue.push(4)
queue.display()
queue.push(7)
queue.display()
queue.push(1)
queue.display()
print("queue")
queue.display()
queue.pop()
queue.display()
queue.pop()
queue.display()
print("sorted queue")
queue.q_sort()
queue.display()
print("9 insrted in queue")
queue.push(9)
queue.display()
print("pop is called on queue")
print(queue.pop())
print("stack with list")
stack=Stack()
stack.push(3)
stack.push(2)
stack.push(4)
stack.push(7)
stack.push(1)
stack.display()
print("stack with queue")
stack1=Q_Stack()
stack1.push(3)
stack1.display()
stack1.push(2)
stack1.display()
stack1.push(4)
stack1.display()
stack1.push(7)
stack1.display()
stack1.push(1)
stack1.display()
