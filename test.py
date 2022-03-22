from Convertor import Convertor

for num in range(0,1000):

    cnv = Convertor(num).convertAll()
    
    yen = 500 * int(cnv[0])
    yen += 100 * int(cnv[1]) 
    yen += 50 * int(cnv[2])
    yen += 10 * int(cnv[3])
    yen += 5 * int(cnv[4])
    yen += 1 * int(cnv[5])

    if (num == yen):
        print(num, ' : ○')
    else:
        print(num, ' : ', yen)
