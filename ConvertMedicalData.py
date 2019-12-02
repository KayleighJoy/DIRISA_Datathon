#Class to read in from textfile

import csv

class Convert_Medical_Data:
    def __init__(self, filename, filename2):
        self.filename = filename
        self.filename2 = filename2
        self.people = list()
        self.newPeople = list()

    def process(self):
        self.read_csv()
        self.convert_to_num()
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

    def convert_to_num(self):
        for person in self.people:
            print(person)
            temp = []
            income = person[8]
            if income == "Prefer not to answer":
                continue
            if person[0] == "Yes":
                temp.append(1)
            else:
                temp.append(2)
            
            if person[1] == "High School or GED":
                temp.append(12)
            elif person[1] == "Some Undergraduate":
                temp.append(12)
            else:
                temp.append(16)

            if person[2] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[3] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[4] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[5] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[6] == "18-29":
                temp.append(1)
            elif person[6] == "30-44":
                temp.append(2)
            elif person[6] == "45-60":
                temp.append(3)
            else:
                temp.append(4)

            if person[7] == "Male":
                temp.append(1)
            else:
                temp.append(2)

            if "+" in income:
                income = income.replace("+", "")
                income = income.replace("$","")
                income = income.replace(",","")
                average = int(income)
            else:
                income = income.replace("$","")
                income = income.replace(",","")
                incomes = income.split("-")
                incomes[0] = int(incomes[0])
                incomes[1] = int(incomes[1])
                #print(incomes)
                average = (incomes[0] + incomes[1])/2

            southAfrican = average * 5.56
            temp.append(southAfrican)
            self.newPeople.append(temp)



mainRun = Convert_Medical_Data("DataSets\Mental Illness Survey 1 Matched.csv", "DataSets\Mental Illness Survey 1_Matched_Converted.csv")
mainRun.process()



   

    