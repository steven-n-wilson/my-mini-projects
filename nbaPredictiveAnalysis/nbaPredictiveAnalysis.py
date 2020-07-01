from urllib.request import urlopen
from bs4 import BeautifulSoup
from elopy import *
import pandas as pd
imp = Implementation()

# NBA season we will be analyzing
year = 2020
months = ['october', 'november', 'december', 'january', 'february', 'march']

headers = []
rows = []
match_date = []
match_stats = []
raw_match_data = []
sortedRanking = []

imp.addPlayer('Hank')

for month in months:
    # URL page we will scraping
    url = "https://www.basketball-reference.com/leagues/NBA_{}_games-{}.html".format(year, month)

    # this is the HTML from the given URL`
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    # use findALL() to get the column headers
    # Example -> soup.findAll('tr', limit=1), we use limit 1 to only get the first header

    # use getText() to extract the text we need into a list
    headers = [th.getText() for th in soup.findAll('tr', limit=1)[0].findAll('th')]
    unwanted_headers = ['\xa0', '\xa0','Notes']

    headers = [header for header in headers if header not in unwanted_headers]
    headers.insert(4, 'Result') #Adds Result Header
    headers.insert(5, 'Diff') #Adds Diff Header 
    # print(headers)



    # avoid the first header row -> [1:]
    rows = soup.findAll('tr')[1:]
    # print(rows)

    match_date = [[th.getText() for th in rows[i].findAll('th')]
                for i in range(len(rows))]

    # print(game_date)

    match_stats = [[td.getText() for td in rows[i].findAll('td')]
                for i in range(len(rows))]

    #     Deletes (by index) the unnecessary td concerning ['\xa0', '\xa0','Notes'] headers
    for i in range(len(rows)):
        del match_stats[i][5], match_stats[i][5],match_stats[i][6]

    # Adds Won or Lost value to Result Header
    for i in range(len(rows)):
        match_stats[i].insert(3, int(match_stats[i][2])- int(match_stats[i][4]))#Adds diff

        if int(match_stats[i][2]) > int(match_stats[i][5]):
            match_stats[i].insert(3,'Won')
        else: 
            match_stats[i].insert(3,'Lost')
            
    for i in range(len(rows)):
        imp.addPlayer(match_stats[i][1]) #Adds Team to Elo
        imp.addPlayer(match_stats[i][5]) #Adds Team to Elo

    # print (imp.getRatingList())   
    for i in range(len(rows)):
        if int(match_stats[i][2]) > int(match_stats[i][6]):
            imp.recordMatch(match_stats[i][1], match_stats[i][5],winner= match_stats[i][1])
        elif int(match_stats[i][2]) < int(match_stats[i][6]):
            imp.recordMatch(match_stats[i][1], match_stats[i][5],winner= match_stats[i][5])
            
    # print ("\n",imp.getRatingList())   

    sortedRanking = sortTuple((imp.getRatingList()))

    # Merge game _date and match stats into one list

    for i in range(len(match_date)):
        raw_match_data .append(match_date[i] + match_stats[i])

    # print(raw_match_data )

# stats = pd.DataFrame(raw_match_data, columns = headers)
# # stats.head(len(rows))

# stats.to_csv('data.csv')

# ranking = pd.DataFrame(sortedRanking, columns = ['Team', 'Rank'])
# # ranking.head(len(rows))

# ranking.to_csv('ranking.csv')

print(imp.predictMatch('Cleveland Cavaliers', 'Milwaukee Bucks'))
