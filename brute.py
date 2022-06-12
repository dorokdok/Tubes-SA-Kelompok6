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
    list = []
    while (inputan != -1):
        inputan = int(input("Masukkan angka yang akan dimasukkan kedalam list (berhenti = -1): "))
        list.append(inputan)
    print("Maksimum LIS:", LIS(list))
    print("Total Perbandingan:",perbandingan)


main()
