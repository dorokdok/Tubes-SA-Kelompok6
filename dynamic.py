perbandingan = 0
def LISwithDP(a):
    global perbandingan
    dmp = [1] * len(a)
    for i in range(1,len(a)):
        for j in range(i):
            if a[j] < a[i]:
                dmp[i] = max(dmp[i], dmp[j] + 1)
                perbandingan += 1
    return max(dmp)

def main():
    global perbandingan
    list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    print("Maksimum LIS:", LISwithDP(list))
    print("Total Perbandingan:",perbandingan)

main()