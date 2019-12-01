from datetime import date

def calcAge(year, month, day):
    today = date.today()
    return today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))