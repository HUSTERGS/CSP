from sys import stdin

n = int(stdin.readline().strip())
nums = tuple(int(x) for x in stdin.readline().strip().split())
# 第一天价格的上界
bound = [0, ] * n
for i in range(2, n - 2):
    bound[i] = 3 * min(nums[i - 1], nums[i], nums[i + 1])
bound[0] = min(2 * nums[0], 3 * nums[1])
if n >= 3:
    bound[1] = min(2 * nums[0], 3 * nums[1], 3 * nums[2])
    bound[n - 2] = min(2 * nums[n - 1], 3 * nums[n - 2], 3 * nums[n - 3])
bound[n - 1] = min(2 * nums[n - 1], 3 * nums[n - 2])

result = [0, ] * n


def determine_i(i):
    global result
    if i == 0:
        for a0 in range(1, bound[0] + 1):
            result[0] = a0
            if determine_i(i + 1) is not None:
                return result
    elif i == 1:
        for bias in range(2):
            a1 = 2 * nums[0] + bias - result[0]
            result[1] = a1
            if a1 > bound[1]:
                return None
            if n == 2:
                return result
            if determine_i(i + 1) is not None:
                return result
        return None
    elif i == n - 1:
        for bias in range(2):
            an_1 = 2 * nums[n - 1] - result[n - 2] + bias
            result[n - 1] = an_1
            if an_1 > bound[n-1]:
                return None
            if 1 <= an_1 <= bound[n - 1]:
                if n >= 3 and (result[n - 3] + result[n - 2] + result[n - 1]) // 3 == nums[n - 2]:
                    return result
        return None

    else:
        for bias in range(3):
            ai = 3 * nums[i-1] - result[i - 1] - result[i - 2] + bias
            result[i] = ai
            if ai > bound[i]:
                return None
            if 1 <= ai <= bound[i] and determine_i(i + 1) is not None:
                return result
        return None


determine_i(0)
print(" ".join([str(x) for x in result]))
