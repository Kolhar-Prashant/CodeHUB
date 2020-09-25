
def calc(princ,int_rate,year,First_year_intr = None):
    CI =  (princ * (100 + int_rate)) / 100
    if year == 1:
        First_year_intr = CI - princ
        year += 1
    return CI,year,First_year_intr

princ = float(input("Enter the Principal amount: "))
base_princ = princ
years = float(input("Enter the number of years: "))
base_years = years
try:
    months = str(years).split(".")
    years = int(months[0])
    months = int(months[1])
except:
    months = 0

int_rate = float(input("Enter the rate of interest: "))
year = 1
First_year_intr = 0

for _ in range(years):
    princ,year,First_year_intr = calc(princ,int_rate,year,First_year_intr)

monthly_intr = First_year_intr / 12
monthly_intr = monthly_intr * months
princ += monthly_intr

print("Compound interest capitalized on Rs",base_princ,"for",years,"years",months,"months is Rs",round(princ-base_princ,2))
print("Total value of investment after interest compounding is",round(princ,2))

