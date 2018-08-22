
inputs = {}
'''
inputs["Harry"] = 37.21
inputs["Berry"] = 37.21
inputs["Tina"] = 37.2
inputs["Akriti"] = 41
inputs["Harsh"] = 39
'''
'''
inputs["Prashant"] = 40
inputs["Pallavi"] = 39
inputs["Dheeraj"] = 36
inputs["Shivam"] = 39
'''
inputs["Prashant"] = 52.22
inputs["Kush"] = 52.223
inputs["Kant"] = 52.222
inputs["Kanti"] = 52.2222
inputs["Harshit"] = 52.22222

if __name__ == '__main__':
    myIndex = {}
    maxItems = 2
    for name, score in inputs.items():
        if len(myIndex)<1:
            myIndex[maxItems-1] = {}
            myIndex[maxItems-1]["score"] = score
            myIndex[maxItems-1]["names"] = []
            myIndex[maxItems-1]["names"].append(name)
            continue

        for i in reversed(range(maxItems)):
            if i not in myIndex.keys() or "score" not in myIndex[i].keys():
                break
            if score == myIndex[i]["score"] and name not in myIndex[i]["names"]:
                myIndex[i]["names"].append(name)
            elif score < myIndex[i]["score"] and i>0:
                if i-1>=0 and (i-1 not in myIndex.keys() or "score" not in myIndex[i-1].keys()):
                    myIndex[i-1] = {}
                myIndex[i-1]["score"] = myIndex[i]["score"]
                myIndex[i-1]["names"] = myIndex[i]["names"]
                myIndex[i]["score"] = score
                myIndex[i]["names"] = []
                myIndex[i]["names"].append(name)
            elif i-1>=0:
                if (i-1 not in myIndex.keys() or "score" not in myIndex[i-1].keys()) or myIndex[i-1]["score"] > score:
                    myIndex[i-1] = {}
                    myIndex[i-1]["names"] = []
                elif myIndex[i-1]["score"]<score:
                    continue
                myIndex[i-1]["score"] = score
                myIndex[i-1]["names"].append(name)

    if len(myIndex)==2:
        o = myIndex[0]["names"]
        o.sort()
        for n in o:
            print("%s" % (n))  