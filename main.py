from typing import final

import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request, redirect, url_for, session

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

#TODO University of California Special cases
#TODO University of San Francisco/San Diego Special cases


#TODO Make way to combine PrincetonReview and CollegeFactual Rankings into single variable sets
    #TODO Make dictionary of P to CF conversions in order to save time on program



#10/19 -> Created function to create finalList to assign names and points (works for 2 lists so far) and cleaned up main function as well as ----Errors in list
#10/20 -> Revised rankingA() function to ensure all colleges (tested with 4 PrincetonReview functions) are show in finalList once with their proper values
            #And started making code to return ordered list of College Factual Rankings (turns out to be way easier than Princeton Review)
#10/21 -> Built CollegeFactual() function up to generating a newrankList
#10/24 -> rankingA() now works with CollegeFactual Function,             Started working with Flask
#10/26 -> Started more learning about flask, reportA() function works for first~20 colleges
#10/27 -> averageA() functions works all the time now, began working on way to join the two lists from C and P together
#10/30 -> converted college variables from CF and P functions to uniform strings
#10/31 -> Video of current functionality
#11/2 -> (Marked as ### in program) Used functionality of listA() function combined with google to compile complete lists of all colleges that might come up, and then now able to convert them without using google
        #Program now runs (with all 14 attributes) in about 45 seconds
#----------------------------------------------------------------------------------------------------------------------#

#Global Variables
newrankList = []
finalList = []
finalListCollegesOnlyP = []
finalListCollegesOnlyC = []
reportfinalListP = []
reportfinalListC = []
###conversionList = []
###finalConversionList = []
aImportance = 0
numPcalls = 3
baseList = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
baseList2 = [25, 24.5, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20.5, 20, 19.5, 19, 18.5, 18, 17.5, 17, 16.5, 16, 15.5, 15, 14.5, 14, 13.5, 13, 12.5, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5, 3, 2.5, 2, 1.5, 1]
#----------------------------------------------------------------------------------------------------------------------#

#Creates final list with all schools and all points (no averages yet, must be used after every CF or P Call)
def listA(order, funkName):
    #Global Variables
    global finalList
    global newrankList
    global baseList
    global finalListCollegesOnlyP
    global finalListCollegesOnlyC
    global baseList2
    ###global finalConversionList

    #Reset baseList
    baseList = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    baseList2 = [25, 24.5, 24, 23.5, 23, 22.5, 22, 21.5, 21, 20.5, 20, 19.5, 19, 18.5, 18, 17.5, 17, 16.5, 16, 15.5, 15,
                 14.5, 14, 13.5, 13, 12.5, 12, 11.5, 11, 10.5, 10, 9.5, 9, 8.5, 8, 7.5, 7, 6.5, 6, 5.5, 5, 4.5, 4, 3.5,
                 3, 2.5, 2, 1.5, 1]

    lennrl = len(newrankList)
    if lennrl > 25:
        lennrl = 25
    i = 0
    i2 = 0
    i3 = 0
    g = 0
    alreadyExists = False

    #If Princeton Review is called
    if funkName == "P":
        #Multiples baseList by User-Selected Importance Value
        while g < len(baseList):
            baseList[g] *= aImportance
            g += 1
        #Determines if it is first attribute or not
        if order == 1:
            #First attribute process
            while i < lennrl:
                finalList.append(newrankList[i])
                finalList.append(baseList[i])
                finalListCollegesOnlyP.append(newrankList[i])

                ###finalconversionlist.append...
                i += 1
        else:
            #Second Attribute Process
            while i2 < lennrl:
                #Repeats for every element in newrankList
                alreadyExists = False
                i3 = 0

                while i3 < len(finalList):
                    #If college already exists in final list
                    if newrankList[i2] == finalList[i3]:
                        finalList.insert((i3 + 1), baseList[i2])
                        alreadyExists = True
                        #print(alreadyExists)
                        break

                    i3 += 1
                #print(alreadyExists)
                if alreadyExists == False:
                    finalList.append(newrankList[i2])
                    finalList.append(baseList[i2])

                    ###finalconversionlist.append
                    finalListCollegesOnlyP.append(newrankList[i2])
                else:
                    pass

                i2 += 1
    #If CollegeFactual Function is Called
    elif funkName == "C":
        #print(lennrl)
        # Multiples baseList by User-Selected Importance Value
        while g < len(baseList2):
            baseList2[g] *= aImportance
            g += 1
        #print(baseList2)
        # Determines if it is first attribute or not
        if order == 1:
            # First attribute process
            while i < lennrl:
                finalList.append(newrankList[i])
                finalList.append(baseList2[i])
                finalListCollegesOnlyC.append(newrankList[i])
                i += 1
        else:
            # Second Attribute Process
            while i2 < lennrl:
                # Repeats for every element in newrankList
                alreadyExists = False
                i3 = 0

                while i3 < len(finalList):
                    # If college already exists in final list
                    if newrankList[i2] == finalList[i3]:
                        finalList.insert((i3 + 1), baseList2[i2])
                        alreadyExists = True
                        # print(alreadyExists)
                        break

                    i3 += 1
                # print(alreadyExists)
                if alreadyExists == False:
                    finalList.append(newrankList[i2])
                    finalList.append(baseList2[i2])

                    finalListCollegesOnlyC.append(newrankList[i2])
                else:
                    pass

                i2 += 1

    #print(finalList)

