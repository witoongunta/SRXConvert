
from __future__ import print_function

startLine = 0
policyCount = 177
listLine = open("testPolicies.txt").readlines()

def writePolicyCon():
    b = 0
    c = ""
    d = []
    dd = []
    e = 1
    f = 0
    g = 0
    h = 1
    i = 1
    j = 1
    k = 1
    l = ""
    global startLine
    global policyCount
    policyLine = 0
    policyName = []
    sourcesList = []
    destinationsList = []
    serviceList = []
    action = ""

    with open ("testPolicies.txt", "r") as mf:
        lines_after = mf.readlines()[startLine:]
        for lineAfter in lines_after:
            aa = lineAfter.split()
            dd.append(aa)
            policyName.append(aa[8])
        #print("policyname:", end="")
        #print(policyName)
        #print()

    while policyName[f] == policyName[e]:
        policyLine += 1
        e += 1
        f += 1

    while g <= policyLine:
        for y in dd[b]:
            c += y
            c += " "
            data = c.split()

        if data[10] == "source-address":
            sourcesList.append(data[11])
        elif data[10] == "destination-address":
            destinationsList.append(data[11])
        elif data[10] == "application":
            serviceList.append(data[11])
        elif data[10] == "permit":
            action = "Accept"
        elif data[10] == "deny":
            action = "Drop"

        c = ""
        b += 1
        e += 1
        g += 1
    """
    print("policyName: " + data[8])
    print(sourcesList)
    print(destinationsList)
    print(serviceList)
    print(action)
    """
    #mgmt_cli add access-rule layer "Network" position 22 source.1 "ThaiCert_DC" source.2 "ThaiCert_DR" destination.1 "ThaiCert" destination.2 "ThaiCert_TCP50" destination.3 "ThaiCert_UDP4500" destination.4 "ThaiCert_UDP500" service "Any" action "Accept" track "Log" -s id.txt
    #mgmt_cli add access-rule layer "Network" position 1 name "Rule 1" service.1 "SMTP" service.2 "AOL"
    policyCount += 1
    print("mgmt_cli add access-rule layer \"Network\" position " + str(policyCount), end=" ")
    #print(position, end = " ")
    print("name \"" + data[8] + "\" ", end = "")

    for source in sourcesList:
        print("sources." + str(h) + " \"" + source + "\"", end=" ")
        h += 1

    for destination in destinationsList:
        print("destination." + str(i) + " \"" + destination + "\"", end=" ")
        i += 1

    for service in serviceList:
        print("service." + str(j) + " \"" + service + "\"", end=" ")
        j += 1

    print("action \"" + action + "\" " + "track \"Log\" -s id.txt")

    startLine += policyLine + 1

def writeLastPolicy():
    b = 0
    c = ""
    d = []
    dd = []
    e = 1
    f = 0
    g = 0
    h = 1
    i = 1
    j = 1
    k = 1
    l = ""
    global startLine
    global listLine
    global policyCount
    policyLine = 0
    policyName = []
    sourcesList = []
    destinationsList = []
    serviceList = []
    action = ""

    with open ("testPolicies.txt", "r") as mf:
        lines_after = mf.readlines()[startLine:]
        for lineAfter in lines_after:
            aa = lineAfter.split()
            dd.append(aa)
            policyName.append(aa[8])
        #print("policyname:", end="")
        #print(policyName)
        #print()

    policyLine = len(listLine) - startLine

    while g <= policyLine -1:
        for y in dd[b]:
            c += y
            c += " "
            data = c.split()

        if data[10] == "source-address":
            sourcesList.append(data[11])
        elif data[10] == "destination-address":
            destinationsList.append(data[11])
        elif data[10] == "application":
            serviceList.append(data[11])
        elif data[10] == "permit":
            action = "Accept"
        elif data[10] == "deny":
            action = "Drop"

        c = ""
        b += 1
        e += 1
        g += 1
    """
    print("policyName: " + data[8])
    print(sourcesList)
    print(destinationsList)
    print(serviceList)
    print(action)
    """
    #mgmt_cli add access-rule layer "Network" position 22 source.1 "ThaiCert_DC" source.2 "ThaiCert_DR" destination.1 "ThaiCert" destination.2 "ThaiCert_TCP50" destination.3 "ThaiCert_UDP4500" destination.4 "ThaiCert_UDP500" service "Any" action "Accept" track "Log" -s id.txt
    #mgmt_cli add access-rule layer "Network" position 1 name "Rule 1" service.1 "SMTP" service.2 "AOL"
    policyCount += 1
    print("mgmt_cli add access-rule layer \"Network\" position " + str(policyCount), end=" ")
    #print(position, end = " ")
    print("name \"" + data[8] + "\" ", end = "")

    for source in sourcesList:
        print("sources." + str(h) + " \"" + source + "\"", end=" ")
        h += 1

    for destination in destinationsList:
        print("destination." + str(i) + " \"" + destination + "\"", end=" ")
        i += 1

    for service in serviceList:
        print("service." + str(j) + " \"" + service + "\"", end=" ")
        j += 1

    print("action \"" + action + "\" " + "track \"Log\" -s id.txt")

    startLine += policyLine + 1

def printPoliciesDetail():
    while startLine < len(listLine):
        print("startline: ", end="")
        print(startLine)
        try:
            writePolicyCon()
        except IndexError:
            writeLastPolicy()
        print("position: " + str(policyCount))
        print()

def printPolicies():
    while startLine < len(listLine):
        try:
            writePolicyCon()
        except IndexError:
            writeLastPolicy()


printPolicies()
