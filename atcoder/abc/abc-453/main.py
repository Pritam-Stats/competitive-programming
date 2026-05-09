class Solution:
    def minOperations(self, nums: list[int]) -> int:
        def isPrime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for d in range(2, int(num**(0.5))+1):
                if num % d == 0:
                    return False
            return True

        n = len(nums)
        cnt = 0
        for i in range(0, n, 2):
            while not isPrime(nums[i]):
                nums[i] += 1
                cnt += 1

        for i in range(1, n, 2):
            while isPrime(nums[i]):
                nums[i] += 1
                cnt += 1
        return cnt


s = Solution()
print(s.minOperations([1,2,3,4]))