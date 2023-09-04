def has_negatives(a):
    nums = {}
    result = []

    for num in a:
        # print(f'nums: {nums}')
        if (num) in nums:
            result.append(abs(num))
        else:
            nums[num * -1] = num

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
