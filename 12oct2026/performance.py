performance_rating=float(input("enter performance rating:"))
year_completed=float(input("enter year completed in company:"))
if performance_rating>=4 and year_completed>=2:
    print("eligible for bonus")
else:
    print("not eligible for bonus")
