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
            #print(person)
            temp = []
            income = person[5]
            if income == "Prefer not to answer":
                continue
            mental = False
            for i in range (6,14):
                if person[i] != '':
                    mental = True
            if mental == True:
                temp.append(1)
            else:
                temp.append(2)

            if person[0] == "Some highschool":
                temp.append(0)
            if person[0] == "High School or GED":
                temp.append(1)
            elif person[0] == "Some Undergraduate":
                temp.append(2)
            elif person[0] == "Completed Undergraduate":
                temp.append(3)
            elif person[0] == "Some Masters":
                temp.append(4)
            elif person[0] == "Completed Masters":
                temp.append(5)
            elif person[0] == "Some Phd":
                temp.append(6)
            elif person[0] == "Completed Phd":
                temp.append(2)

            if person[1] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[2] == "Yes":
                temp.append(1)
            else:
                temp.append(2)

            if person[3] == "18-29":
                temp.append(1)
            elif person[3] == "30-44":
                temp.append(2)
            elif person[3] == "45-60":
                temp.append(3)
            else:
                temp.append(4)

            if person[4] == "Male":
                temp.append(1)
            else:
                temp.append(2)

            income = income.replace("$","")
            income = income.replace(",","")
            if income == "0-9999":
                temp.append(1)
            elif income =="10000-24999":
                temp.append(2)
            elif income =="25000-49999":
                temp.append(3)
            elif income =="50000-74999":
                temp.append(4)
            elif income =="75000-99999":
                temp.append(5)
            elif income =="100000-124999":
                temp.append(6)
            elif income =="125000-149999":
                temp.append(7)
            elif income =="150000-174999":
                temp.append(8)
            elif income =="175000-199999":
                temp.append(9)
            elif income =="200000+":
                temp.append(10)

            #print(person)

            if "Phone" in person[14]:
                temp.append(1)
            else:
                temp.append(2)

            if person[15] == "Yes":
                temp.append(1)
            else:
                temp.append(2)
            
            self.newPeople.append(temp)



mainRun = Convert_Medical_Data("DataSets\Mental_Illness_Survey_2.csv", "DataSets\Mental_Binary_Labels_More.csv")
mainRun.process()



   

    