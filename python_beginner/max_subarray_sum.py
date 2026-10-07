"""Функция принимает список чисел и возвращает максимальную сумму подмассива и сам подмассив."""
def max_subarray_sum(nums: list) -> tuple[int, list[int]]:
    if nums == []:
        return 0, []
    
    current_sum = min(nums)
    best_sum = min(nums)
    current_start = 0
    best_start = 0
    best_end = 0

    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            current_start = i
        else: 
            current_sum += nums[i] 
            if current_sum > best_sum: 
                best_sum = current_sum
                best_start = current_start
                best_end = i
        
    return best_sum, f'подмассив: {nums[best_start:best_end + 1]}'


nums = [-2,1,-3,4,-1,2,1,-5,4]
print(*max_subarray_sum(nums))
