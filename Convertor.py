class Convertor:

    __str_yen = '0'

    def __init__(self, yen) -> None:
        
        if (yen > 999 or yen < 0):
            return None

        self.__str_yen = str(yen)

    def convertAll(self) -> str:

        if (self.__str_yen == '0'):
            return '000000'

        result = self.convert500Yen()
        result += self.convert100Yen()
        result += self.convert50Yen()
        result += self.convert10Yen()
        result += self.convert5Yen()
        result += self.convert1Yen()

        return result

    def convert1Yen(self) -> str:
    
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

    def convert5Yen(self) -> str:

        if (len(self.__str_yen) > 0):

            extracted_number = self.__str_yen[-1]

            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'

    def convert10Yen(self) -> str:
    
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

    def convert50Yen(self) -> str:

        if (len(self.__str_yen) > 1):

            extracted_number = self.__str_yen[-2]
    
            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'

    def convert100Yen(self) -> str:

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
    
    def convert500Yen(self) -> str:

        if (len(self.__str_yen) > 2):
        
            extracted_number = self.__str_yen[-3]

            if (extracted_number == '9' or \
                extracted_number == '8' or \
                extracted_number == '7' or \
                extracted_number == '6' or \
                extracted_number == '5'):

                return '1'

        return '0'
