from time import time
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

def LIS(a):
    dmp = 1
    for i in range(len(a)):
        dmp = max(dmp, brute(a,i))
    return dmp

def main():
    global perbandingan
    print("==================BRUTE FORCE========================\n")
    n = int(input("Banyakan masukkan angka yang akan dimasukkan: "))
    List = list(map(int,input("Masukkan Angkanya :").strip().split()))[:n] 
    Stime = time()
    print("Maksimum LIS:", LIS(List))
    print("Total Perbandingan:",perbandingan)
    print("--- %s\tseconds ---" % '{0:.16f}'.format(time() - Stime))


main()
