#  This is an attempt at creating a datastructure
#  capable of fulfilling our needs

#  Currently needs fixing will continue to work on it in a bit
# import matplotlib.pyplot as plt
# import numpy as np
import re
import random
# from sklearn.cluster import MeanShift as ms
from matplotlib import style

style.use("ggplot")


class FileReader:
    def __init__(self, files):
        self.file = files
        self.match_ups = []
        self.teams = []
        self.team_stats = dict()
        self.hash_lst = random.sample(range(1, 1000000),100000)


    def some_processing(self):

        with open(self.file, "r+") as f:
            lines = f.readlines()

            for line in lines:
                stripped = re.sub('[\[\]]', '', line)
                stripped = re.sub('([\"\'])', '', stripped)
                splits = stripped.split(",")
                team_one = Team(splits[0].strip())
                team_two = Team(splits[5].strip())
                hash = self.hash_lst.pop()

                for team in self.teams:
                    if team != team_one:
                        continue
                    else:
                        break
                else:
                    self.teams.append(team_one)

                for team in self.teams:
                    if team != team_two:
                        continue
                    else:
                        break
                else:
                    self.teams.append(team_two)

                for team in self.teams:

                    if splits[0].strip() == team.name:
                        team.match_ups.append(hash)
                        team.FG.append(float(splits[1].strip(" ")))
                        team.TOV.append(float(splits[2].strip(" ")))
                        team.ORB.append(float(splits[3].strip(" ")))
                        team.FT.append(float(splits[4].strip(" ")))
                        team.win_loss.append([int(splits[-1].strip())])

                    elif splits[5].strip() == team.name:
                        team.match_ups.append(hash)
                        team.FG.append(float(splits[6].strip(" ")))
                        team.TOV.append(float(splits[7].strip(" ")))
                        team.ORB.append(float(splits[8].strip(" ")))
                        team.FT.append(float(splits[9].strip(" ")))
                        team.win_loss.append([int(1) if int(splits[-1].strip()) == 0 else int(0)])


        #for team in self.teams:
            #print(team)


class Team:

    def __init__(self, name):
        self.name = name
        self.match_ups = []
        self.FG = []
        self.TOV = []
        self.ORB = []
        self.FT = []
        self.average = []
        self.win_loss = []

    def __eq__(self, other):
        return self.name == other

    def __str__(self):
        return f"{self.name} -- Stats: {self.average}"


    def averager(self,lst):
        av_lst = []
        for i in range(len(lst)):
            av_lst.append(sum(lst[:i])/(i+1))

        return av_lst

    def last_three_games(self,lst):
        three_lst = lst[0:2]
        for i in range(2,len(lst)):
            three_lst.append(sum(lst[i-2:i+1])/3)
        return three_lst

    def av_stats(self,av_func):

        FG_av = av_func(self.FG)
        TOV_av = av_func(self.TOV)
        ORB_av = av_func(self.ORB)
        FT_av = av_func(self.FT)


        for i in range(1,len(self.FG)):
            self.average.append([round(FG_av[i],3),round(TOV_av[i],3),round(ORB_av[i],3),round(FT_av[i],3)])

    def get_data(self):
        return self.average


def write_to_file(txt,season):
    with open(f"ConvDataSet-{str(season)}.txt","w+") as f:
        for val in txt:
            for gal in val:
                f.write(str(gal) + ";")
            f.write("\n")
        f.flush()
    print("done")



def generate_data_set(file,seasons):
    season = FileReader(file)
    season.some_processing()

    
    games = set()
    ultimate_lst = []
    dlist = []
    for team in season.teams:
        for val in team.match_ups:
            games.add(val)


    for hal in games:
        glist = []
        i = 0
        for team in season.teams:
            team.av_stats(team.last_three_games)
            if hal in team.match_ups:
                idx = team.match_ups.index(hal)
                glist.append(team.average[idx])
                glist.append(team.win_loss[idx])



        dlist.append(glist)



    for val in dlist:
        win_ = val[1]
        win_.append(*val[-1])
        del val[1]
        del val[-1]
        val.append(win_)
    write_to_file(dlist,seasons)



"s20122013.txt"
files = ["s20082009.txt","s20092010.txt","s20102011.txt","s20112012.txt","s20132014.txt","s20142015.txt","s20152016.txt","s20162017.txt","s20172018.txt","s20182019.txt"]
seasons  = [val[7:9] for val in files]

for i in range(len(files)):
    generate_data_set(files[i],seasons[i])













   #

'''

glist = []

    for i in range(len(season.teams)//2):
        team_one = season.teams[2*i]
        team_two = season.teams[2*i + 1]
        team_one.av_stats()
        team_two.av_stats()
        glist.append([team_one.average[i],team_two.average[i],team_one.win_loss[i]])
    for val in glist:
        print(val)

    for i in range(len(season.teams)):
        team_one = season.teams[i]
        team_one.av_stats()
        for j in range(len(team_one.match_ups)):
            hash = team_one.match_ups[j]
            for team in season.teams:
                for val in team.match_ups:
                    if val == hash:
                        team_two = team
                        team_two.av_stats()
                        idx_2 = team_two.match_ups.index(val)
                        break



            game.append(team_one.average[j])
            game.append(team_two.average[idx_2])
            game.append(team_one.win_loss[j])
            games.append([game])



    print(games)
'''

#test_season = FileReader("s20082009.txt")
#test_season.some_processing()
#team = test_season.teams[0]
#team.av_stats()
#generate_data_set("s20082009.txt")
#print(team.get_data())