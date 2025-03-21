def count_beautiful_subsets(nums, k):
    def is_beautiful(subset):
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if abs(subset[i] - subset[j]) == k:
                    return False
        return True
    def generate_subsets(index, current_subset):
        nonlocal count
        if index == len(nums):
            if current_subset and is_beautiful(current_subset):
                count += 1
            return

        generate_subsets(index + 1, current_subset)
        current_subset.append(nums[index])
        generate_subsets(index + 1, current_subset)
        current_subset.pop()

    count = 0
    generate_subsets(0, [])
    return count

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(count_beautiful_subsets(nums, k))