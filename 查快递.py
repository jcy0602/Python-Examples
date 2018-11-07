import json,requests,os

def searchPackage():
    packageNum = input("请输入运单号码:")
    url1 = "http://www.kuaidi100.com/autonumber/autoComNum?resultv2=1&text="+packageNum
    companyName = json.loads(requests.get(url1).text)["auto"][0]["comCode"]
    print("快递公司："+companyName)
    url2 = "http://www.kuaidi100.com/query?type="+companyName+"&postid="+packageNum
    print("时间                  地点和跟踪进度\n")
    for item in json.loads(requests.get(url2).text)["data"]:
        if item["time"]:
            print(item["time"],item["context"])
        else:
            print(item["message"])

searchPackage()
os.system("pause")