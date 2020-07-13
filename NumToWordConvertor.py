
valueDict  = {1:"एक", 2:"दोन", 3:"तीन", 4:"चार", 5:"पाच", 6:"सहा", 7: "सात", 8:"आठ", 9: "नऊ", 10:"दहा", 11:"अकरा", 12:"बारा", 13:"तेरा", 14:"चौदा", 15:"पंधरा", 16:"सोळा", 17:"सतरा", 18:"अठरा", 19:"एकोणीस", 20:"वीस",21:"एकवीस",22:"बावीस",
23:"तेवीस",24:"चोवीस",25:"पंचवीस",26:"सव्वीस",27:"सत्तावीस",28:"अठ्ठावीस",29:"एकोणतीस",30:"तीस",31:"एकतीस",32:"बत्तीस",33:"तेहेतीस",34:"चौतीस",35:"पस्तीस",36:"छत्तीस",37:"सदतीस",38:"अडतीस",39:"एकोणचाळीस",40:"चाळीस",41:"एक्केचाळीस",42:"बेचाळीस",43:"त्रेचाळीस",44:"चव्वेचाळीस",45:"पंचेचाळीस",46:"सेहेचाळीस",47:"सत्तेचाळीस",48:"अठ्ठेचाळीस",49:"एकोणपन्नास",50:"पन्नास",
51:"एक्कावन्न",52:"बावन्न",53:"त्रेपन्न",54:"चोपन्न",55:"पंचावन्न",56:"छप्पन्न",57:"सत्तावन्न",58:"अठ्ठावन्न",59:"एकोणसाठ",60:"साठ",61:"एकसष्ठ",62:"बासष्ठ",63:"त्रेसष्ठ",64:"चौसष्ठ",65:"पासष्ठ",66:"सहासष्ठ",67:"सदुसष्ठ",68:"अडुसष्ठ",69:"एकोणसत्तर",70:"सत्तर",
71:"एक्काहत्तर",72:"बाहत्तर",73:"त्र्याहत्तर",74:"चौर्‍याहत्तर",75:"पंच्याहत्तर",76:"शहात्तर",77:"सत्याहत्तर",78:"अठ्ठ्याहत्तर",79:"एकोणऐंशी",80:"ऐंशी",81:"एक्क्याऐंशी",82:"ब्याऐंशी",83:"त्र्याऐंशी",84:"चौऱ्याऐंशी",85:"पंच्याऐंशी",86:"शहाऐंशी",87:"सत्त्याऐंशी",88:"अठ्ठ्याऐंशी",89:"एकोणनव्वद",90:"नव्वद",91:"एक्क्याण्णव",92:"ब्याण्णव",93:"त्र्याण्णव",94:"चौऱ्याण्णव",95:"पंच्याण्णव",96:"शहाण्णव",97:"सत्त्याण्णव",98:"अठ्ठ्याण्णव",99:"नव्व्याण्णव",100:"शंभर"}

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
            return valueDict[tensDigitNumber]

    def getHundredDigitValue(self,number,numberList, digits):
        hundredCheck = numberList[0:3]
        hundredCheck.reverse()
        hundred = int("".join(map(str,hundredCheck)))
        if hundred == 100:
            value = valueDict[hundred]
        elif digits == 3:
            numberList = self.getPositionValue(number)
            tensDigitNumber = number//10
            if numberList[2] == 0:
                value = self.getTensDigitValue(number,numberList, digits)
            else:
                value = valueDict[numberList[2]]+"शे"+" "+self.getTensDigitValue(number,numberList, digits)
        else:
            if numberList[2] == 0:
                value = self.getTensDigitValue(number,numberList, digits)
            else:
                value = valueDict[numberList[2]]+"शे"+" "+self.getTensDigitValue(number,numberList, digits)
        return value

    def getThousandDigitValue(self, number,numberList, digits):
        if digits == 4:
            if numberList[3] == 0:
                value  = self.getHundredDigitValue(number,numberList[0:3],4)
            else:
                value = valueDict[numberList[3]]+" हजार " + self.getHundredDigitValue(number,numberList[0:3],4)
        elif digits == 5:
            thousandsDigit = number//1000
            if thousandsDigit == 0:
                value = self.getHundredDigitValue(number,numberList[0:3],5)
            else:
                value = valueDict[thousandsDigit]+" हजार " + self.getHundredDigitValue(number,numberList[0:3],5)
        return value


    def getMillionDigitValue(self,number,numberList, digits):
        if digits == 6:
            if numberList[5] == 0:
                value = self.getThousandDigitValue(number%100000,numberList, 5)
            else:
                    value = valueDict[numberList[5]]+" लाख " + self.getThousandDigitValue(number%100000,numberList, 5)
        elif digits == 7:
            # thousandDigitValue = self.getThousandDigitValue(number%100000,numberList, 5)
            lakhsDigit = number//100000
            if lakhsDigit == 0:
                value = self.getThousandDigitValue(number%100000,numberList, 5)
            else:
                if numberList[4] == 0:
                    millionDigitNumber = number // 100000
                    value = valueDict[millionDigitNumber]+" लाख " + self.getThousandDigitValue(number%100000,numberList,4)
                else:
                    value = valueDict[lakhsDigit]+" लाख " + self.getThousandDigitValue(number%100000,numberList, 5)
        return value

    def getValue(self,number):
        number = str(number)
        beforeDecimal = number.split(".")
        noOfDigits = len(str(beforeDecimal[0]))
        number = int(float(number))
        numberList = self.getPositionValue(number)
        if len(numberList) == 1:
            value = valueDict[number]

        if len(numberList) == 2:
            value = valueDict[number]

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
            value = valueDict[numberList[7]]+" कोटी " + self.getMillionDigitValue(number%10000000,numberList, 7)

        if len(numberList) == 9:
            if numberList[6] == 0:
                millionDigitNumber = number//10000000
                value = valueDict[millionDigitNumber]+" कोटी " + self.getMillionDigitValue(number%10000000,numberList, 6)
            else:
                thousandDigitValue = self.getMillionDigitValue(number%10000000,numberList, 7)
                millionsDigit = number // 10000000
                value = valueDict[millionsDigit] +" कोटी " + thousandDigitValue

        value = value + " रुपये "
        try:
            if len(beforeDecimal) > 0 and int(beforeDecimal[1]) != 0:
                afterDecimalNumber = beforeDecimal[1][0:2]
                number = int(float(afterDecimalNumber))
                value= value + valueDict[number] + " पैसे"
                return value
        except:
            return value
