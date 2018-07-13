import requests, json

global profile_list
profile_list = []
with open("profiles.txt","r") as file:
    for profile in file:
        profile_list.append(profile[:-1])
global logins_undftd
logins_undftd = []
with open("logins_undftd.txt","r") as file:
    for line in file:
        login = {}
        login.update({"username":line.split(":")[0]})
        login.update({"password":line.split(":")[1][:-1]})
        logins_undftd.append(login.copy())
def getLogin():
    l = logins_undftd[0]
    logins_undftd.append(logins_undftd[0])
    logins_undftd.pop(0)
    return l
global size_list
size_list = []
with open("sizes.txt","r") as file:
    for line in file:
        size_list.append(line[:-1])
def getSize():
    size = size_list[0]
    size_list.append(size_list[0])
    size_list.pop(0)
    return size
def getProfile():
    p = profile_list[0]
    profile_list.append(profile_list[0])
    profile_list.pop(0)
    return p
site = raw_input('''
################################### ~ CHOOSE A SITE BY ENTERING SITE NAME EXACTLY AS SHOWN BELOWN ~ #################################################

12amrun             18montrose          A-Ma-Maniere        APBStore                AddictMiami         AntiSocialSocialClub        Attic
BBCIceCream         BBCIceCreamEU       Bape*               Beatniconline           BlackMarketUS       Blends                      Bodega
BowsAndArrows       BurnRubber          Commonwealth        Concepts                CrtsdSnkrs          DSM-EU                      DSM-JP
DSM-SG              DSM-US              DreamTown*          EllenShop               Exclucity           ExtraButter                 FearOfGod
Feature             FiceGallery         FunkoShop*          GoodAsGold              GraffitiPrints      HanonShop                   Haven
HighsAndLows        HistoryOfNY         Hotoveli            JustDon                 JustinTimberlake    Kith                        KylieCosmetics
LaceUpNYC           LapstoneAndHammer   LessOneSeven        Livestock               Machus              MarathonSports              MiniShopMadrid
NRML                Noirfonce           Nomad*              Notre                   ObeyGiant           OctobersVeryOwnCA*          OctobersVeryOwnUK
OctobersVeryOwnUS*  OffTheHook          Oipolloi            Omocat                  Oneness287          PackerShoes                 PalaceUS
Par5MilanoYeezy     Places+Faces        ProperLBC           RSVPGallery             ReigningChamp       Renarts                     RimeNYC
Rise45              RockCityKicks       RoninDivision       RonnieFieg              SaintAlfred         ShoeGalleryMiami            ShopNiceKicks
SneakerPolitics     SneakerWorldShop    SocialStatusPHG     Solefly                 Soleheaven          Stampd                      StaplePigeon
StoneIsland         Suede               TheClosetInc        TheDarkSideInitiative   TravisScott*        TrophyRoom                  Undefeated
Unknwn              Vlone               WishATL             WorldOfHombre           Xhibition           YeezySupply

######################################################################################################################################################
################################## You may enter more than one site like this Kith, HanonShop, Undefeated ############################################
######################################################################################################################################################

>> ''')
site_list = []
if "," in site:
    site_list = site.split(",")
global sites
sites = []
for site in site_list:
    for i in range(0,len(size_list)):
        sites.append(site)
def getSite():
    s = sites[0]
    sites.append(sites[0])
    sites.pop(0)
    return s
maxtasks = raw_input("How many tasks? >>")
maxtasks = int(maxtasks)
captcha = raw_input('''
1 - No captcha
2 - Captcha
''')
if captcha == "1":
    hasCaptcha = False
else:
    hasCaptcha = True
keywords = raw_input('''
Please type in your keywords (i.e. +jordan,+off,+white,+1)
''')
if site == "Undefeated":
    useAccount = True
else:
    useAccount = False
tasks = []
count = 0
for i in range(0,maxtasks):

    task = {}
    task.update({"atcQuantity":""})
    task.update({"checkoutMode":"old"})
    task.update({"hasCaptcha":hasCaptcha})
    task.update({"id":count})
    task.update({"monitorInput":keywords})
    task.update({"monitorType":"keywords"})
    task.update({"newProductsOnly":False})
    task.update({"password":getLogin()["password"]})
    task.update({"profile":getProfile()})
    task.update({"scheduleTask":False})
    task.update({"scheduleTime":""})
    if len(site_list) > 1:
        task.update({"site":getSite()})
    else:
        task.update({"site":site})
    task.update({"size":getSize()})
    for site in sites:
        if "Undefeated" in site:
            useAccount = True
            continue
        else:
            useAccount = False
    task.update({"useAccount":useAccount})
    task.update({"username":getLogin()["username"]})
    tasks.append(task.copy())
    print task
    print tasks
    print
    count = count + 1
with open("Generated Tasks.json","w") as file:
    json.dump(tasks,file)
