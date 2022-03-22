from Convertor import Convertor

for num in range(0,1000):

    cvt = Convertor(num).intToCoinary()
    
    yen = 500 * int(cvt[0])
    yen += 100 * int(cvt[1]) 
    yen += 50 * int(cvt[2])
    yen += 10 * int(cvt[3])
    yen += 5 * int(cvt[4])
    yen += 1 * int(cvt[5])

    if (num == yen):
        print(num, ' : ○')
    else:
        print(num, ' : ', yen)
