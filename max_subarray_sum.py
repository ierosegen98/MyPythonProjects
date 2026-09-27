"""Функция принимает список чисел и возвращает максимальную сумму подмассива и сам подмассив."""
def max_subarray_sum(nums: list) -> int:
    summ = 0
    max_subarray = []

    for i in range(len(nums)):
        for j in range (len(nums), 0, -1):
            if sum(nums[i:j]) > summ:
                summ = sum(nums[i:j])
                max_subarray = nums[i:j]
    return summ, f'(подмассив: {max_subarray})'


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(*max_subarray_sum(nums))
