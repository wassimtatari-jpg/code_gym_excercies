from datetime import date

year=int(input("Enter the year of birth : "))
month=int(input("Enter the month of birth :"))
day=int(input("Enter the day of birth : "))

birth_date=date(year,month,day)

current_date=date.today()

deff_cal=(current_date-birth_date).days
print(f"Your birth date is {birth_date}")
print(f"Current date is {current_date}")
print(f"The numbers of days passed since the birth date {deff_cal}")