'''
Story
Ben has a very simple idea to make some profit: he buys something and sells it again. Of course, this wouldn't give him any profit at all if he was simply to buy and sell it at the same price. Instead, he's going to buy it for the lowest possible price and sell it at the highest.

Task
Write a function that returns both the minimum and maximum number of the given list/array.
'''


def min_max(lst):
    least = 10000000000000000
    max = 0
    for i in lst:
        if i <= least:
            least = i
    for i in lst:
        if i >= max:
            max = i
    combine = []
    combine.append(least)
    combine.append(max)
    return combine
'''
def test(lst, res):
  Test.assert_equals(min_max(lst), res, "tested on " + str(lst));

Test.describe("min_max")
Test.it("should work for some examples")
test([1,2,3,4,5], [1,5])
test([2334454,5], [5, 2334454])

for i in range(0,20):
    r = randint(0,100)
    test([r], [r,r])
'''