#Average-creating function, (must run twice for C and P)
def averageA(funkName2):
    global finalList
    global numPcalls
    global finalListCollegesOnlyP
    global finalListCollegesOnlyC
    global reportfinalListP
    global reportfinalListC

    #To split string to isolate each college and their points
    i4 = 1
    i5 = 1
    totalPts = 0
    totalAvgPts = 0
    i6 = 0
    i7 = 1
    i8 = 0
    i9 = 1

    #print(finalListCollegesOnly)
    if funkName2 == "P":
        tfinalList = finalList
        tfnLLength = len(tfinalList)
        while i9 < tfnLLength:
            if type(finalList[i4]) == str:
                #Adds all the numbers together between first string and second string
                totalPts = 0
                i7 = 1
                #print(i4)

                while i7 < i4:
                    totalPts += int(finalList[i7])
                    i7 += 1
                #print(totalPts)
                totalAvgPts = totalPts / numPcalls
                totalAvgPts = round(totalAvgPts, 2)

                reportfinalListP.append(finalListCollegesOnlyP[i8])
                reportfinalListP.append(totalAvgPts)
                #print(reportfinalList)



                del finalList[0]
                while type(finalList[0]) != str:
                    del finalList[0]

                #print(finalList)


                i8 += 1
                i4 = 1
            else:
                i4 += 1

                pass

            i9 += 1
    elif funkName2 == "C":
        tfinalList = finalList
        tfnLLength = len(tfinalList)
        while i9 < tfnLLength:
            if type(finalList[i4]) == str:
                # Adds all the numbers together between first string and second string
                totalPts = 0
                i7 = 1
                # print(i4)

                while i7 < i4:
                    totalPts += int(finalList[i7])
                    i7 += 1
                # print(totalPts)
                totalAvgPts = totalPts / numPcalls
                totalAvgPts = round(totalAvgPts, 2)

                reportfinalListC.append(finalListCollegesOnlyC[i8])
                reportfinalListC.append(totalAvgPts)
                # print(reportfinalList)

                del finalList[0]
                while type(finalList[0]) != str:
                    del finalList[0]

                # print(finalList)

                i8 += 1
                i4 = 1
            else:
                i4 += 1

                pass

            i9 += 1

#Function to combines reportfinalListP and reportfinalListC
def joinA():
    global finalListCollegesOnlyC
    global finalListCollegesOnlyP
    global reportfinalListP
    global reportfinalListC

    #Loop through all colleges in final P list (e1)
    e1 = 0
    e2 = 0
    alreadyExists = False
    while e1 < len(reportfinalListP):
        alreadyExists = False
        #print("\n" + reportfinalListP[e1])
        #Loops through all colleges in final CF list (e2)
        e2 = 0
        while e2 < len(reportfinalListC):
            #print(reportfinalListC[e2])
            if reportfinalListP[e1] == reportfinalListC[e2]:
                #New point value for found college = existing value + value from P list    all over 2
                reportfinalListC[e2 + 1] = (reportfinalListC[e2 + 1] + reportfinalListP[e1 + 1])/2

                alreadyExists = True
                break

            e2 += 2

        if alreadyExists == False:
            reportfinalListC.append(reportfinalListP[e1])
            reportfinalListC.append(reportfinalListP[e1 + 1])
        else:
            pass

        e1 += 2

