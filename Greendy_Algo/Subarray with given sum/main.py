def subArraySum(arr, n, s): 
        # n = len(arr)
        start = 0
        end = 0
        sum = arr[0]
        while (end < n):
            if (sum == s):
                return [start + 1, end + 1]
            elif (sum < s):
                end += 1
                if (end < n):
                    sum += arr[end]
            else:
                sum -= arr[start]
                start += 1
        return [-1]

if __name__ == "__main__":
    arr = [1, 2, 3, 7, 5]
    n = len(arr)
    s = 12
    print(subArraySum(arr, n, s))