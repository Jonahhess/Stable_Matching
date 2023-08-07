#-----------------------------------------------------------------------
# randomqueue.py
#-----------------------------------------------------------------------

import random

#-----------------------------------------------------------------------

# A RandomQueue object is a collection whose items are in random order.

class RandomQueue:

    #-------------------------------------------------------------------

    # Construct an empty RandomQueue object.

    def __init__(self):
        self._a = []  # Items

    #-------------------------------------------------------------------

    # Return True if self is empty, and False otherwise.

    def isEmpty(self):
        return len(self._a) == 0

    #-------------------------------------------------------------------

    # Add item to self.

    def put(self, item):
        self._a += [item]

    #-------------------------------------------------------------------

    # Remove and return a random item of self.

    def get(self):
        length = len(self._a)
        r = random.uniformInt(0, length)
        # Swap self._a[length-1] and self._a[r].
        self._a[length-1], self._a[r] = self._a[r], self._a[length-1]
        return self._a.pop()

    #-------------------------------------------------------------------

    # Return a random item of self.

    def sample(self):
        length = len(self._a)
        r = random.uniformInt(0, length)
        return self._a[r]

    #-------------------------------------------------------------------

    # Return the number of items in self.

    def __len__(self):
        return len(self._a)

    #-------------------------------------------------------------------

    # Return a string representation of self.

    def __str__(self):
        a = self._a[:]  # Make a copy
        random.shuffle(a)  # Shuffle it.
        s = ''
        for item in a:
            s += str(item) + ' '
        return s

#-----------------------------------------------------------------------

#-----------------------------------------------------------------------

# more tobe.txt 
# to be or not to - be - - that - - - is

# python randomqueue.py < tobe.txt 
# or not to that to be 

# python randomqueue.py < tobe.txt 
# not to be be or to 
