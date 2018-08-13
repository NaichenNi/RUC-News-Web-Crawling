#import needed modules
import matplotlib.pyplot as plt
import re

#input json file, use re group to get time string and form a list named 'a'
a=[re.search(r'(\d+)-(\d+)-(\d+)',line).group(0) for line in open('C:\Users\Apple\Desktop\RucReport\RucReport_data.json')]

# transform list a into string b
b=str(a)

# count the amount of published reports from Jan2016 to Oct2016
num1=b.count("2016-01")
num2=b.count("2016-02")
num3=b.count("2016-03")
num4=b.count("2016-04")
num5=b.count("2016-05")
num6=b.count("2016-06")
num7=b.count("2016-07")
num8=b.count("2016-08")
num9=b.count("2016-09")
num10=b.count("2016-10")

# get a list"amount" to show the number of reports from Jan2016 to Oct2016
amount=[num1,num2,num3,num4,num5,num6,num7,num8,num9,num10]
print amount

# transform time string to time format and form a list"c"
c=[datetime.datetime.strptime(i,"%Y-%m-%d") for i in a]

# define a function to filter qualified dates
def fun(s):
    if datetime.datetime(2016,11,1,0,0)>s>datetime.datetime(2015,12,31,0,0):
        return s

#use filter funtion to filter qualified dates and get a list"d"
d=filter(fun,c)

# set the title, xlabel and ylabel
plt.title('RucReport Histogram')
plt.xlabel('month')
plt.ylabel('amount')

#draw the histogram
plt.hist(d,range=(datetime.datetime(2016,1,1,0,0),datetime.datetime(2016,10,31,0,0)))
