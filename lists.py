guests = ["andy", "bob", "carl", "dave"]
print(guests)

guests.append("bill")
print(guests)

guests.pop()
print(guests)

nums = [2,7,11,15]
target = 9

def twoSum(self, nums, target):
    for i in range(nums.size()):
        smaller_than = []
        if nums[i] <= target:
            smaller_than.append(nums[i])