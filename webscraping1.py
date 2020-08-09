import requests
from bs4 import BeautifulSoup
import pandas as pd


url= "https://www.skysports.com/premier-league-table/2011"
page=requests.get(url)
print(page.status_code)
print(page)
#print(page.text)

soup=BeautifulSoup(page.text,"html.parser")
print(soup.prettify)
print(soup.find("a"))
print(soup.find_all("a"))
print(soup.find_all("a")[1])

league=soup.find("table",class_= "standing-table__table")
#print(league)
league_table=league.find_all("tbody")
#print(league_table)

for league_teams in league_table:
    rows=league_teams.find_all('tr')
    for row in rows:
        #team_names = row.find('td',class_= 'standing-table__cell standing-table__cell--name')   # shows all details
        #team_names = row.find('td',class_= 'standing-table__cell standing-table__cell--name').text
        team_names = row.find('td',class_= 'standing-table__cell standing-table__cell--name').text.strip()
        team_points = row.find_all('td',class_= 'standing-table__cell')[9].text.strip()
        print(team_names , team_points)


league_2011= []
for league_teams in league_table:
    rows=league_teams.find_all('tr')
    for row in rows:
        team_names = row.find('td',class_= 'standing-table__cell standing-table__cell--name').text.strip()
        team_points = row.find_all('td',class_= 'standing-table__cell')[9].text.strip()
        
        league_dict={"Team ": team_names,
                    "pts":team_points
                    }
        league_2011.append(league_dict)

df=pd.DataFrame(league_2011)
df.head()

df # whole data


# ADD IN SINGLE CODE 
league_2011= []
for league_teams in league_table:
    rows=league_teams.find_all('tr')
    for row in rows:
        team_names = row.find('td',class_= 'standing-table__cell standing-table__cell--name').text.strip()
        team_points = row.find_all('td',class_= 'standing-table__cell')[9].text.strip()
        team_won = row.find_all('td',class_= 'standing-table__cell')[3].text.strip()
        
        league_dict={"Team ": team_names,
                    "Pts":team_points,
                     "Won":team_won
                    }
        league_2011.append(league_dict)

a=pd.DataFrame(league_2011)
a
