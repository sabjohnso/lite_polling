import unittest

from lite_polling import While

class TestLitePolling(unittest.TestCase):
    class Counter(object):
        def __init__(self):
            self.__value = 0
        def increment(self):
            self.__value += 1
        @property
        def value(self):
            return self.__value

    def testSimple(self):
        counter = self.Counter()
        n = 25
        def incrementCounter():
            counter = counter+1
        While((lambda : counter.value < n),
              counter.increment)
        self.assertEqual(counter.value, n)


if __name__ == '__main__':
    unittest.main()