#Function to return top 10 schools by points
def best10():
    global reportfinalListC

    e3 = 1
    largest = reportfinalListC[1]

    #Main loop that finds top 10 of rfList
    i = 0
    while i < 10:
        #Resets
        largest = reportfinalListC[1]
        e3 = 1

        #Finds largest integer in list and then prints the corresponding school value
        while e3 < len(reportfinalListC):
            if reportfinalListC[e3] > largest:
                largest  = reportfinalListC[e3]

            e3 += 2

        realI = reportfinalListC.index(largest)

        topSchool = reportfinalListC[realI - 1]

        #Creates final dictionary
        finalDict = {}
        finalDict[topSchool] = largest

        print(finalDict)

        #Deletes elements from rfList
        del reportfinalListC[realI]
        del reportfinalListC[realI - 1]

        i += 1


#Princeton Review Function
def princetonReview(pChoice, pImportance):
    global conversionList
    conversionList = []
    #Global Importance value
    global aImportance
    aImportance = pImportance

    #Searches Google to find URL of Attribute Ranking Site

    # to search
    query = "The Princeton Review Best College " + pChoice

    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        goodURL = j

    #print("Hello: " + goodURL)
    #Gets HTML Data from URL
    r = requests.get(goodURL)
    soup = BeautifulSoup(r.text, 'html.parser')
    j = soup.find('main', class_="col-lg-8 col-md-12 col-sm-12").get_text(strip=True)
    #print(j)

    rank1 = j.find("#1")
    #print(rank1)
    #------------------------------------------------------------------------------------------------------------#

    #Number for iterations v (testing purposes)
    if pChoice == "Internships Public" or pChoice == "Internships Private":
        testTimes = 20
    elif pChoice == "Public School value top 50" or pChoice == "Private School value top 50":
        testTimes = 25
    else:
        testTimes = 25
    #Loop to put top 25 in ordered list
    loop = 1
    rankList = []

    while loop < testTimes:
        #print(loop)
        loopS = str(loop)
        finder = '#' + loopS
        # print(finder)

        rank = j.find(finder)
        # print(rank)

        strnew = j.split(finder)
        # print(strnew)

        firstU = strnew[1]
        finalStr = ""
        i = 0
        x = 0

        while x < 4:
            while firstU[i] != ' ':
                finalStr = finalStr + firstU[i]
                i += 1

            # print(finalStr)
            i += 1
            x += 1

        #--------Editing the Final String
        upperList = []
        f = finalStr.find("Featured")
        if f == 0:
            finalStr = finalStr.replace("Featured", " ")
        for c in finalStr:
            if c.isupper() == True:
                upperList.append(c)
        #print(upperList)
        #print(finalStr)

        UnivExists = False
        CollegeOfExists = False

        if finalStr[0] == "U" and finalStr[10] == "o" or finalStr[11] == "o":
            UnivExists = True
        if finalStr[0] == "C" and finalStr[7] == "o":
            CollegeOfExists = True

        #print(finalStr)
        if UnivExists or CollegeOfExists:
            #Specific School Exception
            if finalStr == "UniversityofPuget":
                endCap = upperList[3]
            if finalStr =="UniversityofTexasat" or finalStr=="UniversityofIllinoisat":
                endCap = "a"
            else:
                if upperList[1] == upperList[2]:
                    endCap = upperList[3]
                else:
                    endCap = upperList[2]

            endCap_find = finalStr.find(endCap)
            newFinalStr = finalStr.split(finalStr[endCap_find])

            rankList.append(newFinalStr[0])
        else:
            if len(upperList) > 2:
                if upperList[0] == upperList[2]:
                    endCap = upperList[1]
                else:
                    endCap = upperList[2]
                endCap_find = finalStr.find(endCap)
                newFinalStr = finalStr.split(finalStr[endCap_find])
                rankList.append(newFinalStr[0])
            else:
                rankList.append("____ERROR____")

        #print(rankList)
        i = 0
        loop += 1

    #For loop to put error in missing colleges
    for num in range(testTimes - 1):
        if rankList[num] == ' ' or rankList[num] == '':
            rankList[num] = "____ERROR____"

    #printout of final ranking list (with errors included)
    #print(rankList)

    #Removes ____Error____'s from List
    i1 = 0
    global newrankList
    newrankList = []
    while i1 < (testTimes - 1):
        #print(i1)
        if rankList[i1] != "____ERROR____":
            newrankList.append(rankList[i1])
        i1 += 1

    #print("\nFinal Ranking: ")
    #print(newrankList)

    """ ###
    #Searches google to get Princeton Review colleges in string format of CF colleges
    e = 0
    newrllen = len(newrankList)
    while e < newrllen:

        query4 = "CollegeFactual" + newrankList[e]

        for k in search(query4, tld="co.in", num=1, stop=1, pause=2):
            stringURL = k

        #Adds characters of college in URL to final string variable
        finalPstr = ' '
        i9 = 40
        while i9 < (len(stringURL) - 1):
            finalPstr = finalPstr + stringURL[i9]
            i9 += 1
    
    #Conversion Function is called
    
    #Adds new formated characters to newrankList
    if finalPstr == 'virginia-polytechnic-institute-and-state-university':
        finalPstr = 'virginia-tech'
    if finalPstr == "best-colleges":
        finalPstr = "united-states-naval-academy"
    if finalPstr == "best-colleges/southwest/texas":
        finalPstr = "texas-a-and-m-university-college-station"
    if finalPstr == '':
        finalPstr = "suny-at-binghamton"
    conversionList.append(finalPstr)

    #print(newrankList)
    """

    #print("\nPrincetonReview call done")
    #print(newrankList)

