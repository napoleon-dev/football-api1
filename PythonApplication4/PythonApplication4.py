#!/usr/bin/python
# -*- coding: utf-8 -*-
import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': '',
           'X-Response-Control': 'minified'}
connection.request('GET', '/v1/teams/66/fixtures?timeFrame=p318', None,
                   headers)
response = json.loads(connection.getresponse().read().decode())

print (json.dumps(response, sort_keys=True, indent=4, separators=(',',': ')))
fixtures = response['fixtures']


# wincount

wincount = 0
lossCount = 0
drawCount = 0
winHome = 0
winAway = 0
counter= 0

for val in fixtures:

    competitionId=val["competitionId"]
    if competitionId==426:
        matchday=val["matchday"]
        #if matchday>=20:
            # is united away or home?

        awayTeamId = val['awayTeamId']
        homeTeamId = val['homeTeamId']
        awayTeamName=val["awayTeamName"]
        homeTeamName=val["homeTeamName"]
           # print (awayTeamId)

    
        results=val['result']
        goalsAwayTeam = results['goalsAwayTeam']
        goalsHomeTeam = results['goalsHomeTeam']
        #who won home or away?
        if goalsHomeTeam > goalsAwayTeam:
            if homeTeamId==66:
                wincount=wincount+1
                winHome=winHome+1
                print("Result: ",goalsHomeTeam," : ",goalsAwayTeam,homeTeamName,"vs",awayTeamName,"Home-Win")
        elif goalsHomeTeam  < goalsAwayTeam:
                if homeTeamId==66:
                    lossCount=lossCount+1
                    print("Result: ",goalsHomeTeam," : ",goalsAwayTeam,homeTeamName,"vs",awayTeamName,"Home-Loss")

        if goalsAwayTeam  > goalsHomeTeam:
                if awayTeamId==66:
                    wincount=wincount+1
                    winAway=winAway+1
                    print("Result: ",goalsHomeTeam," : ",goalsAwayTeam,homeTeamName,"vs",awayTeamName,"Away-Win")
        elif  goalsAwayTeam  < goalsHomeTeam:
            #away loss
            if awayTeamId==66:
                lossCount=lossCount+1
                print("Result: ",goalsHomeTeam," : ",goalsAwayTeam,homeTeamName,"vs",awayTeamName,"Away-Loss")
            #home loss
        if goalsHomeTeam  == goalsAwayTeam:
                if homeTeamId==66 or awayTeamId==66:
                    drawCount=drawCount+1
                    print("Result: ",goalsHomeTeam," : ",goalsAwayTeam,homeTeamName,"vs",awayTeamName,"Draw")
    
counter=counter+1
    #if counter>=20:
    #    break   
print("Total wins: ",wincount)
print("Away Win:",winAway)
print("Home Wins: ",winHome)
print("Losses: ",lossCount)
print("Draws: ",drawCount)
