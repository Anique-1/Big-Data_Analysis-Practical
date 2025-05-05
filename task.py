import pandas as pd

#create dataframe
stu={
        "name":["muahmmad ali akbar", "muhammmad ali usman", "muhammad ahmad bajwa", "muhammad anqiue ahmad", "muhammad hassan ali", ",muhammad ansab raza", "mhammad faiz ahmad", "muhammad ali ahmad", "muhammad sarib fraz", "muhammad wahab raza"],
        "age":[20,21, 23, 19, 21,20, 19, 18, 17, 22],
        "sex":["male","male","male","male","male","male","male","male","male","male",],
        "marks":[23, 56, 78, 9, 12, 45, 12, 56, 78, 34],
        "city":["faisalabad","lahore", "faisalabad", "islamabad", "multan","faisalabad", "faisalabad","lahore", "islamabad","faisalabad"],
        "date-of-birth":["2004-03-12","2005-04-22", "2002-03-25", "2004-03-12", "2002-04-30", "2003-05-29", "2004-06-11", "2006-03-12", "2001-02-10","2001-01-9"],
        "start-date":["2004-03-12","2004-03-11","2004-02-12","2004-03-11","2005-03-12", "2007-04-11", "2005-07-9", "2001-07-09", "2005-09-10", "2001-01-11"],
        "end-date":["2024-03-11","2024-03-15", "2024-03-19","2024-04-12", "2024-05-10","2024-03-9","2024-04-09", "2024-03-29", "2024-04-8", "2024-05-16" ]
    }


var=pd.DataFrame(stu)

#print(var)


#caluculate the middle name of the students

mid_name=var["name"].str.split(" ").str.get(1)
print(mid_name)


#contains ali

con_name=var["name"].str.contains("ali")
print(con_name)


#replace the city name with 3 code words

re_city=var["city"].replace({
    "faisalabad":"FSD",
    "lahore":"LHR",
    "multan":"MUL",
    "islamabad":"ISB"
})


print(re_city)


#people whose name greater than 10 

cal_len=var[var["name"].str.len() > 10]
print(cal_len)


#yountest and oldest student in the class
young_oldest=var["date-of-birth"].min()
young_oldest1=var["date-of-birth"].max()
print(f'oldest {young_oldest}')
print(f'youngest {young_oldest1}')


#calualte min 
cal_stats=var.agg({
     "marks":["min", "max","median", "skew", "mean"],
     "age":["min"]
})
print(cal_stats)


#average and median marks of male and female students

avg_mar=var.agg({
    "marks":["median", "average"]
})
print(avg_mar)


#completion of degree
var['start-date'] = pd.to_datetime(var['start-date'])
var['end-date'] = pd.to_datetime(var['end-date'])

# Calculate degree completion (difference between start-date and end-date)
var2= var['end-date'] - var['start-date']
print(var2)