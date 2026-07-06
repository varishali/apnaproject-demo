import matplotlib.pyplot as plt
days = ["mon","Tues","Wed","Thur","Fri","Sat","Sun"]
direct = [50,60,70,80,90,100,110]
organic = [30,40,50,55,60,70,80]
social = [20,25,30,35,40,50,60]

plt.stackplot(days,direct,organic,social, labels=["Direect","Organic","Social"])
plt.title("Marketing data for the week")
plt.xlabel("Days")
plt.ylabel("# of customers")
plt.legend()
plt.show()