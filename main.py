try:
    import datetime
#we are activating the datetime function by import
    age = int(input('Enter your age or year and find out how old you are:'))
#The reason we put int is because we need to enter a number here
    x = datetime.date.today()
    print(x.year-age)
#Here, it will subtract the age you entered from the current year and get the age of Nexha
except:
    print(age+x.year)
