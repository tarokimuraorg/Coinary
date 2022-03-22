class Convertor:

    __str_yen = '0'

    def __init__(self, yen : int) -> None:
        
        if (yen > 999 or yen < 0):
            return None

        self.__str_yen = str(yen)

    def intToCoinary(self) -> str:

        if (self.__str_yen == '0'):
            return '000000'

        result = self.__convert500Yen()
        result += self.__convert100Yen()
        result += self.__convert50Yen()
        result += self.__convert10Yen()
        result += self.__convert5Yen()
        result += self.__convert1Yen()

        return result

    def __convert1Yen(self) -> str:
    
        if (len(self.__str_yen) > 0):

            extracted_number = self.__str_yen[-1]

            if (extracted_number == '9' or extracted_number == '4'):
                return '4'
        
            if (extracted_number == '8' or extracted_number == '3'):
                return '3'
        
            if (extracted_number == '7' or extracted_number == '2'):
                return '2'
        
            if (extracted_number == '6' or extracted_number == '1'):
                return '1'

        return '0'

    def __convert5Yen(self) -> str:

        if (len(self.__str_yen) > 0):

            extracted_number = self.__str_yen[-1]

            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'

    def __convert10Yen(self) -> str:
    
        if (len(self.__str_yen) > 1):

            extracted_number = self.__str_yen[-2]

            if (extracted_number == '9' or extracted_number == '4'):
                return '4'
        
            if (extracted_number == '8' or extracted_number == '3'):
                return '3'
        
            if (extracted_number == '7' or extracted_number == '2'):
                return '2'
        
            if (extracted_number == '6' or extracted_number == '1'):
                return '1'

        return '0'

    def __convert50Yen(self) -> str:

        if (len(self.__str_yen) > 1):

            extracted_number = self.__str_yen[-2]
    
            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'

    def __convert100Yen(self) -> str:

        if (len(self.__str_yen) > 2):
        
            extracted_number = self.__str_yen[-3]

            if (extracted_number == '9' or extracted_number == '4'):
                return '4'
        
            if (extracted_number == '8' or extracted_number == '3'):
                return '3'
        
            if (extracted_number == '7' or extracted_number == '2'):
                return '2'
        
            if (extracted_number == '6' or extracted_number == '1'):
                return '1'

        return '0'
    
    def __convert500Yen(self) -> str:

        if (len(self.__str_yen) > 2):
        
            extracted_number = self.__str_yen[-3]

            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'