#College Factual Function
def collegeFactual(pChoice, pImportance):
    global newrankList
    newrankList = []

    # Global Importance value
    global aImportance
    aImportance = pImportance

    # Searches Google to find URL of Attribute Ranking Site
    query2 = "College Factual 2024/25 Best Colleges for " + pChoice

    for j in search(query2, tld="co.in", num=1, stop=1, pause=2):
        goodURL2 = j

    #print("Hello: " + goodURL2)
    # Gets HTML Data from URL
    r = requests.get(goodURL2)
    soup = BeautifulSoup(r.text, 'html.parser')
    j = soup.find_all('a', class_="rankListHeaderText")


    # Appends colleges to newrankList
    for element in j:
        newrankList.append(element.get_text())

    #List Comprehension to convert all to lowercase
    newrankList = [x.lower() for x in newrankList]
    newrankList = [z.replace(' - ', ' ') for z in newrankList]
    newrankList = [y.replace(' ', '-') for y in newrankList]

    #print("\n CollegeFactual call done")
    #print(newrankList)

#P to CF variable conversions list:
def conversions():
    global finalListCollegesOnlyP

    finalPlist = [' UniversityofDenverDenver,', 'EmoryUniversity', 'LehighUniversity', 'FloridaState', 'VirginiaTech', 'WashingtonState', ' Auburn', ' WashingtonUniversityin', 'KansasState', 'RiceUniversity', 'TulaneUniversity', 'Hampden-Sydney', 'AngeloState', 'FranklinW.', 'ClaremontMc', 'UniversityofWisconsin-', 'CollegeoftheAtlantic', 'TheUniversityof', 'ThomasAquinas', 'Hamilton', 'Amherst', 'UniversityofCincinnatiCincinnati,', ' VanderbiltUniversity', ' GonzagaUniversity', 'ArizonaState', 'Syracuse', ' Clemson', 'BrighamYoung', 'TheOhio', 'MichiganState', 'UniversityofTex', 'ButlerUniversity', 'Wabash', 'UniversityofNotre', 'UniversityofDaytonDayton,', 'UniversityofTennessee-', 'UnitedStates', 'XavierUniversity(', ' UniversityofNebraska—', 'IowaState', ' BryantUniversity', 'UniversityofSan', 'BrynMawr', 'Lewis&', ' FloridaSouthern', 'MountHolyoke', ' SalveRegina', ' ReedCollege', ' RhodesCollege', 'RollinsCollege', ' HighPoint', 'TexasChristian', 'UniversityofPuget', 'UniversityofCalifornia—', 'PepperdineUniversity', ' LoyolaMarymount', 'AmericanUniversity', 'SimmonsUniversity', 'EmersonCollege', 'ColumbiaUniversity', 'CityUniversityof', 'EugeneLang', ' SuffolkUniversity', ' NortheasternUniversity', ' GeorgeWashington', 'TheCooper', 'UniversityofVermont', 'LoyolaUniversity', 'NewYork', ' DruryUniversity', 'JuniataCollege', "St.John's", 'DenisonUniversity', 'CaliforniaState', 'Wellesley', ' DrewUniversity', 'AgnesScott', 'St.Bonaventure', 'Bowdoin', 'Scripps', 'Pitzer', 'UniversityofKentucky', 'WheatonCollege(', 'Skidmore', ' ChristopherNewport', 'Elon', 'UniversityofMassachusetts-', 'CornellUniversity', 'BatesCollege', 'JamesMadison', ' MuhlenbergCollege', ' St.Olaf', ' Gettysburg', 'GeorgiaInstituteof', 'UniversityofVirginia', 'UniversityofMichigan—', 'NorthCarolina', 'UniversityofWashington', 'UniversityofGeorgia', 'UniversityofIllinois', ' StateUniversityof', 'MissouriUniversityof', 'William&', 'PurdueUniversity—', 'NewCollegeof', 'TexasA&', 'NewJersey', 'MassachusettsInstituteof', 'Princeton', 'Stanford', 'HarveyMudd', 'CaliforniaInstituteof', 'DartmouthCollege', 'Harvard', 'Williams', 'YaleUniversity', 'JohnsHopkins', 'CarnegieMellon', 'Universityof', 'BrownUniversity', 'Duke', 'ColgateUniversity', 'Pomona', 'MichiganTechnological', 'PennState', ' The', 'MiamiUniversity', 'OregonState', ' St.Lawrence', 'Rose-Hulman', 'WakeForest', 'Marquette', 'AustinCollege', ' HobartandWilliam', ' CollegeofWoosterWooster,', 'WorcesterPolytechnic']

    completePconversionList = ['university-of-denver', 'emory-university', 'lehigh-university', 'florida-state-university', 'virginia-tech', 'washington-state-university', 'auburn-university', 'washington-university-in-st-louis', 'kansas-state-university', 'rice-university', 'tulane-university-of-louisiana', 'hampden-sydney-college', 'angelo-state-university', 'franklin-university', 'claremont-mckenna-college', 'university-of-wisconsin-madison', 'college-of-the-atlantic', 'university-of-connecticut', 'thomas-aquinas-college', 'hamilton-college', 'amherst-college', 'university-of-cincinnati-main-campus', 'vanderbilt-university', 'gonzaga-university', 'arizona-state-university', 'syracuse-university', 'clemson-university', 'brigham-young-university-provo', 'ohio-state-university-main-campus', 'michigan-state-university', 'the-university-of-texas-at-austin', 'butler-university', 'wabash-college', 'university-of-notre-dame', 'university-of-dayton', 'the-university-of-tennessee', 'united-states-naval-academy', 'xavier-university', 'university-of-nebraska-lincoln', 'iowa-state-university', 'bryant-university', 'university-of-san-francisco', 'bryn-mawr-college', 'lewis-and-clark-college', 'florida-southern-college', 'mount-holyoke-college', 'salve-regina-university', 'reed-college', 'rhodes-college', 'rollins-college', 'high-point-university', 'texas-christian-university', 'university-of-puget-sound', 'university-of-california-berkeley', 'pepperdine-university', 'loyola-marymount-university', 'american-university', 'simmons-college', 'emerson-college', 'columbia-university-in-the-city-of-new-york', 'city-university-of-seattle', 'suny-at-binghamton', 'suffolk-university', 'northeastern-university', 'george-washington-university', 'cooper-union-for-the-advancement-of-science-and-art', 'university-of-vermont', 'loyola-university-chicago', 'new-york-university', 'drury-university', 'juniata-college', 'st-johns-university-new-york', 'denison-university', 'california-state-university-los-angeles', 'wellesley-college', 'drew-university', 'agnes-scott-college', 'saint-bonaventure-university', 'bowdoin-college', 'scripps-college', 'pitzer-college', 'university-of-kentucky', 'wheaton-college-illinois', 'skidmore-college', 'christopher-newport-university', 'elon-university', 'university-of-massachusetts-amherst', 'cornell-university', 'bates-college', 'james-madison-university', 'muhlenberg-college', 'st-olaf-college', 'gettysburg-college', 'georgia-institute-of-technology-main-campus', 'university-of-virginia-main-campus', 'university-of-michigan-ann-arbor', 'university-of-north-carolina-at-chapel-hill', 'university-of-washington-seattle-campus', 'university-of-georgia', 'university-of-illinois-at-urbana-champaign', 'suny-at-binghamton', 'university-of-missouri-columbia', 'college-of-william-and-mary', 'purdue-university-main-campus', 'the-new-school', 'texas-a-and-m-university-college-station', 'the-college-of-new-jersey', 'massachusetts-institute-of-technology', 'princeton-university', 'stanford-university', 'harvey-mudd-college', 'california-institute-of-technology', 'dartmouth-college', 'harvard-university', 'williams-college', 'yale-university', 'johns-hopkins-university', 'carnegie-mellon-university', 'university-of-connecticut', 'brown-university', 'duke-university', 'colgate-university', 'pomona-college', 'michigan-technological-university', 'pennsylvania-state-university-main-campus', 'suny-at-binghamton', 'miami-university-oxford', 'oregon-state-university', 'st-lawrence-university', 'rose-hulman-institute-of-technology', 'wake-forest-university', 'marquette-university', 'austin-college', 'hobart-william-smith-colleges', 'the-college-of-wooster', 'worcester-polytechnic-institute']

    #Loops through all of finalListCollegesOnlyP
    i = 0
    flcoplen = len(finalListCollegesOnlyP)
    while i < flcoplen:
        oneIndex = finalPlist.index(finalListCollegesOnlyP[i])

        finalListCollegesOnlyP.insert(i, completePconversionList[oneIndex])
        del finalListCollegesOnlyP[i + 1]

        i += 1


