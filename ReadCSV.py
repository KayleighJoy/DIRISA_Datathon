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
        self.filter_9()
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


mainRun = ReadIn("Output_Filter_9.csv", "Output_Filter_9_Take2.csv")

mainRun.process()


   

    