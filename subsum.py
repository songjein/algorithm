'''
def subarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    total = 0
    buf = {}
    for i, n in enumerate(nums):
        total += n
        buf[total] = True 

    cnt = 0
    for key in buf.keys():
        diff = key - k
        if (diff == 0) or (diff in buf):
            cnt += 1

    return cnt
'''

'''
def subarraySum(nums, k):
    total = 0
    cnt = 0
    buf = {0: True}
    for i, n in enumerate(nums):
        total += n
        if total - k in buf:
            cnt += 1
        buf[total] = True 

    return cnt
'''

def subarraySum(nums, k):
    total = 0
    cnt = 0
    buf = {0: 1}
    for i, n in enumerate(nums):
        total += n
        if total - k in buf:
            cnt += buf[total - k] 
        buf[total] = buf[total] + 1 if (total in buf) else 1
    return cnt

print (subarraySum([1, 1, 1], 2))
print (subarraySum([1], 0))
print (subarraySum([-1, -1, 1], 0))
print (subarraySum([1,2,3,4], 3))
print (subarraySum([-1,1,1,-1,2,-3,4,1], 2))
print (subarraySum([0,0,0,0,0,0,0,0,0,0], 0))