#Main function
def main():
    global finalList
    global reportfinalListC
    global reportfinalListP
    global finalListCollegesOnlyP
    global finalListCollegesOnlyC
    #global conversionList

    #Call College Factual Functions FIRST
    #College Factual Function Calls
    collegeFactual("Systems Engineering", 3)
    listA(1, "C")

    collegeFactual("Undergrad Engineering Schools", 7)
    listA(2, "C")

    collegeFactual("Overall Prestige", 5)
    listA(3, "C")

    print("\n")
    averageA("C")
    print(reportfinalListC)


    print("---------------------------------------------------------------------------------------------------------")
    

    #Princeton Review Function Calls

    princetonReview("Their Students Love these colleges", 1)
    listA(1, "P")

    princetonReview("Students love their school teams", 1)
    listA(2, "P")

    princetonReview("Campus Beauty", 1)
    listA(3, "P")

    princetonReview("Cities", 1)
    listA(4, "P")

    princetonReview("Lots of race/class interaction", 1)
    listA(5, "P")

    princetonReview("Dorms", 1)
    listA(6, "P")

    princetonReview("Food", 1)
    listA(7, "P")

    princetonReview("Public School value top 50", 1)
    listA(8, "P")

    princetonReview("Private School value top 50", 1)
    listA(9, "P")

    princetonReview("Internships Public", 1)
    listA(10, "P")

    princetonReview("Internships Private", 1)
    listA(11, "P")

    print("\n")
    conversions()
    #print(finalListCollegesOnlyP)

    print("\n")
    averageA("P")
    print(reportfinalListP)

    #Joins Lists together
    joinA()
    print("\n")
    print(reportfinalListC)

    #Returns best 10 schools
    print("\n")
    best10()


#Calls main function
main()


