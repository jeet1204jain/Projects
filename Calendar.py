normal = {
    "Jan" : "1",
    "Feb" : "4",
    "Mar" : "4",
    "Apr" : "0",
    "May" : "2",
    "Jun" : "5",
    "Jul" : "0",
    "Aug" : "3",
    "Sep" : "6",
    "Oct" : "1",
    "Nov" : "4",
    "Dec" : "6",
}
leap = {
    "Jan" : "0",
    "Feb" : "3",
    "Mar" : "4",
    "Apr" : "0",
    "May" : "2",
    "Jun" : "5",
    "Jul" : "0",
    "Aug" : "3",
    "Sep" : "6",
    "Oct" : "1",
    "Nov" : "4",
    "Dec" : "6",
}

centcode = 6
def dayfinder():
    day = int(input("Enter Day: "))
    month = input("Enter Month: ")
    year = int(input("Enter Year: "))
    century = int(input("Enter Century: "))

    monthcode = int(normal[month])
    if (year % 4 == 0) or (century % 400 == 0):
        monthcode == int(leap[month])

    if century == 1700:
        centcode = 4
    elif century == 1800:
        centcode = 2
    elif century == 1900:
        centcode = 0
    elif century == 2000:
        centcode = 6

    yearqoutient = year//4

    sum = day + monthcode + year + centcode + yearqoutient

    if sum%7 == 1:
        day1 = "Sunday"

    if sum%7 == 2:
        day1 = "Monday"

    if sum%7 == 3:
        day1 = "Tuesday"

    if sum%7 == 4:
        day1 = "Wednesday"

    if sum%7 == 5:
        day1 = "Thursday"

    if sum%7 == 6:
        day1 = "Friday"

    if sum%7 == 0:
        day1 = "Saturday"

    print(f"Day on {day} {month} {year} is: {day1}")
dayfinder()