from urlpuller import getURLS
from stat_scraper import stat_creator
seasonlist = [(2008,2009),(2009,2010),(2010,2011),(2011,2012),(2012,2013),(2013,2014),(2014,2015),(2015,2016),(2016,2017),(2017,2018),(2018,2019)]
for item in seasonlist:
    startyear, endyear = item
    print(startyear)
    print(endyear)

    x = getURLS(startyear,endyear)

    print(len(x))
    i = 0
    filename = 'New season'+str(startyear)+str(endyear)+'.txt'
    print(filename)
    f = open(filename, 'w+')
    for url in x:
        z = stat_creator(url)
        z = str(z)
        f.write(z)
        f.write("\n")
        f.flush()
        i+=1
        print(f"{round((i/len(x))*100)}%")
    f.close()
    print("done")


