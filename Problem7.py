def binary_search(first, last, number):
    mid = int((first + last) / 2)
    mid_sq = mid * mid
    if mid_sq == number:
        return mid
    temp = (mid + 1) * (mid + 1)
    if mid_sq < number < temp:
        return mid
    elif mid_sq > number:
        return binary_search(first, mid - 1, number)
    else:
        return binary_search(mid + 1, last, number)


def sqrt(number):
    if number is None:
        return None
    if number is 0:
        return 0
    last = int(number / 2) + 1
    return binary_search(1, last, number)


if __name__ == '__main__':
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")
    print("Pass" if (8 == sqrt(69)) else "Fail")

    # Test case 1
    print("Pass" if (-4 == sqrt(
        16)) else "Fail")  # Expected result is to print fail since we are covering only positive numbers

    # Test case 2
    print("Pass" if (5 == sqrt(
        18)) else "Fail")  # Expected result id to print fail since 18 would lead us to 4 as correct answer

    # Test Case 3
    print("Pass" if (5 == sqrt(None)) else "Fail")  # Expected result is to print fail since arguement passed is None
