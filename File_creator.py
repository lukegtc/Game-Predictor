from stat_scraper import stat_creator
from urlpuller import getURLS



def season_file_maker(season_start,season_end):
    box_score_links = getURLS(season_start, season_end)
    season_file = open(str(season_start) +'-'+ str(season_end),"w+")
    i = 0
    for url in box_score_links:
        season_file.write(str(stat_creator(url)) + '\n')
        #print(url)
        i +=1
        print(i)
    season_file.close()

season_file_maker(2015,2017)