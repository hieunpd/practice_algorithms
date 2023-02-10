def maxSubArraySum(array,N):
        ##Your code here
        max_sum = current_sum = array[0]
        for num in array[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    n = len(arr)
    print(maxSubArraySum(arr, n))