def find_outlier(integers):
    even_nums = [i for i in integers if i % 2 == 0]
    return even_nums[0] if len(even_nums) == 1 else list(set(integers)-set(even_nums))[0]

