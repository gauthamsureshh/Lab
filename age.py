from datetime import date

print("Age Calculator")
name=input("Enter Ur Name:")
age=int(input("Enter Ur Current Age:"))
current_date=date.today()
current_year=current_date.year
century=100-age
year_to_century=current_year+century
print(f"Hello {name}. You will turn 100 years old in the year {year_to_century}.Stay Healthy..!")

