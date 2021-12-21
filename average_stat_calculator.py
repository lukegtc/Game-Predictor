import numpy as np
import ast

#SINGLE GAME VERSION
#input is an array of format [[name1,stat1,stat2,stat3,stat4],[name2,stat1,stat2,stat3,stat4],1/0,date as str]
#team_dict's keys are the team names
#and each entry is an array with rows =
# [avg stat 1, avg stat 2, avg stat 3, avg stat 4, 2nd team name, did team play away/home(1/0), away/home win(1/0), date]


def create_teams_dict():
    team_names = ['Boston Celtics', 'Brooklyn Nets','New York Knicks','Philadelphia 76ers', 'Toronto Raptors',
                'Chicago Bulls','Cleveland Cavaliers', 'Detroit Pistons', 'Indiana Pacers','Milwaukee Bucks',
                'Denver Nuggets', 'Minnesota Timberwolves', 'Oklahoma City Thunder','Portland Trail Blazers',
                'Utah Jazz', 'Golden State Warriors','Los Angeles Clippers','Los Angeles Lakers','Phoenix Suns',
                'Sacramento Kings', 'Atlanta Hawks','Charlotte Hornets','Miami Heat','Orlando Magic',
                'Washington Wizards','Dallas Mavericks', 'Houston Rockets','Memphis Grizzlies',
                'New Orleans Pelicans','San Antonio Spurs']

    teams_dict = dict()

    for name in team_names:
        #zeros are placeholder for the first game
        teams_dict[name] = np.zeros(8)

    return teams_dict


def add_game(teams_dict, game):

    name1, name2 = game[0][0], game[1][0]
    first1 = False
    first2 = False

    if np.count_nonzero(teams_dict[name1][0]) == 0:
        first1=True
        teams_dict[name1] = np.vstack(
            (teams_dict[name1], np.array([game[0][1], game[0][2], game[0][3], game[0][4], name2, 1, game[2], game[3]])))
        teams_dict[name1] = teams_dict[name1][1:]
    if np.count_nonzero(teams_dict[name2][0]) == 0:
        first2=True
        teams_dict[name2] = np.vstack(
            (teams_dict[name2], np.array([game[1][1], game[1][2], game[1][3], game[1][4], name1, 0, game[2], game[3]])))
        teams_dict[name2] = teams_dict[name2][1:]

    if not first1:
        num_games_played1 = len(teams_dict[name1])
        old_stats1 = teams_dict[name1][-1][:4].astype(float)
        new_stats1 = old_stats1*(num_games_played1/(num_games_played1+1)) + game[0][1:].astype(float)*(
                1/(num_games_played1+1))
        teams_dict[name1] = np.vstack(
            (teams_dict[name1], np.hstack((new_stats1, name2, 1, game[2], game[3]))))
    if not first2:
        num_games_played2 = len(teams_dict[name2])
        old_stats2 = teams_dict[name2][-1][:4].astype(float)
        new_stats2 = old_stats2 * (num_games_played2 / (num_games_played2 + 1)) + game[1][1:].astype(float) * (
                1 / (num_games_played2 + 1))
        teams_dict[name2] = np.vstack(
            (teams_dict[name2], np.hstack((new_stats2, name1, 0, game[2], game[3]))))


sample_game = np.array([np.array(['Boston Celtics',0.57,23,12,4]),np.array(['Brooklyn Nets',0.49,21,15,3]),1,'11/15/2018'])
sample_game2 = np.array([np.array(['Boston Celtics',0.51,25,19,5]),np.array(['Brooklyn Nets',0.60,18,14,6]),1,'11/15/2018'])
sample_game3 = np.array([np.array(['Boston Celtics',0.55,20,16,2]),np.array(['Brooklyn Nets',0.58,20,10,6]),1,'11/15/2018'])
sample_game4 = np.array([np.array(['Los Angeles Lakers',0.55,20,16,2]),np.array(['Cleveland Cavaliers',0.58,20,10,6]),1,'11/15/2018'])

games_dict = create_teams_dict()

#adds games from "games.txt" to dictionary with all games per team (games_dict)

fin = open("games.txt")
for line in fin:
    line = ast.literal_eval(line)
    line = np.array(line)
    line[0] = np.array(line[0])
    line[1] = np.array(line[1])
    add_game(games_dict, line)

print(games_dict["Los Angeles Lakers"])



