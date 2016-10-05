class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        tmp = []
        for i in xrange(len(self.stack) - 1):
            tmp.append(self.stack.pop())

        self.stack.pop() # pop the last one

        for i in tmp[::-1]:
            self.stack.append(i)


    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]


    def empty(self):
        """
        :rtype: bool
        """
        if 0 == len(self.stack):
            return True
        else:
            return False



def main():

    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.pop()
    q.pop()
    print q.peek()


if __name__ == '__main__':
    main()