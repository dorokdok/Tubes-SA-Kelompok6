from time import time
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
    print("==================Dynamic Programming==================")
    n = int(input("Banyakan masukkan angka yang akan dimasukkan: "))
    List = list(map(int,input("Masukkan Angkanya: ").strip().split()))[:n]
    Stime = time()
    print("Maksimum LIS:", LISwithDP(List))
    print("Total Perbandingan:",perbandingan)
    print("--- %s\tseconds ---" % '{0:.16f}'.format(time() - Stime))

main()
