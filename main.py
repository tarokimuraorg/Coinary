# 500 * [0,1] + 100 * [0,1,2,3,4] + 50 * [0,1] + 10 * [0,1,2,3,4] + 5 * [0,1] + 1 * [0,1,2,3,4]
def convertor(yen : int) -> str:

    if (yen > 999 or yen < 0):
        return ''
    
    if (yen == 0):
        return '000000'

    str_yen = str(yen)

    result = convertor500(str_yen)
    result += convertor100(str_yen)
    result += convertor50(str_yen)
    result += convertor10(str_yen)
    result += convertor5(str_yen)
    result += convertor1(str_yen)

    return result
    
def convertor1(yen : str) -> str:
    
    len_yen = len(yen)
    p = len_yen - 1

    if (p > 0 or p == 0):

        extracted_number = yen[p]

        if (extracted_number == '9' or extracted_number == '4'):
            return '4'
        
        if (extracted_number == '8' or extracted_number == '3'):
            return '3'
        
        if (extracted_number == '7' or extracted_number == '2'):
            return '2'
        
        if (extracted_number == '6' or extracted_number == '1'):
            return '1'

    return '0'

def convertor5(yen : str) -> str:

    len_yen = len(yen)
    p = len_yen - 1

    if (p > 0 or p == 0):

        extracted_number = yen[p]

        if (extracted_number == '9' or \
            extracted_number == '8' or \
            extracted_number == '7' or \
            extracted_number == '6' or \
            extracted_number == '5'):

            return '1'

    return '0'

def convertor10(yen : str) -> str:
    
    len_yen = len(yen)
    p = len_yen - 2

    if (p > 0 or p == 0):

        extracted_number = yen[p]

        if (extracted_number == '9' or extracted_number == '4'):
            return '4'
        
        if (extracted_number == '8' or extracted_number == '3'):
            return '3'
        
        if (extracted_number == '7' or extracted_number == '2'):
            return '2'
        
        if (extracted_number == '6' or extracted_number == '1'):
            return '1'

    return '0'

def convertor50(yen : str) -> str:

    len_yen = len(yen)
    p = len_yen - 2

    if (p > 0 or p == 0):

        extracted_number = yen[p]
    
        if (extracted_number == '9' or \
            extracted_number == '8' or \
            extracted_number == '7' or \
            extracted_number == '6' or \
            extracted_number == '5'):

            return '1'

    return '0'

def convertor100(yen : str) -> str:

    if (len(yen) == 3):
        
        extracted_number = yen[0]

        if (extracted_number == '9' or extracted_number == '4'):
            return '4'
        
        if (extracted_number == '8' or extracted_number == '3'):
            return '3'
        
        if (extracted_number == '7' or extracted_number == '2'):
            return '2'
        
        if (extracted_number == '6' or extracted_number == '1'):
            return '1'

    return '0'
    
def convertor500(yen : str) -> str:

    if (len(yen) == 3):
        
        extracted_number = yen[0]

        if (extracted_number == '9' or \
            extracted_number == '8' or \
            extracted_number == '7' or \
            extracted_number == '6' or \
            extracted_number == '5'):

            return '1'

    return '0'

if __name__ == "__main__":
    print(convertor(11))
