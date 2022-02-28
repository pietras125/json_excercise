import json
import os
from datetime import datetime

f = open('dane.json')
data = json.load(f)

diedActors = []
for diedActor in data:
    if('dod' in diedActor):
        diedActors.append(diedActor)
#print(diedActors)

aliveActors = []
for aliveActor in data:
    if not ('dod' in aliveActor):
        aliveActors.append(aliveActor)

birthdatesAlive = []
for years in aliveActors:
    convertedDate = datetime.strptime(years['dob'], "%d-%m-%Y")
    birthdatesAlive.append(convertedDate)

#POINTS 1,2==================================================================
for name in data:
    if (datetime.strptime(name['dob'], "%d-%m-%Y") == min(birthdatesAlive)):
        answer1 = name['name']
        print('1. Oldest alive actor is', answer1, '.')
for name in aliveActors:
    if (datetime.strptime(name['dob'], "%d-%m-%Y") == max(birthdatesAlive)):
        answer2 = name['name']
        print('2. Youngest actor is', answer2, '.')

#POINTS 3,4==================================================================
thisYear = datetime.today()
answer3 = thisYear.year - min(birthdatesAlive).year
answer4 = thisYear.year - max(birthdatesAlive).year
print('3. The oldes actor is', answer3, 'years old.')
print('4. The youngest actor is', answer4, 'years old.')

#POINT 5=====================================================================
maxMovies = []
for movies in data:
    maxMovies.append(len(movies['movies']))
#print(max(maxMovies))
for personAndMoviesCount in data:
    if (len(personAndMoviesCount['movies']) == max(maxMovies)):
        answer5 = personAndMoviesCount['name']
        print('5.',answer5,'has',max(maxMovies),'movies.' )

#POINT 6=====================================================================
hasDiedEarliest = []
for personDead in diedActors:
    if (personDead['dod'] != "\n"):
        dateconv = datetime.strptime(personDead['dod'], "%d-%m-%Y")
        hasDiedEarliest.append(dateconv)
earliestDeathDate = min(hasDiedEarliest)
answer6 = ''

for person in diedActors:
    if (person['dod'] != "\n" and datetime.strptime(person['dod'], "%d-%m-%Y") == earliestDeathDate):
        answer6 = person['name']
print('6.',answer6,'is dead for the longest period of time.')

#POINT 7=====================================================================
moviesList = []
for movies in data:
    moviesList.append(movies['movies'])
    #print(movies['movies'])

yearsList = []
year =""
for i in range(len(moviesList)):
    for j in range(len(moviesList[i])):
        if ('year' in moviesList[i][j]):
            if (moviesList[i][j]['year'] != ''):
                year = str(moviesList[i][j]['year'])
                year.replace("\\n","")
                year.replace("\\t","")
                if (year != ''):
                    yearsList.append(year)
                else:
                    continue
            else:
                continue
        else:
            continue
#print(yearsList)

theOldestMovie = min(yearsList)
for i in range(len(moviesList)):
    for j in range(len(moviesList[i])):
        if ('year' in moviesList[i][j]):
            if (moviesList[i][j]['year']==theOldestMovie):
                answer7 = moviesList[i][j]['title']
print('7. The oldest movie is ',answer7)

#POINT 8 =================================================================
birthdatesAll = []
for yearsOfBirth in data:
    convertedDate = datetime.strptime(yearsOfBirth['dob'], "%d-%m-%Y").year
    birthdatesAll.append(convertedDate)
#print(birthdatesAll)

tmpList =[]
for i in birthdatesAll:
    if i not in tmpList:
        tmpList.append(i)
        birthdatesAll.remove(i)
#print(birthdatesAll)
answer8 = birthdatesAll
print('8. Repeatable years:',answer8)

#POINT 9===================================================================
answer9 = len(diedActors)
print('9. There are',answer9,'dead actors.')

#POINT 10==================================================================
ageList = []
for birthDate in range(len(birthdatesAlive)):
    ageList.append(int(thisYear.year - birthdatesAlive[birthDate].year))
#print(ageList)
answer10 = sum(ageList)/len(ageList)
print('10. Average age of alive actors is',answer10)

#POINT 11===================================================================
actors = []
moviesCount = []
for i in data:
    actors.append(i['name'])
    moviesCount.append(len(i['movies']))
#print(moviesCount)
#print(actors)
answer11 = sum(moviesCount)/len(actors)
print('11. Average movies per actor is',answer11)
        