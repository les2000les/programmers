def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i, num in enumerate(nums):
        numbers = numbers.replace(num, str(i))
    answer = int(numbers)
    return answer