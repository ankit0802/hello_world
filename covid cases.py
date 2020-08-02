from covid import Covid
from matplotlib import pyplot as pl

l=[]
xp=[]
covid = Covid()
colour=["r","y","g","b"]
print("*******************LIVE COVID CASES UPDATES********************")
country=input("Enter the country name:")
received=covid.get_status_by_country_name(country)
data={
      key:received[key]
      for key in received.keys() and {'confirmed','active','deaths','recovered'}
      }

for x in data:
    print(x,":",data[x])
    xp.append(x)
    l.append((data[x]))

bars=pl.bar(xp,l,label=country,color=colour,width=.4)
pl.legend()
tle="LIVE COVID-19 Updates from "+(country)
pl.xlabel("UPDATES")
pl.ylabel("Patients")
pl.title(tle)
for bar in bars:
    yval = bar.get_height()
    pl.text(bar.get_x(), yval + 10, yval,)

pl.show()

