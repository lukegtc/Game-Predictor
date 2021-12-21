import re

def normalize(lst):
    new_lst = [0]*len(lst)
    if len(lst) == 0:
        return
    for i in range(len(lst)-4):
        max_ = max(lst[i],lst[i+4])
        new_lst[i] = lst[i]/max_
        new_lst[i+4]= lst[i+4]/max_
    return new_lst


def load_data():
    files = ["DataSet-10.txt", "DataSet-11.txt", "DataSet-12.txt", "DataSet-14.txt", "DataSet15.txt"]
    load_data(files)

    winners = []
    losers = []

    for file in files:
        with open(file) as f:
            lines = f.readlines()
            for line in lines:

                value = []
                stripped = re.sub('[\[\]]', '', line)
                stripped = re.sub('([\"\'])', '', stripped)
                stripped = re.sub('([\"\'])', '', stripped)
                splitted = stripped.split(",")
                values = [float(val) for val in splitted[:-2] if float(splitted[-2]) == 1.0]
                values = normalize(values)
                if values is not None:
                    winners.append(values)
                walues = [float(val) for val in splitted[:-2] if float(splitted[-2]) == 0.0]
                walues = normalize(walues)
                if walues is not None:
                    losers.append(walues)

    return winners,losers








