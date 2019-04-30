from charlist import *
import itertools

def findTeam(eTeam, charList):
    eTeamValue = 0
    sTeam = []
    nameList = []
    teamValueList = []
    valueList = []
    for spot in eTeam:
        eTeamValue = eTeamValue + spot.get("invalue")
        for ch in charList:
            if spot.get("name") in ch:
                newvalue = ch.get("invalue") + ch.get(spot.get("name"))
                ch.pop("invalue")
                ch.update({"invalue":newvalue})
    for ch in charList:
        value = ch.get("invalue")
        valueList.append(value)
    combList = list(itertools.combinations(charList, 6))
    for team in combList:
        sTeamValue = 0
        for ch in team:
            chvalue = ch.get("invalue")
            for ch2 in team:
                if "s_" + ch2.get("name") in ch:
                    chvalue = chvalue + ch.get("s_" + ch2.get("name"))
            sTeamValue = sTeamValue + chvalue

        teamValueList.append(sTeamValue)
    tVMax = max(teamValueList)
    top = teamValueList.count(tVMax)
    print(top)
    selectTeam = teamValueList.index(tVMax)
    sTeamO = combList[selectTeam]

    for ch in sTeamO:
        name = ch.get("name")
        nameList.append(name)
    sTeam = nameList

    for ch in eTeam:
        for ch2 in eTeam:
            if "s_" + ch2.get("name") in ch:
                chvalue = ch.get("s_" + ch2.get("name"))
                eTeamValue = eTeamValue + chvalue

    for ch in eTeam:
        for sch in sTeamO:
            if sch.get("name") in ch:
                countvalue = ch.get(sch.get("name"))
                eTeamValue = eTeamValue + countvalue


    return sTeam, sTeamValue, eTeamValue








eTeam = [reinhardt, zarya, brigitte, ana, lucio, dva]
print(findTeam(eTeam, charlist))

