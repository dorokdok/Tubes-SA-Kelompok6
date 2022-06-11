perbandingan = 0

def brute(a, n):
    global perbandingan
    if n == 0 :
        return 1
    dmp = 1
    i = n - 1
    while i >= 0 :
        if a[i] < a[n]:
            dmp = max(dmp, 1 + brute(a, i))
            perbandingan += 1
        i -= 1
    return dmp

def LIS(a, N):
    dmp = 1
    for i in range(N):
        dmp = max(dmp, brute(a,i))
    return dmp

def main():
    global perbandingan
    list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    dmp = LIS(list, len(list))
    print("Maksimum LIS:", dmp)
    print("Total Perbandingan:",perbandingan)


main()