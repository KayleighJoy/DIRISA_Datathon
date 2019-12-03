#Class to read in from textfile

import csv

class ReadIn:
    def __init__(self, filename, filename2):
        self.filename = filename
        self.filename2 = filename2
        self.people = list()
        self.newPeople = list()

    def process(self):
        self.read_csv()
        #self.filter_Over99()
        #self.filter_9()
        self.clean_data()
        self.write_csv()

    def read_csv(self):
        with open(self.filename, mode='r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                self.people.append(row)
        del self.people[0]

    def write_csv(self):
        with open(self.filename2, mode='w') as writeDS:
            ds_writer = csv.writer(writeDS, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            ds_writer.writerows(self.newPeople)

    #don't run again
    def filter_Over99(self):
        for person in self.people:
            print(person)
            print("\n")
            if '99' in person:
                self.people.remove(person)
                continue
            if '999999999' in person:
                self.people.remove(person)
                continue
            if person[11] == '8':
                self.people.remove(person)
                continue
            if person[12] == '8':
                self.people.remove(person)
                continue
            if person[13] == '8':
                self.people.remove(person)
                continue
            if person[14] == '8':
                self.people.remove(person)
                continue
            if person[15] == '8':
                self.people.remove(person)
                continue
            if person[16] == '8':
                self.people.remove(person)
                continue
    
    def filter_9(self):
        check_nums = [0,3,5,6,7,9,16,17,19,36,37,40,44,59,72,86,153,155,156,161,168,170,171]
        people2 = []
        for person in self.people:
            found = False
            for i in range(0,len(person)):
                if i == 7 and person[i] == '99':
                    #print(person)
                    found = True
                if person[i] == '99':
                    found = True
                if person[i] == '9' and i not in check_nums:
                    found = True
            if found == False:
                people2.append(person)
        self.newPeople = people2

    def classifyIncome(self, num):
        if num <= 55599:
            return 1
        elif num >= 55600 and num <= 138999:
            return 2
        elif num >= 139000 and num <= 277999:
            return 3
        elif num >= 278000 and num <= 416999:
            return 4
        elif num >= 417000 and num <= 555999:
            return 5
        elif num >= 556000 and num <= 694999:
            return 6
        elif num >= 695000 and num <= 833999:
            return 7
        elif num >= 834000 and num <= 972999:
            return 8
        elif num >= 973000 and num <= 1111999:
            return 9
        else:
            return 10
    
    def clean_data(self):
        filterPeople = []
        for person in self.people:
            temp = []
            temp.append(int(person[1]))
            if person[2]== '99':
                continue
            elif person[2] > '8' and person[1] < '12' or person[1] == '88':
                temp.append(0)
            elif person[2] >= '12' and person[1] < '88':
                temp.append(1)
            else:
                temp.append(1)
            
            disable = False
            if person[3] == '9' or person[4] =='9' or person[5] =='9':
                continue
            for i in range(3,6):
                if person[i] == '1':
                    person[i] == True

            if disable:
                temp.append(1)
            else:
                temp.append(2)

            if person[6] == '3' or person[6] == '9':
                continue
            elif person[6] == '1' or person[6] == '2':
                temp.append(0)
            elif person[6] == '8':
                temp.append(1)
            
            ages = [1,2,3,4]
            age1 = [5,6]
            age2 = [7,8,9]
            age3 = [10,11,12]
            if person[7] in ages:
                continue
            elif person[7] in age1:
                temp.append(1)
            elif person[7] in age2:
                temp.append(2)
            elif person[7] in age3:
                temp.append(3)
            else:
                temp.append(4)

            if person[8] == '1':
                temp.append(1)
            else:
                temp.append(2)

            if person[9] == '999999999':
                continue
            elif person[9] == '888888888':
                houseID = person[0]
                total = 0
                for p in self.people:
                    if p[0] == houseID:
                        if p[9] == '999999999' or p[9] == '888888888':
                            total = total + 0
                        else:
                            num = int(p[9]) * 12
                            total = total + num
                toAppend = self.classifyIncome(total)
                temp.append(toAppend)
            else:
                num = int(person[9]) * 12
                toAppend = self.classifyIncome(num)
                temp.append(toAppend)

            if person[10] == '9':
                continue
            elif person[10] == '1':
                temp.append(1)
            else:
                temp.append(2)
            
            deleted = False
            found = False
            for i in range(11,29):
                if person[i] == '9':
                    deleted = True
                elif person[i] == '1':
                    found = True
            
            if deleted == True:
                continue
            if found == True:
                temp.append(1)
            else:
                temp.append(2)
            
            filterPeople.append(temp)

        self.newPeople = filterPeople

mainRun = ReadIn("DataSets\CensusData_Uncleaned.csv", "DataSets\CensusData_Cleaned.csv")

mainRun.process()


   

    