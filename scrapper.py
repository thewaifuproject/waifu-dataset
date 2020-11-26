import requests, json, shutil

finalId = 32796 #17268

waifus = [] #json.loads(open("waifus.json", 'r').read())
for waifuId in range(1, finalId):
    try:
        r=requests.get("https://mywaifulist.moe/api/waifu/"+str(waifuId), headers={'x-requested-with': 'XMLHttpRequest'})
        if (r.text!=""):
            waifu=r.json()
            print("Scrapped "+waifu["name"])
            imageURL=requests.get("https://mywaifulist.moe/api/waifu/"+str(waifuId)+"/gallery?page=0", headers={'x-requested-with': 'XMLHttpRequest'}).json()["data"][0]["path"]
            #imageURL=waifu["display_picture"].replace("_thumb", "")
            waifuFile=str(waifuId)
            imageData=requests.get(imageURL, stream=True)
            with open("images/"+waifuFile, "wb") as f:
                imageData.raw.decode_content = True
                shutil.copyfileobj(imageData.raw, f)
            waifu["display_picture"]=imageURL
            waifus.append(waifu)
            open("waifus.json", "w+").write(json.dumps(waifus))
    except:
        pass
