import json

with open("data.json",'r', encoding='utf8') as words:
    valueDict = json.load(words)

class NumberToWord():
    def getPositionValue(self,number):
        listOfNumbers = []
        while number != 0:
            listOfNumbers.append(number % 10)
            number = number // 10
        return listOfNumbers

    def getTensDigitValue(self,number,numberList, digits):
        for i in range(0,digits+1):
            divident = 10*10
        tensDigitNumber = int(number%divident)
        if tensDigitNumber == 0:
            return ""
        else:
            return valueDict[str(tensDigitNumber)]

    def getHundredDigitValue(self,number,numberList, digits):
        hundredCheck = numberList[0:3]
        hundredCheck.reverse()
        hundred = int("".join(map(str,hundredCheck)))
        if hundred == 100:
            value = valueDict[str(hundred)]
        elif digits == 3:
            numberList = self.getPositionValue(number)
            tensDigitNumber = number//10
            if numberList[2] == 0:
                value = self.getTensDigitValue(number,numberList, digits)
            else:
                value = valueDict[str(numberList[2])]+"शे"+" "+self.getTensDigitValue(number,numberList, digits)
        else:
            if numberList[2] == 0:
                value = self.getTensDigitValue(number,numberList, digits)
            else:
                value = valueDict[str(numberList[2])]+"शे"+" "+self.getTensDigitValue(number,numberList, digits)
        return value

    def getThousandDigitValue(self, number,numberList, digits):
        if digits == 4:
            if numberList[3] == 0:
                value  = self.getHundredDigitValue(number,numberList[0:3],4)
            else:
                value = valueDict[str(numberList[3])]+" हजार " + self.getHundredDigitValue(number,numberList[0:3],4)
        elif digits == 5:
            thousandsDigit = number//1000
            if thousandsDigit == 0:
                value = self.getHundredDigitValue(number,numberList[0:3],5)
            else:
                value = valueDict[str(thousandsDigit)]+" हजार " + self.getHundredDigitValue(number,numberList[0:3],5)
        return value


    def getMillionDigitValue(self,number,numberList, digits):
        if digits == 6:
            if numberList[5] == 0:
                value = self.getThousandDigitValue(number%100000,numberList, 5)
            else:
                    value = valueDict[str(numberList[5])]+" लाख " + self.getThousandDigitValue(number%100000,numberList, 5)
        elif digits == 7:
            # thousandDigitValue = self.getThousandDigitValue(number%100000,numberList, 5)
            lakhsDigit = number//100000
            if lakhsDigit == 0:
                value = self.getThousandDigitValue(number%100000,numberList, 5)
            else:
                if numberList[4] == 0:
                    millionDigitNumber = number // 100000
                    value = valueDict[str(millionDigitNumber)]+" लाख " + self.getThousandDigitValue(number%100000,numberList,4)
                else:
                    value = valueDict[str(lakhsDigit)]+" लाख " + self.getThousandDigitValue(number%100000,numberList, 5)
        return value

    def getValue(self,number):
        number = str(number)
        beforeDecimal = number.split(".")
        noOfDigits = len(str(beforeDecimal[0]))
        number = int(float(number))
        numberList = self.getPositionValue(number)
        if len(numberList) == 1:
            value = valueDict[str(number)]

        if len(numberList) == 2:
            value = valueDict[str(number)]

        if len(numberList) == 3:
            value = self.getHundredDigitValue(number,numberList, 3)

        if len(numberList) == 4:
            value = self.getThousandDigitValue(number,numberList, 4)

        if len(numberList) == 5:
            value = self.getThousandDigitValue(number,numberList, 5)

        if len(numberList) == 6:
            value = self.getMillionDigitValue(number,numberList, 6)

        if len(numberList) == 7:
            value = self.getMillionDigitValue(number,numberList, 7)

        if len(numberList) == 8:
            value = valueDict[str(numberList[7])]+" कोटी " + self.getMillionDigitValue(number%10000000,numberList, 7)

        if len(numberList) == 9:
            if numberList[6] == 0:
                millionDigitNumber = number//10000000
                value = valueDict[str(millionDigitNumber)]+" कोटी " + self.getMillionDigitValue(number%10000000,numberList, 6)
            else:
                thousandDigitValue = self.getMillionDigitValue(number%10000000,numberList, 7)
                millionsDigit = number // 10000000
                value = valueDict[str(millionsDigit)] +" कोटी " + thousandDigitValue

        value = value + " रुपये "
        try:
            if len(beforeDecimal) > 0 and int(beforeDecimal[1]) != 0:
                afterDecimalNumber = beforeDecimal[1][0:2]
                number = int(float(afterDecimalNumber))
                value= value + valueDict[str(number)] + " पैसे"
                return value
        except:
            return value
