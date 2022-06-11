perbandingan = 0
def LISwithDP(a):
    global perbandingan
    dmp = []
    for i in range (len(a)):
        dmp.append(0)
    dmp[0] = 1
    for i in range(1,len(a)):
        for j in range(i-1):
            if a[j] < a[i]:
                dmp[i] = max(dmp[i], dmp[j] + 1)
                perbandingan += 1
    Max = max(dmp)
    return Max

def main():
    global perbandingan
    list = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    dmp = LISwithDP(list)
    print("Maksimum LIS:", dmp)
    print("Total Perbandingan:",perbandingan)

main()