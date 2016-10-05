from collections import deque

class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = deque(list())


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        tmp = []
        for i in xrange(len(self.queue) - 1):
            tmp.append(self.queue.popleft())

        self.queue.popleft() # remove the last one

        for i in tmp:
            self.queue.append(i)


    def top(self):
        """
        :rtype: int
        """
        return self.queue[len(self.queue)-1]


    def empty(self):
        """
        :rtype: bool
        """
        if 0 == len(self.queue):
            return True
        else:
            return False

def main():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    print stack.top()


if __name__ == '__main__':
    main()