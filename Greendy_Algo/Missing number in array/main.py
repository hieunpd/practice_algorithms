def MissingNumber(array,N):
        return (N * (N + 1) // 2) - sum(array)

if __name__ == "__main__":
    arr = [1, 2, 3, 5, 6]
    n = len(arr) +1
    print(MissingNumber(arr, n))