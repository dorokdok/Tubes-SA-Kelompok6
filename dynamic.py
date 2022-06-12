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
    list = []
    while (inputan != -1):
        inputan = int(input("Masukkan angka yang akan dimasukkan kedalam list (berhenti = -1): "))
        list.append(inputan)
    print("Maksimum LIS:", LISwithDP(list))
    print("Total Perbandingan:",perbandingan)

main()
