#zápis, klasifikácia a výpočty dát
import pandas as pd
import numpy as np
import csv
#časť, ktorá sa venovala zápisu a klasifikácii dát, teraz už nie je potrebná iba, ak by sme chceli aktualizovať databázu o šampiónoch (je po riadok 403)
meno_championa = "zyra"
index = 1
winrate_data_with = pd.read_csv('data\winratedatawith.txt', index_col ="champion")
winrate_data_directmatchup = pd.read_csv('data\winratedatadirectmatchup.txt', index_col ="champion")
winrate_data_indirectmatchup = pd.read_csv('data\winratedataindirectmatchup.txt', index_col ="champion")
winlose = pd.read_csv('data\winlose.txt')
predictdata = pd.read_csv('data\predictdata.txt')
predictdatanew = pd.read_csv('data\predictdatanew.txt')
predictdatafinal = pd.read_csv('data\predictdatafinal.txt')
predictdataoldfinal = pd.read_csv('data\predictdataoldfinal.txt')

winn = pd.read_csv('championwinrate13.1.txt', delimiter='\t')
winnn = winn.iloc[:,6]
winnnn = winn.iloc[:,1]
winn = pd.DataFrame(winn.Champion.str.split(' ',1).tolist(),
                                 columns = ['Champion','Winrate'])
winn['Winrate'] = winnn
winn['Picks'] = winnnn
championwinrate = winn[winn['Picks'] > 6] 


championwinrate.loc[:,'Champion'] = championwinrate['Champion'].apply(str.lower)


predictdata = predictdata.drop(columns=["Unnamed: 0"])
predictdatanew = predictdatanew.drop(columns=["Unnamed: 0"])
predictdatafinal = predictdatafinal.drop(columns=["Unnamed: 0"])
predictdataoldfinal = predictdataoldfinal.drop(columns=["Unnamed: 0"])
data = pd.read_csv('data\\' + meno_championa + ".txt")

championwinrate.loc[:, 'Winrate'] = championwinrate['Winrate'].str.rstrip('%').astype('float')



data_reduced = data.drop(columns=["CSD@15","GD@15","XPD@15","KDA"])

teams = pd.read_csv('teams.txt', index_col ="teamside")
winner = pd.read_csv('data\winner.txt', index_col ="teamside")

top = "malphite"
jg = "olaf"
mid = "lissandra"
bot ="ezreal"
sup = "leona"

totalgames = 0
totalwinrate = 0

teams.top = top
teams.jg = jg
teams.mid = mid
teams.bot = bot
teams.sup = sup

champions=data_reduced.iloc[:,0]
champions=np.array(champions) 


winrate=data_reduced.iloc[:,3]
winrate=np.array(winrate)

games=data_reduced.iloc[:,2]
games=np.array(games)

gankergames = 0
gankerwinrate = 0
engagegames = 0
engagewinrate = 0
lanerwinrate = 0
lanergames = 0
splitpushergames = 0
splitpusherwinrate = 0
teamfightdamagegames = 0
teamfightdamagewinrate = 0
teamfightccwinrate = 0
teamfightccgames = 0
clearerwinrate = 0
clearergames = 0
assasinwinrate = 0
assasingames = 0
roamerwinrate = 0
roamergames = 0
pokerwinrate = 0
pokergames = 0
fighterwinrate = 0
fightergames = 0
utilitywinrate = 0
utilitygames = 0
fronttobackwinrate = 0
fronttobackgames = 0
peelwinrate = 0
peelgames = 0
enchanterwinrate = 0
enchantergames = 0
scalerwinrate = 0
scalergames = 0
latewinrate = 0
lategames = 0

                         
for i in range(len(champions)):
    if champions[i] == " Aatrox": champions[i] = "teamfightdamage"
    if champions[i] == " Ahri": champions[i] = "roamer"
    if champions[i] == " Akali": champions[i] = "teamfightdamage"
    if champions[i] == " Akshan": champions[i] = "laner"
    if champions[i] == " Alistar": champions[i] = "engage"
    if champions[i] == " Amumu": champions[i] = "teamfightcc"
    if champions[i] == " Anivia": champions[i] = "teamfightcc"
    if champions[i] == " Annie": champions[i] = "teamfightcc"
    if champions[i] == " Aphelios": champions[i] = "fronttoback"
    if champions[i] == " Ashe": champions[i] = "utility"
    if champions[i] == " Aurelion Sol": champions[i] = "roamer"
    if champions[i] == " Azir": champions[i] = "scaler"
    if champions[i] == " Bard": champions[i] = "roamer"
    if champions[i] == " Blitzcrank": champions[i] = "engage"
    if champions[i] == " Brand": champions[i] = "teamfightdamage"
    if champions[i] == " Braum": champions[i] = "peel"
    if champions[i] == " Cailtyn": champions[i] = "fronttoback"
    if champions[i] == " Camille": champions[i] = "splitpusher"
    if champions[i] == " Cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == " Cho'Gath": champions[i] = "teamfightcc"
    if champions[i] == " Corki": champions[i] = "scaler"
    if champions[i] == " Darius": champions[i] = "laner"
    if champions[i] == " Diana": champions[i] = "clearer"
    if champions[i] == " Draven": champions[i] = "fighter"
    if champions[i] == " Dr.Mundo": champions[i] = "teamfightcc"
    if champions[i] == " Ekko": champions[i] = "teamfightdamage"
    if champions[i] == " Elise": champions[i] = "ganker"
    if champions[i] == " Evelynn": champions[i] = "teamfightdamage"
    if champions[i] == " Ezreal": champions[i] = "poker"
    if champions[i] == " Fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == " Fiora": champions[i] = "splitpusher"
    if champions[i] == " Fizz": champions[i] = "roamer"
    if champions[i] == " Gallo": champions[i] = "teamfightcc"
    if champions[i] == " Gangplank": champions[i] = "teamfightdamage"
    if champions[i] == " Garen": champions[i] = "splitpusher"
    if champions[i] == " Gnar": champions[i] = "teamfightcc"
    if champions[i] == " Gragas": champions[i] = "teamfightcc"
    if champions[i] == " Graves": champions[i] = "clearer"
    if champions[i] == " Gwen": champions[i] = "splitpusher"
    if champions[i] == " Hecarim": champions[i] = "clearer"
    if champions[i] == " Heimerdinger": champions[i] = "laner"
    if champions[i] == " Illaoi": champions[i] = "splitpusher"
    if champions[i] == " Irelia": champions[i] = "laner"
    if champions[i] == " Ivern": champions[i] = "ganker"
    if champions[i] == " Janna": champions[i] = "enchanter"
    if champions[i] == " Jarvan IV": champions[i] = "ganker"
    if champions[i] == " Jax": champions[i] = "splitpusher"
    if champions[i] == " Jayce": champions[i] = "laner"
    if champions[i] == " Jhin": champions[i] = "fronttoback"
    if champions[i] == " Jinx": champions[i] = "fronttoback"
    if champions[i] == " Kai'Sa": champions[i] = "fighter"
    if champions[i] == " Kalista": champions[i] = "fighter"
    if champions[i] == " Karma": champions[i] = "enchanter"
    if champions[i] == " Karthus": champions[i] = "teamfightdamage"
    if champions[i] == " Kassadin": champions[i] = "scaler"
    if champions[i] == " Katarina": champions[i] = "roamer"
    if champions[i] == " Kayle": champions[i] = "scaler"
    if champions[i] == " Kayn": champions[i] = "late"
    if champions[i] == " Kennen": champions[i] = "teamfightdamage"
    if champions[i] == " Kha'Zix": champions[i] = "assasin"
    if champions[i] == " Kindred": champions[i] = "late"
    if champions[i] == " Kled": champions[i] = "laner"
    if champions[i] == " Kog'Maw": champions[i] = "fronttoback"
    if champions[i] == " LeBlanc": champions[i] = "assasin"
    if champions[i] == " Lee Sin": champions[i] = "ganker"
    if champions[i] == " Leona": champions[i] = "engage"
    if champions[i] == " Lillia": champions[i] = "teamfightcc"
    if champions[i] == " Lissandra": champions[i] = "teamfightcc"
    if champions[i] == " Lucian": champions[i] = "fighter"
    if champions[i] == " Lulu": champions[i] = "enchanter"
    if champions[i] == " Lux": champions[i] = "teamfightdamage"
    if champions[i] == " Malphite": champions[i] = "teamfightcc"
    if champions[i] == " Malzahar": champions[i] = "teamfightcc"
    if champions[i] == " Maokai": champions[i] = "teamfightcc"
    if champions[i] == " Master Yi": champions[i] = "teamfightdamage"
    if champions[i] == " Miss Fortune": champions[i] = "fronttoback"
    if champions[i] == " Mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == " Morgana": champions[i] = "peel"
    if champions[i] == " Nami": champions[i] = "enchanter"
    if champions[i] == " Nasus": champions[i] = "splitpusher"
    if champions[i] == " Nautilus": champions[i] = "engage"
    if champions[i] == " Neeko": champions[i] = "teamfightcc"
    if champions[i] == " Nidalee": champions[i] = "ganker"
    if champions[i] == " Nocturne": champions[i] = "ganker"
    if champions[i] == " Nunu & Willump": champions[i] = "ganker"
    if champions[i] == " Olaf": champions[i] = "teamfightdamage"
    if champions[i] == " Orianna": champions[i] = "teamfightcc"
    if champions[i] == " Ornn": champions[i] = "teamfightcc"
    if champions[i] == " Pantheon": champions[i] = "engage"
    if champions[i] == " Poppy": champions[i] = "teamfightcc"
    if champions[i] == " Pyke": champions[i] = "assasin"
    if champions[i] == " Qiyana": champions[i] = "assasin"
    if champions[i] == " Quinn": champions[i] = "splitpusher"
    if champions[i] == " Rakan": champions[i] = "peel"
    if champions[i] == " Rammus": champions[i] = "teamfightcc"
    if champions[i] == " Rek'Sai": champions[i] = "ganker"
    if champions[i] == " Rell": champions[i] = "peel"
    if champions[i] == " Renata Glasc": champions[i] = "peel"
    if champions[i] == " Renekton": champions[i] = "laner"
    if champions[i] == " Rengar": champions[i] = "assasin"
    if champions[i] == " Riven": champions[i] = "splitpusher"
    if champions[i] == " Rumble": champions[i] = "teamfightdamage"
    if champions[i] == " Ryze": champions[i] = "scaler"
    if champions[i] == " Samira": champions[i] = "fighter"
    if champions[i] == " Sejuani": champions[i] = "teamfightcc"
    if champions[i] == " Senna": champions[i] = "utility"
    if champions[i] == " Seraphine": champions[i] = "enchanter"
    if champions[i] == " Sett": champions[i] = "laner"
    if champions[i] == " Shaco": champions[i] = "assasin"
    if champions[i] == " Shen": champions[i] = "peel"
    if champions[i] == " Shyvana": champions[i] = "teamfightdamage"
    if champions[i] == " Singed": champions[i] = "splitpusher"
    if champions[i] == " Sion": champions[i] = "splitpusher"
    if champions[i] == " Sivir": champions[i] = "fronttoback"
    if champions[i] == " Skarner": champions[i] = "teamfightcc"
    if champions[i] == " Sona": champions[i] = "enchanter"
    if champions[i] == " Soraka": champions[i] = "enchanter"
    if champions[i] == " Swain": champions[i] = "teamfightdamage"
    if champions[i] == " Sylas": champions[i] = "scaler"
    if champions[i] == " Syndra": champions[i] = "teamfightdamage"
    if champions[i] == " Tahm Kench": champions[i] = "peel"
    if champions[i] == " Tallyah": champions[i] = "teamfightdamage"
    if champions[i] == " Talon": champions[i] = "assasin"
    if champions[i] == " Taric": champions[i] = "peel"
    if champions[i] == " Teemo": champions[i] = "splitpusher"
    if champions[i] == " Thresh": champions[i] = "peel"
    if champions[i] == " Tristana": champions[i] = "fighter"
    if champions[i] == " Trundle": champions[i] = "ganker"
    if champions[i] == " Tryndamere": champions[i] = "splitpusher"
    if champions[i] == " Twisted Fate": champions[i] = "roamer"
    if champions[i] == " Twitch": champions[i] = "assasin"
    if champions[i] == " Udyr": champions[i] = "clearer"
    if champions[i] == " Urgot": champions[i] = "splitpusher"
    if champions[i] == " Varus": champions[i] = "poker"
    if champions[i] == " Vayne": champions[i] = "fighter"
    if champions[i] == " Veigar": champions[i] = "teamfightcc"
    if champions[i] == " Vel'Koz": champions[i] = "teamfightdamage"
    if champions[i] == " Vex": champions[i] = "roamer"
    if champions[i] == " Vi": champions[i] = "teamfightcc"
    if champions[i] == " Viego": champions[i] = "teamfightdamage"
    if champions[i] == " Viktor": champions[i] = "scaler"
    if champions[i] == " Vladimir": champions[i] = "scaler"
    if champions[i] == " Volibear": champions[i] = "ganker"
    if champions[i] == " Warwick": champions[i] = "ganker"
    if champions[i] == " Wukong": champions[i] = "teamfightcc"
    if champions[i] == " Xayah": champions[i] = "fronttoback"
    if champions[i] == " Xerath": champions[i] = "teamfightdamage"
    if champions[i] == " Xin Zhao": champions[i] = "ganker"
    if champions[i] == " Yasuo": champions[i] = "teamfightdamage"
    if champions[i] == " Yone": champions[i] = "teamfighdamage"
    if champions[i] == " Yorick": champions[i] = "splitpusher"
    if champions[i] == " Yuumi": champions[i] = "enchanter"
    if champions[i] == " Zac": champions[i] = "teamfightcc"
    if champions[i] == " Zed": champions[i] = "assasin"
    if champions[i] == " Zeri": champions[i] = "fronttoback"
    if champions[i] == " Ziggs": champions[i] = "teamfightdamage"
    if champions[i] == " Zilean": champions[i] = "peel"
    if champions[i] == " Zoe": champions[i] = "roamer"
    if champions[i] == " Zyra": champions[i] = "teamfightdamage"
    


data_reduced["Champion"] = champions


for i in range(len(champions)):
    if champions[i] == "ganker":
        gankergames = gankergames + int(games[i])
        gankerwinrate = gankerwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "laner":
        lanergames = lanergames + int(games[i])
        lanerwinrate = lanerwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "splitpusher":
        splitpushergames = splitpushergames + int(games[i])
        splitpusherwinrate = splitpusherwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "teamfightdamage":
        teamfightdamagegames = teamfightdamagegames + int(games[i])
        teamfightdamagewinrate = teamfightdamagewinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "teamfightcc":
        teamfightccgames = teamfightccgames + int(games[i])
        teamfightccwinrate = teamfightccwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "clearer":
        clearergames = clearergames + int(games[i])
        clearerwinrate = clearerwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "assasin":
        assasingames = assasingames + int(games[i])
        assasinwinrate = assasinwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "late":
        lategames = lategames + int(games[i])
        latewinrate = latewinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "scaler":
        scalergames = scalergames + int(games[i])
        scalerwinrate = scalerwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "roamer":
        roamergames = roamergames + int(games[i])
        roamerwinrate = roamerwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "poker":
        pokergames = pokergames + int(games[i])
        pokerwinrate = pokerwinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "fighter":
        fightergames = fightergames + int(games[i])
        fighterwinrate = fighterwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "utility":
        utilitygames = utilitygames + int(games[i])
        utilitywinrate = utilitywinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "fronttoback":
        fronttobackgames = fronttobackgames + int(games[i])
        fronttobackwinrate = fronttobackwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "engage":
        engagegames = engagegames + int(games[i])
        engagewinrate = engagewinrate + (int(winrate[i]) * int(games[i]))

    if champions[i] == "peel":
        peelgames = peelgames + int(games[i])
        peelwinrate = peelwinrate + (int(winrate[i]) * int(games[i]))
        
    if champions[i] == "enchanter":
        enchantergames = enchantergames + int(games[i])
        enchanterwinrate = enchanterwinrate + (int(winrate[i]) * int(games[i]))

    
if gankergames > 0:
        gankerwinrate = gankerwinrate / gankergames

if lanergames > 0:
        lanerwinrate = lanerwinrate / lanergames

if splitpushergames > 0:
        splitpusherwinrate = splitpusherwinrate / splitpushergames

if teamfightdamagegames > 0:
        teamfightdamagewinrate = teamfightdamagewinrate / teamfightdamagegames

if teamfightccgames > 0:
        teamfightccwinrate = teamfightccwinrate / teamfightccgames

if clearergames > 0:
        clearerwinrate =clearerwinrate / clearergames

if assasingames > 0:
        assasinwinrate = assasinwinrate / assasingames

if lategames > 0:
        latewinrate = latewinrate / lategames

if scalergames > 0:
        scalerwinrate = scalerwinrate / scalergames

if roamergames > 0:
        roamerwinrate = roamerwinrate / roamergames

if pokergames > 0:
        pokerwinrate = pokerwinrate / pokergames

if fightergames > 0:
        fighterwinrate = fighterwinrate / fightergames

if utilitygames > 0:
        utilitywinrate = utilitywinrate / utilitygames

if fronttobackgames > 0:
        fronttobackwinrate = fronttobackwinrate / fronttobackgames

if engagegames > 0:
        engagewinrate = engagewinrate / engagegames

if peelgames > 0:
        peelwinrate = peelwinrate / peelgames

if enchantergames > 0:
        enchanterwinrate = enchanterwinrate / enchantergames





winrate_data_indirectmatchup.loc[meno_championa] = [gankergames,gankerwinrate,engagegames,engagewinrate,lanerwinrate,lanergames,splitpushergames,splitpusherwinrate,teamfightdamagegames,teamfightdamagewinrate,teamfightccwinrate,teamfightccgames,clearerwinrate,clearergames,assasinwinrate,assasingames,roamerwinrate,roamergames,pokerwinrate,pokergames,fighterwinrate,fightergames,utilitywinrate,utilitygames,fronttobackwinrate,fronttobackgames,peelwinrate,peelgames,enchanterwinrate,enchantergames,scalerwinrate,scalergames,latewinrate,lategames]

winrate_data_indirectmatchup = winrate_data_indirectmatchup.dropna()
winrate_data_indirectmatchup.to_csv('data\winratedataindirectmatchup.txt')

#Začiatok výpočtovej časti kódu

teams = pd.read_csv('teams.txt', index_col ="teamside")

index = len(predictdatanew) 
indexx = len(predictdata) 
indexxx = len(predictdatafinal)
indexxxx = len(predictdataoldfinal)

# #Tu je miesto na vypočítanie nových prípadov
# #Treba zadať ranking tímu 1 a 2. Označiť víťaza je potrebné iba ak zadávame nové dáta na trénovanie modelu (Ak vyhral prvý tím, tak 1 ak druhý, tak 0).
# #Treba zadať 5 šampiónov, ktorý hrajú v prvom tíme a 5 šampiónov z druhého tímu
# #Výsledok bude vypísaný do konzoli a zároveň zapísaný na vrch všetkých 4 textových súborov 8,18,32,42. 
# #Názvy súborov :
# 8 - predictdata.txt
# 18 - predictdataoldfinal.txt
# 32 - predictdatanew.txt
# 42 - predictdatafinal.txt
team1rankingSS = 0
team1rankingS = 1
team1rankingA = 0
team1rankingB = 0
team1rankingC = 0
team1rankingD = 0
team2rankingSS = 0
team2rankingS = 0
team2rankingA = 1
team2rankingB = 0
team2rankingC = 0
team2rankingD = 0

team1ranking = 3
team2ranking = 3
winner = 1


patch = "13.3"


top = "gnar"
jg  = "leesin"
mid = "akali"
bot = "caitlyn"
sup = "lux"

top_enemy = "fiora"
jg_enemy = "vi"
mid_enemy = "ryze"
bot_enemy = "ezreal"
sup_enemy = "karma"

top2 = top
jg2 = jg
mid2 = mid
bot2 = bot
sup2 = sup

top_enemy2 = top_enemy
jg_enemy2 = jg_enemy
mid_enemy2 = mid_enemy
bot_enemy2 = bot_enemy
sup_enemy2 = sup_enemy

totalgames = 0
totalwinrate = 0

if len(winrate_data_with.columns) > 34:
    winrate_data_with = winrate_data_with.drop(columns=["Unnamed: 0"])
if len(winrate_data_with.columns) > 34:
    winrate_data_with = winrate_data_with.drop(columns=["Unnamed: 0.1"])

#táto časť sa venuje výpočtom pre kompatibilitný winrate

champions_team1=winlose.iloc[0,:]
champions_team2=winlose.iloc[0,:]
champions=winlose.iloc[0,:]
champions["top"] = top2
champions["jg"] = jg2
champions["mid"] = mid2
champions["bot"] = bot2
champions["sup"] = sup2

top = winrate_data_with.loc[top]
jg = winrate_data_with.loc[jg]
mid = winrate_data_with.loc[mid]
bot = winrate_data_with.loc[bot]
sup = winrate_data_with.loc[sup]

gamess = 0
winratee = 0


win131 = pd.read_csv(patch + ".txt")

win131.loc[:,'Champion'] = win131['Champion'].apply(str.lower)
win131.loc[:, 'Winrate'] = win131['Winrate'].str.rstrip('%').astype('float')

for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "belveth": champions[i] = "teamfightdamage"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    #if champions[i] == "ksante": champions[i] = "teamfightcc"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"
champions_team1 = champions
idk = champions.iloc[:]
idk = idk.drop("top")


for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    
    team1compatibilitywinratetop = winratee / gamess
if( gamess < 40):
    team1compatibilitywinratetop = 50
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("bot")
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team1compatibilitywinratebot = winratee / gamess
if( gamess < 40):
    team1compatibilitywinratebot = 50
gamess = 0
winratee = 0
idk = champions.iloc[:]
idk = idk.drop("jg")

for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team1compatibilitywinratejg = winratee / gamess
if( gamess < 40):
    team1compatibilitywinratejg = 50
  
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("mid")
       
for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team1compatibilitywinratemid = winratee / gamess
if( gamess <= 40):
    team1compatibilitywinratemid = 50
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("sup")
       
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee 
team1compatibilitywinratesup = winratee / gamess
if( gamess < 40):
    team1compatibilitywinratesup = 50
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")

team1compatibilitygames = totalgames
team1compatibilitywinrate =  totalwinrate / totalgames

totalwinrate = 0
totalgames = 0



champions=winlose.iloc[0,:]
champions["top"] = top_enemy2
champions["jg"] = jg_enemy2
champions["mid"] = mid_enemy2
champions["bot"] = bot_enemy2
champions["sup"] = sup_enemy2

top = winrate_data_with.loc[top_enemy]
jg = winrate_data_with.loc[jg_enemy]
mid = winrate_data_with.loc[mid_enemy]
bot = winrate_data_with.loc[bot_enemy]
sup = winrate_data_with.loc[sup_enemy].copy()


gamess = 0
winratee = 0


for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"
champions_team2 = champions
idk = champions.iloc[:]
idk = idk.drop("top")

for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team2compatibilitywinratetop = winratee / gamess
if( gamess < 40):
    team2compatibilitywinratetop = 50
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("bot")
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team2compatibilitywinratebot = winratee / gamess
if( gamess < 40):
    team2compatibilitywinratebot = 50
gamess = 0
winratee = 0
idk = champions.iloc[:]
idk = idk.drop("jg")

for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team2compatibilitywinratejg = winratee / gamess
if( gamess < 40):
    team2compatibilitywinratejg = 50    
  
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("mid")
       
for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team2compatibilitywinratemid = winratee / gamess
if( gamess < 40):
    team2compatibilitywinratemid = 50  
gamess = 0
winratee = 0
        
idk = champions.iloc[:]
idk = idk.drop("sup")
       
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee 
    team2compatibilitywinratesup = winratee / gamess
if( gamess < 40):
    team2compatibilitywinratesup = 50  
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")

team2compatibilitygames = totalgames
team2compatibilitywinrate =  totalwinrate / totalgames


totalwinrate = 0
totalgames = 0




#táto časť sa venuje výpočtom pre winratu priamych súbojov





champions=winlose.iloc[0,:]
champions["top"] = top2
champions["jg"] = jg2
champions["mid"] = mid2
champions["bot"] = bot2
champions["sup"] = sup2

top = winrate_data_directmatchup.loc[top2]
jg = winrate_data_directmatchup.loc[jg2]
mid = winrate_data_directmatchup.loc[mid2]
bot = winrate_data_directmatchup.loc[bot2]
sup = winrate_data_directmatchup.loc[sup2]

gamess = 0
winratee = 0


for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "belveth": champions[i] = "teamfightdamage"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"

idk = champions_team2.iloc[:]
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("bot")
idk = idk.drop("sup")


for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
if (gamess > 0):
    team1directmatchupwinratetop = winratee / gamess
if( gamess < 40):
    team1directmatchupwinratetop = 50  
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("sup")
for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
if (gamess > 0):
    team1directmatchupwinratebot = winratee / gamess
if( gamess < 40):
    team1directmatchupwinratebot = 50  
gamess = 0
winratee = 0
idk = champions_team2.iloc[:]
idk = idk.drop("top")
idk = idk.drop("mid")
idk = idk.drop("bot")
idk = idk.drop("sup")
for i in range(2):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team1directmatchupwinratejg = winratee / gamess
if( gamess < 40):
    team1directmatchupwinratejg = 50      
  
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("bot")
idk = idk.drop("sup")
       
for i in range(2):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
if (gamess > 0):
    team1directmatchupwinratemid = winratee / gamess
if( gamess < 40):
    team1directmatchupwinratemid = 50    
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("bot")
       
for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee 
if (gamess > 0):
    team1directmatchupwinratesup = winratee / gamess
if( gamess < 40):
    team1directmatchupwinratesup = 50    
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")

team1directmatchupgames = totalgames
team1directmatchupwinrate =  totalwinrate / totalgames


totalwinrate = 0
totalgames = 0




champions=winlose.iloc[0,:]
champions["top"] = top_enemy2
champions["jg"] = jg_enemy2
champions["mid"] = mid_enemy2
champions["bot"] = bot_enemy2
champions["sup"] = sup_enemy2

top = winrate_data_directmatchup.loc[top_enemy2]
jg = winrate_data_directmatchup.loc[jg_enemy2]
mid = winrate_data_directmatchup.loc[mid_enemy2]
bot = winrate_data_directmatchup.loc[bot_enemy2]
sup = winrate_data_directmatchup.loc[sup_enemy2]

gamess = 0
winratee = 0


for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"

idk = champions_team1.iloc[:]
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("bot")
idk = idk.drop("sup")


for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee
if (gamess > 0):
    team2directmatchupwinratetop = winratee / gamess
if( gamess < 40):
    team2directmatchupwinratetop = 50  
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("sup")
for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee
if (gamess > 0):
    team2directmatchupwinratebot = winratee / gamess
if( gamess < 40):
    team2directmatchupwinratebot = 50 
gamess = 0
winratee = 0
idk = champions_team1.iloc[:]
idk = idk.drop("top")
idk = idk.drop("mid")
idk = idk.drop("bot")
idk = idk.drop("sup")
for i in range(2):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team2directmatchupwinratejg = winratee / gamess
if( gamess < 40):
    team2directmatchupwinratejg = 50     
  
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("bot")
idk = idk.drop("sup")
       
for i in range(2):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee  
if (gamess > 0):
    team2directmatchupwinratemid = winratee / gamess
if( gamess < 40):
    team2directmatchupwinratemid = 50   
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]
idk = idk.drop("top")
idk = idk.drop("jg")
idk = idk.drop("mid")
idk = idk.drop("bot")
       
for i in range(2):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
totalgames = totalgames + gamess
totalwinrate = totalwinrate + winratee 
if (gamess > 0):
    team2directmatchupwinratesup = winratee / gamess
if( gamess < 40):
    team2directmatchupwinratesup = 50   
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")

team2directmatchupgames = totalgames
team2directmatchupwinrate =  totalwinrate / totalgames


totalwinrate = 0
totalgames = 0



#táto časť sa venuje výpočtom pre winratu nepriamych súbojov


champions=winlose.iloc[0,:]
champions["top"] = top2
champions["jg"] = jg2
champions["mid"] = mid2
champions["bot"] = bot2
champions["sup"] = sup2

top = winrate_data_indirectmatchup.loc[top2]
jg = winrate_data_indirectmatchup.loc[jg2]
mid = winrate_data_indirectmatchup.loc[mid2]
bot = winrate_data_indirectmatchup.loc[bot2]
sup = winrate_data_indirectmatchup.loc[sup2]

gamess = 0
winratee = 0


for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"

idk = champions_team2.iloc[:]

idk = idk.drop("top")


for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team1indirectmatchupwinratetop = winratee / gamess
if( gamess < 40):
    team1indirectmatchupwinratetop = 50 
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]

idk = idk.drop("bot")

for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team1indirectmatchupwinratebot = winratee / gamess
if( gamess < 40):
    team1indirectmatchupwinratebot = 50 
gamess = 0
winratee = 0
idk = champions_team2.iloc[:]
idk = idk.drop("jg")

for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team1indirectmatchupwinratejg = winratee / gamess
if( gamess < 40):
    team1indirectmatchupwinratejg = 50     
  
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]

idk = idk.drop("mid")

       
for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team1indirectmatchupwinratemid = winratee / gamess
if( gamess < 40):
    team1indirectmatchupwinratemid = 50   
gamess = 0
winratee = 0
        
idk = champions_team2.iloc[:]

idk = idk.drop("sup")

       
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee 
    team1indirectmatchupwinratesup = winratee / gamess
if( gamess < 40):
    team1indirectmatchupwinratesup = 50   
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")

team1indirectmatchupgames = totalgames
team1indirectmatchupwinrate =  totalwinrate / totalgames


totalwinrate = 0
totalgames = 0




champions=winlose.iloc[0,:]
champions["top"] = top_enemy2
champions["jg"] = jg_enemy2
champions["mid"] = mid_enemy2
champions["bot"] = bot_enemy2
champions["sup"] = sup_enemy2

top = winrate_data_indirectmatchup.loc[top_enemy2]
jg = winrate_data_indirectmatchup.loc[jg_enemy2]
mid = winrate_data_indirectmatchup.loc[mid_enemy2]
bot = winrate_data_indirectmatchup.loc[bot_enemy2]
sup = winrate_data_indirectmatchup.loc[sup_enemy2]

gamess = 0
winratee = 0


for i in range(6):
    if champions[i] == "aatrox": champions[i] = "teamfightdamage"
    if champions[i] == "ahri": champions[i] = "roamer"
    if champions[i] == "akali": champions[i] = "teamfightdamage"
    if champions[i] == "akshan": champions[i] = "laner"
    if champions[i] == "alistar": champions[i] = "engage"
    if champions[i] == "amumu": champions[i] = "teamfightcc"
    if champions[i] == "anivia": champions[i] = "teamfightcc"
    if champions[i] == "annie": champions[i] = "teamfightcc"
    if champions[i] == "aphelios": champions[i] = "fronttoback"
    if champions[i] == "ashe": champions[i] = "utility"
    if champions[i] == "aurelion Sol": champions[i] = "roamer"
    if champions[i] == "azir": champions[i] = "scaler"
    if champions[i] == "bard": champions[i] = "roamer"
    if champions[i] == "blitzcrank": champions[i] = "engage"
    if champions[i] == "brand": champions[i] = "teamfightdamage"
    if champions[i] == "braum": champions[i] = "peel"
    if champions[i] == "cailtyn": champions[i] = "fronttoback"
    if champions[i] == "camille": champions[i] = "splitpusher"
    if champions[i] == "cassiopeia": champions[i] = "teamfightdamage"
    if champions[i] == "chogath": champions[i] = "teamfightcc"
    if champions[i] == "corki": champions[i] = "scaler"
    if champions[i] == "darius": champions[i] = "laner"
    if champions[i] == "diana": champions[i] = "clearer"
    if champions[i] == "draven": champions[i] = "fighter"
    if champions[i] == "dr.mundo": champions[i] = "teamfightcc"
    if champions[i] == "ekko": champions[i] = "teamfightdamage"
    if champions[i] == "elise": champions[i] = "ganker"
    if champions[i] == "evelynn": champions[i] = "teamfightdamage"
    if champions[i] == "ezreal": champions[i] = "poker"
    if champions[i] == "fiddlesticks": champions[i] = "teamfightcc"
    if champions[i] == "fiora": champions[i] = "splitpusher"
    if champions[i] == "fizz": champions[i] = "roamer"
    if champions[i] == "gallio": champions[i] = "teamfightcc"
    if champions[i] == "gangplank": champions[i] = "teamfightdamage"
    if champions[i] == "garen": champions[i] = "splitpusher"
    if champions[i] == "gnar": champions[i] = "teamfightcc"
    if champions[i] == "gragas": champions[i] = "teamfightcc"
    if champions[i] == "graves": champions[i] = "clearer"
    if champions[i] == "gwen": champions[i] = "splitpusher"
    if champions[i] == "hecarim": champions[i] = "clearer"
    if champions[i] == "heimerdinger": champions[i] = "laner"
    if champions[i] == "illaoi": champions[i] = "splitpusher"
    if champions[i] == "irelia": champions[i] = "laner"
    if champions[i] == "ivern": champions[i] = "ganker"
    if champions[i] == "janna": champions[i] = "enchanter"
    if champions[i] == "jarvaniv": champions[i] = "ganker"
    if champions[i] == "jax": champions[i] = "splitpusher"
    if champions[i] == "jayce": champions[i] = "laner"
    if champions[i] == "jhin": champions[i] = "fronttoback"
    if champions[i] == "jinx": champions[i] = "fronttoback"
    if champions[i] == "kaisa": champions[i] = "fighter"
    if champions[i] == "kalista": champions[i] = "fighter"
    if champions[i] == "karma": champions[i] = "enchanter"
    if champions[i] == "karthus": champions[i] = "teamfightdamage"
    if champions[i] == "kassadin": champions[i] = "scaler"
    if champions[i] == "katarina": champions[i] = "roamer"
    if champions[i] == "kayle": champions[i] = "scaler"
    if champions[i] == "kayn": champions[i] = "late"
    if champions[i] == "kennen": champions[i] = "teamfightdamage"
    if champions[i] == "khazix": champions[i] = "assasin"
    if champions[i] == "kindred": champions[i] = "late"
    if champions[i] == "kled": champions[i] = "laner"
    if champions[i] == "kogmaw": champions[i] = "fronttoback"
    if champions[i] == "leblanc": champions[i] = "assasin"
    if champions[i] == "leesin": champions[i] = "ganker"
    if champions[i] == "leona": champions[i] = "engage"
    if champions[i] == "lillia": champions[i] = "teamfightcc"
    if champions[i] == "lissandra": champions[i] = "teamfightcc"
    if champions[i] == "lucian": champions[i] = "fighter"
    if champions[i] == "lulu": champions[i] = "enchanter"
    if champions[i] == "lux": champions[i] = "teamfightdamage"
    if champions[i] == "malphite": champions[i] = "teamfightcc"
    if champions[i] == "malzahar": champions[i] = "teamfightcc"
    if champions[i] == "maokai": champions[i] = "teamfightcc"
    if champions[i] == "masteryi": champions[i] = "teamfightdamage"
    if champions[i] == "miss Fortune": champions[i] = "fronttoback"
    if champions[i] == "mordekaiser": champions[i] = "teamfightcc"
    if champions[i] == "morgana": champions[i] = "peel"
    if champions[i] == "nami": champions[i] = "enchanter"
    if champions[i] == "nasus": champions[i] = "splitpusher"
    if champions[i] == "nautilus": champions[i] = "engage"
    if champions[i] == "neeko": champions[i] = "teamfightcc"
    if champions[i] == "nidalee": champions[i] = "ganker"
    if champions[i] == "nocturne": champions[i] = "ganker"
    if champions[i] == "nunu&willump": champions[i] = "ganker"
    if champions[i] == "olaf": champions[i] = "teamfightdamage"
    if champions[i] == "orianna": champions[i] = "teamfightcc"
    if champions[i] == "ornn": champions[i] = "teamfightcc"
    if champions[i] == "pantheon": champions[i] = "engage"
    if champions[i] == "poppy": champions[i] = "teamfightcc"
    if champions[i] == "pyke": champions[i] = "assasin"
    if champions[i] == "qiyana": champions[i] = "assasin"
    if champions[i] == "quinn": champions[i] = "splitpusher"
    if champions[i] == "rakan": champions[i] = "peel"
    if champions[i] == "rammus": champions[i] = "teamfightcc"
    if champions[i] == "reksai": champions[i] = "ganker"
    if champions[i] == "rell": champions[i] = "peel"
    if champions[i] == "renataglasc": champions[i] = "peel"
    if champions[i] == "renekton": champions[i] = "laner"
    if champions[i] == "rengar": champions[i] = "assasin"
    if champions[i] == "riven": champions[i] = "splitpusher"
    if champions[i] == "rumble": champions[i] = "teamfightdamage"
    if champions[i] == "ryze": champions[i] = "scaler"
    if champions[i] == "samira": champions[i] = "fighter"
    if champions[i] == "sejuani": champions[i] = "teamfightcc"
    if champions[i] == "senna": champions[i] = "utility"
    if champions[i] == "seraphine": champions[i] = "enchanter"
    if champions[i] == "sett": champions[i] = "laner"
    if champions[i] == "shaco": champions[i] = "assasin"
    if champions[i] == "shen": champions[i] = "peel"
    if champions[i] == "shyvana": champions[i] = "teamfightdamage"
    if champions[i] == "singed": champions[i] = "splitpusher"
    if champions[i] == "sion": champions[i] = "splitpusher"
    if champions[i] == "sivir": champions[i] = "fronttoback"
    if champions[i] == "skarner": champions[i] = "teamfightcc"
    if champions[i] == "sona": champions[i] = "enchanter"
    if champions[i] == "soraka": champions[i] = "enchanter"
    if champions[i] == "swain": champions[i] = "teamfightdamage"
    if champions[i] == "sylas": champions[i] = "scaler"
    if champions[i] == "syndra": champions[i] = "teamfightdamage"
    if champions[i] == "tahmkench": champions[i] = "peel"
    if champions[i] == "tallyah": champions[i] = "teamfightdamage"
    if champions[i] == "talon": champions[i] = "assasin"
    if champions[i] == "taric": champions[i] = "peel"
    if champions[i] == "teemo": champions[i] = "splitpusher"
    if champions[i] == "thresh": champions[i] = "peel"
    if champions[i] == "tristana": champions[i] = "fighter"
    if champions[i] == "trundle": champions[i] = "ganker"
    if champions[i] == "tryndamere": champions[i] = "splitpusher"
    if champions[i] == "twistedfate": champions[i] = "roamer"
    if champions[i] == "twitch": champions[i] = "assasin"
    if champions[i] == "udyr": champions[i] = "clearer"
    if champions[i] == "urgot": champions[i] = "splitpusher"
    if champions[i] == "varus": champions[i] = "poker"
    if champions[i] == "vayne": champions[i] = "fighter"
    if champions[i] == "veigar": champions[i] = "teamfightcc"
    if champions[i] == "velkoz": champions[i] = "teamfightdamage"
    if champions[i] == "vex": champions[i] = "roamer"
    if champions[i] == "vi": champions[i] = "teamfightcc"
    if champions[i] == "viego": champions[i] = "teamfightdamage"
    if champions[i] == "viktor": champions[i] = "scaler"
    if champions[i] == "vladimir": champions[i] = "scaler"
    if champions[i] == "volibear": champions[i] = "ganker"
    if champions[i] == "warwick": champions[i] = "ganker"
    if champions[i] == "wukong": champions[i] = "teamfightcc"
    if champions[i] == "xayah": champions[i] = "fronttoback"
    if champions[i] == "xerath": champions[i] = "teamfightdamage"
    if champions[i] == "xinzhao": champions[i] = "ganker"
    if champions[i] == "yasuo": champions[i] = "teamfightdamage"
    if champions[i] == "yone": champions[i] = "teamfighdamage"
    if champions[i] == "yorick": champions[i] = "splitpusher"
    if champions[i] == "yuumi": champions[i] = "enchanter"
    if champions[i] == "zac": champions[i] = "teamfightcc"
    if champions[i] == "zed": champions[i] = "assasin"
    if champions[i] == "zeri": champions[i] = "fronttoback"
    if champions[i] == "ziggs": champions[i] = "teamfightdamage"
    if champions[i] == "zilean": champions[i] = "peel"
    if champions[i] == "zoe": champions[i] = "roamer"
    if champions[i] == "zyra": champions[i] = "teamfightdamage"

idk = champions_team1.iloc[:]

idk = idk.drop("top")


for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + top.teamfightdamagegames
        winratee = winratee + (top.teamfightdamagewinrate * top.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + top.fightergames
        winratee = winratee + (top.fighterwinrate * top.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  top.engagegames
        winratee = winratee + (top.engagewinrate * top.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + top.lanergames
        winratee = winratee + (top.lanerwinrate * top.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + top.splitpushergames
        winratee = winratee + (top.splitpusherwinrate * top.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + top.teamfightccgames
        winratee = winratee + (top.teamfightccwinrate * top.teamfightccgames)
    if(idk[i] == "clearer"):
        gamess = gamess +  top.clearergames
        winratee = winratee + (top.clearerwinrate * top.clearergames)
    if(idk[i] == "ganker"):
        gamess = gamess + top.gankergames
        winratee = winratee + (top.gankerwinrate * top.gankergames)
        
    if(idk[i] == "assasin"):
        gamess = gamess + top.assasingames
        winratee = winratee + (top.assasinwinrate * top.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + top.lategames
        winratee = winratee + (top.latewinrate * top.lategames)
    if(idk[i] == "scaler"):
        gamess = gamess +  top.scalergames
        winratee = winratee + (top.scalerwinrate * top.scalergames)
    if(idk[i] == "roamer"):
        gamess = gamess + top.roamergames
        winratee = winratee + (top.roamerwinrate * top.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + top.pokergames
        winratee = winratee + (top.pokerwinrate * top.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  top.utilitygames
        winratee = winratee + (top.utilitywinrate * top.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + top.fronttobackgames
        winratee = winratee + (top.fronttobackwinrate * top.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + top.peelgames
        winratee = winratee + (top.peelwinrate * top.peelgames)
    if(idk[i] == "enchanter"):
        gamess = gamess + top.enchantergames
        winratee = winratee + (top.enchanterwinrate * top.enchantergames)
      
print("TOP")        
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team2indirectmatchupwinratetop = winratee / gamess
if( gamess < 40):
    team2indirectmatchupwinratetop = 50 
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]

idk = idk.drop("bot")

for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + bot.teamfightdamagegames
        winratee = winratee + (bot.teamfightdamagewinrate * bot.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if(idk[i] == "fighter"):
        gamess = gamess + bot.fightergames
        winratee = winratee + (bot.fighterwinrate * bot.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  bot.engagegames
        winratee = winratee + (bot.engagewinrate * bot.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + bot.lanergames
        winratee = winratee + (bot.lanerwinrate * bot.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + bot.splitpushergames
        winratee = winratee + (bot.splitpusherwinrate * bot.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + bot.teamfightccgames
        winratee = winratee + (bot.teamfightccwinrate * bot.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  bot.clearergames
        winratee = winratee + (bot.clearerwinrate * bot.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + bot.gankergames
        winratee = winratee + (bot.gankerwinrate * bot.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + bot.assasingames
        winratee = winratee + (bot.assasinwinrate * bot.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + bot.lategames
        winratee = winratee + (bot.latewinrate * bot.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  bot.scalergames
        winratee = winratee + (bot.scalerwinrate * bot.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + bot.roamergames
        winratee = winratee + (bot.roamerwinrate * bot.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + bot.pokergames
        winratee = winratee + (bot.pokerwinrate * bot.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  bot.utilitygames
        winratee = winratee + (bot.utilitywinrate * bot.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + bot.fronttobackgames
        winratee = winratee + (bot.fronttobackwinrate * bot.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + bot.peelgames
        winratee = winratee + (bot.peelwinrate * bot.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + bot.enchantergames
        winratee = winratee + (bot.enchanterwinrate * bot.enchantergames)
      
print("BOT")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee
    team2indirectmatchupwinratebot = winratee / gamess
if( gamess < 40):
    team2indirectmatchupwinratebot = 50 
gamess = 0
winratee = 0
idk = champions_team1.iloc[:]
idk = idk.drop("jg")

for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + jg.teamfightdamagegames
        winratee = winratee + (jg.teamfightdamagewinrate * jg.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + jg.fightergames
        winratee = winratee + (jg.fighterwinrate * jg.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  jg.engagegames
        winratee = winratee + (jg.engagewinrate * jg.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + jg.lanergames
        winratee = winratee + (jg.lanerwinrate * jg.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + jg.splitpushergames
        winratee = winratee + (jg.splitpusherwinrate * jg.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + jg.teamfightccgames
        winratee = winratee + (jg.teamfightccwinrate * jg.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  jg.clearergames
        winratee = winratee + (jg.clearerwinrate * jg.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + jg.gankergames
        winratee = winratee + (jg.gankerwinrate * jg.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + jg.assasingames
        winratee = winratee + (jg.assasinwinrate * jg.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + jg.lategames
        winratee = winratee + (jg.latewinrate * jg.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  jg.scalergames
        winratee = winratee + (jg.scalerwinrate * jg.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + jg.roamergames
        winratee = winratee + (jg.roamerwinrate * jg.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + jg.pokergames
        winratee = winratee + (jg.pokerwinrate * jg.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  jg.utilitygames
        winratee = winratee + (jg.utilitywinrate * jg.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + jg.fronttobackgames
        winratee = winratee + (jg.fronttobackwinrate * jg.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + jg.peelgames
        winratee = winratee + (jg.peelwinrate * jg.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + jg.enchantergames
        winratee = winratee + (jg.enchanterwinrate * jg.enchantergames)
      
print("JG")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team2indirectmatchupwinratejg = winratee / gamess
if( gamess < 40):
    team2indirectmatchupwinratejg = 50    
  
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]

idk = idk.drop("mid")

for i in range(4):
    if(idk[i] == "teamfightdamage"):
        gamess = gamess + mid.teamfightdamagegames
        winratee = winratee + (mid.teamfightdamagewinrate * mid.teamfightdamagegames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + mid.fightergames
        winratee = winratee + (mid.fighterwinrate * mid.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  mid.engagegames
        winratee = winratee + (mid.engagewinrate * mid.engagegames)
    if(  idk[i] == "laner"):
        gamess = gamess + mid.lanergames
        winratee = winratee + (mid.lanerwinrate * mid.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + mid.splitpushergames
        winratee = winratee + (mid.splitpusherwinrate * mid.splitpushergames)
    if( idk[i] == "teamfightcc"):
        gamess = gamess + mid.teamfightccgames
        winratee = winratee + (mid.teamfightccwinrate * mid.teamfightccgames)
    if( idk[i] == "clearer"):
        gamess = gamess +  mid.clearergames
        winratee = winratee + (mid.clearerwinrate * mid.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + mid.gankergames
        winratee = winratee + (mid.gankerwinrate * mid.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + mid.assasingames
        winratee = winratee + (mid.assasinwinrate * mid.assasingames)
    if(idk[i] == "late"):
        gamess = gamess + mid.lategames
        winratee = winratee + (mid.latewinrate * mid.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  mid.scalergames
        winratee = winratee + (mid.scalerwinrate * mid.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + mid.roamergames
        winratee = winratee + (mid.roamerwinrate * mid.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + mid.pokergames
        winratee = winratee + (mid.pokerwinrate * mid.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  mid.utilitygames
        winratee = winratee + (mid.utilitywinrate * mid.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + mid.fronttobackgames
        winratee = winratee + (mid.fronttobackwinrate * mid.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + mid.peelgames
        winratee = winratee + (mid.peelwinrate * mid.peelgames)
    if( idk[i] == "enchanter"):
        gamess = gamess + mid.enchantergames
        winratee = winratee + (mid.enchanterwinrate * mid.enchantergames)
      
print("MID")         
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee  
    team2indirectmatchupwinratemid = winratee / gamess
if( gamess < 40):
    team2indirectmatchupwinratemid = 50   
gamess = 0
winratee = 0
        
idk = champions_team1.iloc[:]

idk = idk.drop("sup")

       
for i in range(4):
    if( idk[i] == "teamfightdamage"):
        gamess = gamess + sup.teamfightdamagegames
        winratee = winratee + (sup.teamfightdamagewinrate * sup.teamfightdamagegames)
    if(idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "fighter"):
        gamess = gamess + sup.fightergames
        winratee = winratee + (sup.fighterwinrate * sup.fightergames)
    if( idk[i] == "engage"):
        gamess = gamess +  sup.engagegames
        winratee = winratee + (sup.engagewinrate * sup.engagegames)
    if( idk[i] == "laner"):
        gamess = gamess + sup.lanergames
        winratee = winratee + (sup.lanerwinrate * sup.lanergames)
        
    if( idk[i] == "splitpusher"):
        gamess = gamess + sup.splitpushergames
        winratee = winratee + (sup.splitpusherwinrate * sup.splitpushergames)
    if(  idk[i] == "teamfightcc"):
        gamess = gamess + sup.teamfightccgames
        winratee = winratee + (sup.teamfightccwinrate * sup.teamfightccgames)
    if(  idk[i] == "clearer"):
        gamess = gamess +  sup.clearergames
        winratee = winratee + (sup.clearerwinrate * sup.clearergames)
    if( idk[i] == "ganker"):
        gamess = gamess + sup.gankergames
        winratee = winratee + (sup.gankerwinrate * sup.gankergames)
        
    if( idk[i] == "assasin"):
        gamess = gamess + sup.assasingames
        winratee = winratee + (sup.assasinwinrate * sup.assasingames)
    if( idk[i] == "late"):
        gamess = gamess + sup.lategames
        winratee = winratee + (sup.latewinrate * sup.lategames)
    if( idk[i] == "scaler"):
        gamess = gamess +  sup.scalergames
        winratee = winratee + (sup.scalerwinrate * sup.scalergames)
    if( idk[i] == "roamer"):
        gamess = gamess + sup.roamergames
        winratee = winratee + (sup.roamerwinrate * sup.roamergames)
    if( idk[i] == "poker"):
        gamess = gamess + sup.pokergames
        winratee = winratee + (sup.pokerwinrate * sup.pokergames)
    if( idk[i] == "utility"):
        gamess = gamess +  sup.utilitygames
        winratee = winratee + (sup.utilitywinrate * sup.utilitygames)
    if( idk[i] == "fronttoback"):
        gamess = gamess + sup.fronttobackgames
        winratee = winratee + (sup.fronttobackwinrate * sup.fronttobackgames)        
    if( idk[i] == "peel"):
        gamess = gamess + sup.peelgames
        winratee = winratee + (sup.peelwinrate * sup.peelgames)
    if(  idk[i] == "enchanter"):
        gamess = gamess + sup.enchantergames
        winratee = winratee + (sup.enchanterwinrate * sup.enchantergames)
      
print("SUP")          
print("Games played :",gamess)
if (gamess > 0):
    print("Average score :",winratee / gamess,"\n")  
    totalgames = totalgames + gamess
    totalwinrate = totalwinrate + winratee 
    team2indirectmatchupwinratesup = winratee / gamess
if( gamess < 40):
    team2indirectmatchupwinratesup = 50   
    
print("Total games played :",totalgames)
print("Total score :",totalwinrate / totalgames)
if((totalwinrate / totalgames) < 48):
    print("Známka : F")
elif ((totalwinrate / totalgames) < 49.5):
    print("Známka : E")
elif ((totalwinrate / totalgames) < 50.5):
    print("Známka : D")
elif ((totalwinrate / totalgames) < 51.5):
    print("Známka : C")
elif ((totalwinrate / totalgames) < 52.5):
    print("Známka : B")    
elif ((totalwinrate / totalgames) < 53.5):
    print("Známka : A")
elif ((totalwinrate / totalgames) < 54.5):
    print("Známka : S")
elif ((totalwinrate / totalgames) > 54.5):
    print("Známka : S+")
print("\n")
team2indirectmatchupgames = totalgames
team2indirectmatchupwinrate =  totalwinrate / totalgames


totalwinrate = 0
totalgames = 0

team1winratee = (team1compatibilitygames * team1compatibilitywinrate) + (team1directmatchupgames * team1directmatchupwinrate) + (team1indirectmatchupgames * team1indirectmatchupwinrate)
team1winrate = team1winratee / (team1compatibilitygames + team1directmatchupgames + team1indirectmatchupgames)

team2winratee = (team2compatibilitygames * team2compatibilitywinrate) + (team2directmatchupgames * team2directmatchupwinrate) + (team2indirectmatchupgames * team2indirectmatchupwinrate)
team2winrate = team2winratee / (team2compatibilitygames + team2directmatchupgames + team2indirectmatchupgames)


print("\nCelkový winrate prvého tímu je :",team1winrate,"\n")
print("Celkový winrate druhého tímu je :",team2winrate,"\n")

#zápis dát do textových súborov

#predictdata.loc[indexx] = [team1compatibilitywinrate,team1directmatchupwinrate,team1indirectmatchupwinrate,team1winrate,team2compatibilitywinrate,team2directmatchupwinrate,team2indirectmatchupwinrate,team2winrate,winner]
#predictdata.to_csv('data\predictdata.txt')
#predictdatanew.loc[index] = [team1compatibilitywinratetop,team1compatibilitywinratejg,team1compatibilitywinratemid,team1compatibilitywinratebot,team1compatibilitywinratesup,team1directmatchupwinratetop,team1directmatchupwinratejg,team1directmatchupwinratemid,team1directmatchupwinratebot,team1directmatchupwinratesup,team1indirectmatchupwinratetop,team1indirectmatchupwinratejg,team1indirectmatchupwinratemid,team1indirectmatchupwinratebot,team1indirectmatchupwinratesup,team1winrate,team2compatibilitywinratetop,team2compatibilitywinratejg,team2compatibilitywinratemid,team2compatibilitywinratebot,team2compatibilitywinratesup,team2directmatchupwinratetop,team2directmatchupwinratejg,team2directmatchupwinratemid,team2directmatchupwinratebot,team2directmatchupwinratesup,team2indirectmatchupwinratetop,team2indirectmatchupwinratejg,team2indirectmatchupwinratemid,team2indirectmatchupwinratebot,team2indirectmatchupwinratesup,team2winrate,winner]
#predictdatanew.to_csv('data\predictdatanew.txt')
#predictdatafinal.loc[indexxx] = [team1ranking,team1compatibilitywinratetop,team1compatibilitywinratejg,team1compatibilitywinratemid,team1compatibilitywinratebot,team1compatibilitywinratesup,team1directmatchupwinratetop,team1directmatchupwinratejg,team1directmatchupwinratemid,team1directmatchupwinratebot,team1directmatchupwinratesup,team1indirectmatchupwinratetop,team1indirectmatchupwinratejg,team1indirectmatchupwinratemid,team1indirectmatchupwinratebot,team1indirectmatchupwinratesup,team1winrate,team2ranking,team2compatibilitywinratetop,team2compatibilitywinratejg,team2compatibilitywinratemid,team2compatibilitywinratebot,team2compatibilitywinratesup,team2directmatchupwinratetop,team2directmatchupwinratejg,team2directmatchupwinratemid,team2directmatchupwinratebot,team2directmatchupwinratesup,team2indirectmatchupwinratetop,team2indirectmatchupwinratejg,team2indirectmatchupwinratemid,team2indirectmatchupwinratebot,team2indirectmatchupwinratesup,team2winrate,winner]
#predictdatafinal.to_csv('data\predictdatafinal.txt')
#predictdataoldfinal.loc[indexxxx] = [team1ranking,team1compatibilitywinrate,team1directmatchupwinrate,team1indirectmatchupwinrate,team1winrate,team2ranking,team2compatibilitywinrate,team2directmatchupwinrate,team2indirectmatchupwinrate,team2winrate,winner]
#predictdataoldfinal.to_csv('data\predictdataoldfinal.txt')

#print(team1compatibilitywinratetop,",",team1compatibilitywinratejg,",",team1compatibilitywinratemid,",",team1compatibilitywinratebot,",",team1compatibilitywinratesup,",",team1directmatchupwinratetop,",",team1directmatchupwinratejg,",",team1directmatchupwinratemid,",",team1directmatchupwinratebot,",",team1directmatchupwinratesup,",",team1indirectmatchupwinratetop,",",team1indirectmatchupwinratejg,",",team1indirectmatchupwinratemid,",",team1indirectmatchupwinratebot,",",team1indirectmatchupwinratesup,",",team1winrate,",",team2compatibilitywinratetop,",",team2compatibilitywinratejg,",",team2compatibilitywinratemid,",",team2compatibilitywinratebot,",",team2compatibilitywinratesup,",",team2directmatchupwinratetop,",",team2directmatchupwinratejg,",",team2directmatchupwinratemid,",",team2directmatchupwinratebot,",",team2directmatchupwinratesup,",",team2indirectmatchupwinratetop,",",team2indirectmatchupwinratejg,",",team2indirectmatchupwinratemid,",",team2indirectmatchupwinratebot,",",team2indirectmatchupwinratesup,",",team2winrate,",",team2rankingS,",",team2rankingS,",",team2rankingA,",",team2rankingB,",",team2rankingC,",",team2rankingD,",",team1rankingSS,",",team1rankingS,",",team1rankingA,",",team1rankingB,",",team1rankingC,",",team1rankingD,",",winner)
winratetopnow = 0
winratejgnow = 0
winratemidnow = 0
winratebotnow = 0
winratesupnow = 0
winratetopenemynow = 0
winratejgenemynow = 0
winratemidenemynow = 0
winratebotenemynow = 0
winratesupenemynow = 0

row = championwinrate.loc[championwinrate['Champion'] == top2]

if not row.empty:
    winratetopnow = row['Winrate'].values[0]
    
row = championwinrate.loc[championwinrate['Champion'] == jg2]

if not row.empty:
    winratejgnow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == mid2]

if not row.empty:
    winratemidnow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == bot2]

if not row.empty:
    winratebotnow = row['Winrate'].values[0]
    
row = championwinrate.loc[championwinrate['Champion'] == sup2]

if not row.empty:
    winratesupnow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == top_enemy2]

if not row.empty:
    winratetopenemynow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == jg_enemy2]

if not row.empty:
    winratejgenemynow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == mid_enemy2]

if not row.empty:
    winratemidenemynow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == bot_enemy2]

if not row.empty:
    winratebotenemynow = row['Winrate'].values[0]

row = championwinrate.loc[championwinrate['Champion'] == sup_enemy2]

if not row.empty:
    winratesupenemynow = row['Winrate'].values[0]





row = win131.loc[win131['Champion'] == top2]

if not row.empty:
    winratetopnow += row['Winrate'].values[0] 
    winratetopnow = winratetopnow / 2
    
row = win131.loc[win131['Champion'] == jg2]

if not row.empty:
    winratejgnow += row['Winrate'].values[0] 
    winratejgnow = winratejgnow / 2

row = win131.loc[win131['Champion'] == mid2]

if not row.empty:
    winratemidnow += row['Winrate'].values[0] 
    winratemidnow = winratemidnow / 2

row = win131.loc[win131['Champion'] == bot2]

if not row.empty:
    winratebotnow += row['Winrate'].values[0] 
    winratebotnow = winratebotnow / 2
    
row = win131.loc[win131['Champion'] == sup2]

if not row.empty:
    winratesupnow += row['Winrate'].values[0] 
    winratesupnow = winratesupnow / 2

row = win131.loc[win131['Champion'] == top_enemy2]

if not row.empty:
    winratetopenemynow += row['Winrate'].values[0] 
    winratetopenemynow = winratetopenemynow / 2

row = win131.loc[win131['Champion'] == jg_enemy2]

if not row.empty:
    winratejgenemynow = +row['Winrate'].values[0] 
    winratejgenemynow = winratejgenemynow / 2

row = win131.loc[win131['Champion'] == mid_enemy2]

if not row.empty:
    winratemidenemynow += row['Winrate'].values[0] 
    winratemidenemynow = winratemidenemynow / 2

row = win131.loc[win131['Champion'] == bot_enemy2]

if not row.empty:
    winratebotenemynow += row['Winrate'].values[0] 
    winratebotenemynow = winratebotenemynow / 2

row = win131.loc[win131['Champion'] == sup_enemy2]

if not row.empty:
    winratesupenemynow += row['Winrate'].values[0] 
    winratesupenemynow = winratesupenemynow / 2









def calculate_total_winrate(row):
    winrates = [row["gankerwinrate"], row["engagewinrate"], row["lanerwinrate"], row["splitpusherwinrate"], 
                row["teamfightdamagewinrate"], row["teamfightccwinrate"], row["clearerwinrate"], 
                row["assasinwinrate"], row["roamerwinrate"], row["pokerwinrate"], row["fighterwinrate"], 
                row["utilitywinrate"], row["fronttobackwinrate"], row["peelwinrate"], row["enchanterwinrate"], 
                row["scalerwinrate"], row["latewinrate"]]
    games = [row["gankergames"], row["engagegames"], row["lanergames"], row["splitpushergames"], 
             row["teamfightdamagegames"], row["teamfightccgames"], row["clearergames"], row["assasingames"], 
             row["roamergames"], row["pokergames"], row["fightergames"], row["utilitygames"], 
             row["fronttobackgames"], row["peelgames"], row["enchantergames"], row["scalergames"], row["lategames"]]
    winrates = pd.Series(winrates).fillna(0)
    games = pd.Series(games).fillna(0)
    if sum(games) == 0:
        return 0
    total_winrate = sum(winrates[i] * games[i] for i in range(len(winrates))) / sum(games)
    return total_winrate


winrate_data_with["total_winrate"] = winrate_data_with.apply(calculate_total_winrate, axis=1)
winrate_data_directmatchup["total_winrate"] = winrate_data_directmatchup.apply(calculate_total_winrate, axis=1)
winrate_data_indirectmatchup["total_winrate"] = winrate_data_indirectmatchup.apply(calculate_total_winrate, axis=1)


def calculate_total_games(row):
    games = [row["gankergames"], row["engagegames"], row["lanergames"], row["splitpushergames"], row["teamfightdamagegames"], row["teamfightccgames"], row["clearergames"], row["assasingames"], row["roamergames"], row["pokergames"], row["fightergames"], row["utilitygames"], row["fronttobackgames"], row["peelgames"], row["enchantergames"], row["scalergames"], row["lategames"]]
    total_games = sum(games)
    return total_games

winrate_data_with["total_games"] = winrate_data_with.apply(calculate_total_games, axis=1)
winrate_data_directmatchup["total_games"] = winrate_data_directmatchup.apply(calculate_total_games, axis=1)
winrate_data_indirectmatchup["total_games"] = winrate_data_indirectmatchup.apply(calculate_total_games, axis=1)
games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[top2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[top2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[top2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

toptotalwinrate = games / gamess


games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[jg2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[jg2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[jg2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

jgtotalwinrate = games / gamess

games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[mid2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[mid2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[mid2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

midtotalwinrate = games / gamess



games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[bot2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[bot2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[bot2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

bottotalwinrate = games / gamess



games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[sup2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[sup2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[sup2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

suptotalwinrate = games / gamess



games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[top_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[top_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[top_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

topenemytotalwinrate = games / gamess


games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[jg_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[jg_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[jg_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

jgenemytotalwinrate = games / gamess

games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[mid_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[mid_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[mid_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

midenemytotalwinrate = games / gamess



games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[bot_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[bot_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[bot_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

botenemytotalwinrate = games / gamess



games = 0
winrate = 0
gamess = 0
top = winrate_data_with.loc[sup_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_directmatchup.loc[sup_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]
top = winrate_data_indirectmatchup.loc[sup_enemy2]
games += top["total_games"] * top["total_winrate"]
gamess += top["total_games"]

supenemytotalwinrate = games / gamess





if winratetopnow > 0:
    team1compatibilitywinratetop = team1compatibilitywinratetop / toptotalwinrate if toptotalwinrate > 0 else 0.5
    team1compatibilitywinratetop = team1compatibilitywinratetop * winratetopnow
    
    team1directmatchupwinratetop = team1directmatchupwinratetop / toptotalwinrate if toptotalwinrate > 0 else 0.5
    team1directmatchupwinratetop = team1directmatchupwinratetop * winratetopnow
    
    team1indirectmatchupwinratetop = team1indirectmatchupwinratetop / toptotalwinrate if toptotalwinrate > 0 else 0.5
    team1indirectmatchupwinratetop = team1indirectmatchupwinratetop * winratetopnow

if winratejgnow > 0:
    team1compatibilitywinratejg = team1compatibilitywinratejg / jgtotalwinrate if jgtotalwinrate > 0 else 0.5
    team1compatibilitywinratejg = team1compatibilitywinratejg * winratejgnow
    
    team1directmatchupwinratejg = team1directmatchupwinratejg / jgtotalwinrate if jgtotalwinrate > 0 else 0.5
    team1directmatchupwinratejg = team1directmatchupwinratejg * winratejgnow
    
    team1indirectmatchupwinratejg = team1indirectmatchupwinratejg / jgtotalwinrate if jgtotalwinrate > 0 else 0.5
    team1indirectmatchupwinratejg = team1indirectmatchupwinratejg * winratejgnow

if winratemidnow > 0:
    team1compatibilitywinratemid = team1compatibilitywinratemid / midtotalwinrate if midtotalwinrate > 0 else 0.5
    team1compatibilitywinratemid = team1compatibilitywinratemid * winratemidnow
    
    team1directmatchupwinratemid = team1directmatchupwinratemid / midtotalwinrate if midtotalwinrate > 0 else 0.5
    team1directmatchupwinratemid = team1directmatchupwinratemid * winratemidnow
    
    team1indirectmatchupwinratemid = team1indirectmatchupwinratemid / midtotalwinrate if midtotalwinrate > 0 else 0.5
    team1indirectmatchupwinratemid = team1indirectmatchupwinratemid * winratemidnow
    
if winratebotnow > 0:
    team1compatibilitywinratebot = team1compatibilitywinratebot / bottotalwinrate if bottotalwinrate > 0 else 0.5
    team1compatibilitywinratebot = team1compatibilitywinratebot * winratebotnow
    
    team1directmatchupwinratebot = team1directmatchupwinratebot / bottotalwinrate if bottotalwinrate > 0 else 0.5
    team1directmatchupwinratebot = team1directmatchupwinratebot * winratebotnow
    
    team1indirectmatchupwinratebot = team1indirectmatchupwinratebot / bottotalwinrate
    team1indirectmatchupwinratebot = team1indirectmatchupwinratebot * winratebotnow

if (winratesupnow > 0):
    team1compatibilitywinratesup = team1compatibilitywinratesup / suptotalwinrate if suptotalwinrate > 0 else 0.5
    team1compatibilitywinratesup = team1compatibilitywinratesup * winratesupnow
    
    team1directmatchupwinratesup = team1directmatchupwinratesup / suptotalwinrate if suptotalwinrate > 0 else 0.5
    team1directmatchupwinratesup = team1directmatchupwinratesup * winratesupnow
    
    team1indirectmatchupwinratesup = team1indirectmatchupwinratesup / suptotalwinrate if suptotalwinrate > 0 else 0.5
    team1indirectmatchupwinratesup = team1indirectmatchupwinratesup * winratesupnow
    
    
    
if (winratetopenemynow > 0):
    team2compatibilitywinratetop = team2compatibilitywinratetop / topenemytotalwinrate if topenemytotalwinrate > 0 else 0.5
    team2compatibilitywinratetop = team2compatibilitywinratetop * winratesupenemynow  
    
    team2directmatchupwinratetop = team2directmatchupwinratetop / topenemytotalwinrate if topenemytotalwinrate > 0 else 0.5
    team2directmatchupwinratetop = team2directmatchupwinratetop * winratesupenemynow     
    
    team2indirectmatchupwinratetop = team2indirectmatchupwinratetop / topenemytotalwinrate if topenemytotalwinrate > 0 else 0.5
    team2indirectmatchupwinratetop = team2indirectmatchupwinratetop * winratesupenemynow  

if (winratejgenemynow > 0):
    team2compatibilitywinratejg = team2compatibilitywinratejg / jgenemytotalwinrate if jgenemytotalwinrate > 0 else 0.5
    team2compatibilitywinratejg = team2compatibilitywinratejg * winratejgenemynow 
    
    team2directmatchupwinratejg = team2directmatchupwinratejg / jgenemytotalwinrate if jgenemytotalwinrate > 0 else 0.5
    team2directmatchupwinratejg = team2directmatchupwinratejg * winratejgenemynow 
    
    team2indirectmatchupwinratejg = team2indirectmatchupwinratejg / jgenemytotalwinrate if jgenemytotalwinrate > 0 else 0.5
    team2indirectmatchupwinratejg = team2indirectmatchupwinratejg * winratejgenemynow 

if (winratemidenemynow > 0):
    team2compatibilitywinratemid = team2compatibilitywinratemid / midenemytotalwinrate
    team2compatibilitywinratemid = team2compatibilitywinratemid * winratemidenemynow 
    
    team2directmatchupwinratemid = team2directmatchupwinratemid / midenemytotalwinrate
    team2directmatchupwinratemid = team2directmatchupwinratemid * winratemidenemynow 
    
    team2indirectmatchupwinratemid = team2indirectmatchupwinratemid / midenemytotalwinrate
    team2indirectmatchupwinratemid = team2indirectmatchupwinratemid * winratemidenemynow 
    
if (winratebotenemynow > 0):
    team2compatibilitywinratebot = team2compatibilitywinratebot / botenemytotalwinrate
    team2compatibilitywinratebot = team2compatibilitywinratebot * winratebotenemynow 
    
    team2directmatchupwinratebot = team2directmatchupwinratebot / botenemytotalwinrate
    team2directmatchupwinratebot = team2directmatchupwinratebot * winratebotenemynow 
    
    team2indirectmatchupwinratebot = team2indirectmatchupwinratebot / botenemytotalwinrate
    team2indirectmatchupwinratebot = team2indirectmatchupwinratebot * winratebotenemynow 

if (winratesupenemynow > 0):
    team2compatibilitywinratesup = team2compatibilitywinratesup / supenemytotalwinrate
    team2compatibilitywinratesup = team2compatibilitywinratesup * winratesupenemynow 
    
    team2directmatchupwinratesup = team2directmatchupwinratesup / supenemytotalwinrate
    team2directmatchupwinratesup = team2directmatchupwinratesup * winratesupenemynow 
    
    team2indirectmatchupwinratesup = team2indirectmatchupwinratesup / supenemytotalwinrate
    team2indirectmatchupwinratesup = team2indirectmatchupwinratesup * winratesupenemynow 
    
team2winrates = (team2compatibilitywinratetop + team2directmatchupwinratetop + team2indirectmatchupwinratetop + team2compatibilitywinratejg + team2directmatchupwinratejg + team2indirectmatchupwinratejg + team2compatibilitywinratemid + team2directmatchupwinratemid + team2indirectmatchupwinratemid + team2compatibilitywinratebot + team2directmatchupwinratebot + team2indirectmatchupwinratebot + team2compatibilitywinratesup + team2directmatchupwinratesup + team2indirectmatchupwinratesup) / 15
team1winrates = (team1compatibilitywinratetop + team1directmatchupwinratetop + team1indirectmatchupwinratetop + team1compatibilitywinratejg + team1directmatchupwinratejg + team1indirectmatchupwinratejg + team1compatibilitywinratemid + team1directmatchupwinratemid + team1indirectmatchupwinratemid + team1compatibilitywinratebot + team1directmatchupwinratebot + team1indirectmatchupwinratebot + team1compatibilitywinratesup + team1directmatchupwinratesup + team1indirectmatchupwinratesup) / 15
print("\nUpdated celkový winrate prvého tímu je :",team1winrates,"\n")
print("Updated celkový winrate druhého tímu je :",team2winrates,"\n")

team1compatibility = team1compatibilitywinratetop + team1compatibilitywinratejg + team1compatibilitywinratemid + team1compatibilitywinratebot + team1compatibilitywinratesup
team1directmatchup = team1directmatchupwinratetop + team1directmatchupwinratejg + team1directmatchupwinratemid + team1directmatchupwinratebot + team1directmatchupwinratesup
team1indirectmatchup = team1indirectmatchupwinratetop + team1indirectmatchupwinratejg + team1indirectmatchupwinratemid + team1indirectmatchupwinratebot + team1indirectmatchupwinratesup

team2compatibility = team2compatibilitywinratetop + team2compatibilitywinratejg + team2compatibilitywinratemid + team2compatibilitywinratebot + team2compatibilitywinratesup
team2directmatchup = team2directmatchupwinratetop + team2directmatchupwinratejg + team2directmatchupwinratemid + team2directmatchupwinratebot + team2directmatchupwinratesup
team2indirectmatchup = team2indirectmatchupwinratetop + team2indirectmatchupwinratejg + team2indirectmatchupwinratemid + team2indirectmatchupwinratebot + team2indirectmatchupwinratesup


datas = {'team1compatibilitywinratetop': [team1compatibilitywinratetop], 
        'team1compatibilitywinratejg': [team1compatibilitywinratejg],
        'team1compatibilitywinratemid': [team1compatibilitywinratemid],
        'team1compatibilitywinratebot': [team1compatibilitywinratebot],
        'team1compatibilitywinratesup': [team1compatibilitywinratesup],
        'team1directmatchupwinratetop': [team1directmatchupwinratetop],
        'team1directmatchupwinratejg': [team1directmatchupwinratejg],
        'team1directmatchupwinratemid': [team1directmatchupwinratemid],
        'team1directmatchupwinratebot': [team1directmatchupwinratebot],
        'team1directmatchupwinratesup': [team1directmatchupwinratesup],
        'team1indirectmatchupwinratetop': [team1indirectmatchupwinratetop],
        'team1indirectmatchupwinratejg': [team1indirectmatchupwinratejg],
        'team1indirectmatchupwinratemid': [team1indirectmatchupwinratemid],
        'team1indirectmatchupwinratebot': [team1indirectmatchupwinratebot],
        'team1indirectmatchupwinratesup': [team1indirectmatchupwinratesup],
        'team1winrate': [team1winrate],
        'team2compatibilitywinratetop': [team2compatibilitywinratetop],
        'team2compatibilitywinratejg': [team2compatibilitywinratejg],
        'team2compatibilitywinratemid': [team2compatibilitywinratemid],
        'team2compatibilitywinratebot': [team2compatibilitywinratebot],
        'team2compatibilitywinratesup': [team2compatibilitywinratesup],
        'team2directmatchupwinratetop': [team2directmatchupwinratetop],
        'team2directmatchupwinratejg': [team2directmatchupwinratejg],
        'team2directmatchupwinratemid': [team2directmatchupwinratemid],
        'team2directmatchupwinratebot': [team2directmatchupwinratebot],
        'team2directmatchupwinratesup': [team2directmatchupwinratesup],
        'team2indirectmatchupwinratetop': [team2indirectmatchupwinratetop],
        'team2indirectmatchupwinratejg': [team2indirectmatchupwinratejg],
        'team2indirectmatchupwinratemid': [team2indirectmatchupwinratemid],
'team2indirectmatchupwinratebot': [team2indirectmatchupwinratebot],
'team2indirectmatchupwinratesup': [team2indirectmatchupwinratesup],
'team2winrate': [team2winrate],
'team1rankingSS': [team1rankingSS],
'team1rankingS': [team1rankingS],
'team1rankingA': [team1rankingA],
'team1rankingB': [team1rankingB],
'team1rankingC': [team1rankingC],
'team1rankingD': [team1rankingD],
'team2rankingSS': [team2rankingSS],
'team2rankingS': [team2rankingS],
'team2rankingA': [team2rankingA],
'team2rankingB': [team2rankingB],
'team2rankingC': [team2rankingC],
'team2rankingD': [team2rankingD]
}
data_frame = pd.DataFrame(datas)
data_frame.to_csv('output.txt')


datas34 = {'team1compatibilitywinratetop': [team1compatibilitywinratetop], 
        'team1compatibilitywinratejg': [team1compatibilitywinratejg],
        'team1compatibilitywinratemid': [team1compatibilitywinratemid],
        'team1compatibilitywinratebot': [team1compatibilitywinratebot],
        'team1compatibilitywinratesup': [team1compatibilitywinratesup],
        'team1directmatchupwinratetop': [team1directmatchupwinratetop],
        'team1directmatchupwinratejg': [team1directmatchupwinratejg],
        'team1directmatchupwinratemid': [team1directmatchupwinratemid],
        'team1directmatchupwinratebot': [team1directmatchupwinratebot],
        'team1directmatchupwinratesup': [team1directmatchupwinratesup],
        'team1indirectmatchupwinratetop': [team1indirectmatchupwinratetop],
        'team1indirectmatchupwinratejg': [team1indirectmatchupwinratejg],
        'team1indirectmatchupwinratemid': [team1indirectmatchupwinratemid],
        'team1indirectmatchupwinratebot': [team1indirectmatchupwinratebot],
        'team1indirectmatchupwinratesup': [team1indirectmatchupwinratesup],
        'team1winrate': [team1winrate],
        'team2compatibilitywinratetop': [team2compatibilitywinratetop],
        'team2compatibilitywinratejg': [team2compatibilitywinratejg],
        'team2compatibilitywinratemid': [team2compatibilitywinratemid],
        'team2compatibilitywinratebot': [team2compatibilitywinratebot],
        'team2compatibilitywinratesup': [team2compatibilitywinratesup],
        'team2directmatchupwinratetop': [team2directmatchupwinratetop],
        'team2directmatchupwinratejg': [team2directmatchupwinratejg],
        'team2directmatchupwinratemid': [team2directmatchupwinratemid],
        'team2directmatchupwinratebot': [team2directmatchupwinratebot],
        'team2directmatchupwinratesup': [team2directmatchupwinratesup],
        'team2indirectmatchupwinratetop': [team2indirectmatchupwinratetop],
        'team2indirectmatchupwinratejg': [team2indirectmatchupwinratejg],
        'team2indirectmatchupwinratemid': [team2indirectmatchupwinratemid],
'team2indirectmatchupwinratebot': [team2indirectmatchupwinratebot],
'team2indirectmatchupwinratesup': [team2indirectmatchupwinratesup],
'team2winrate': [team2winrate],
'team1ranking': [team1ranking],
'team2ranking': [team2ranking]
}
data_framey = pd.DataFrame(datas34)
data_framey.to_csv('output34.txt')





datas20 = {'team1compatibilitywinrate': [team1compatibilitywinrate], 
        'team1directmatchupwinrate': [team1directmatchupwinrate],
        'team1indirectmatchupwinrate': [team1indirectmatchupwinrate],
        'team1winrate': [team1winrate],
        'team2compatibilitywinrate': [team2compatibilitywinrate],
        'team2directmatchupwinrate': [team2directmatchupwinrate],
        'team2indirectmatchupwinrate': [team2indirectmatchupwinrate],
'team2winrate': [team2winrate],
'team1rankingSS': [team1rankingSS],
'team1rankingS': [team1rankingS],
'team1rankingA': [team1rankingA],
'team1rankingB': [team1rankingB],
'team1rankingC': [team1rankingC],
'team1rankingD': [team1rankingD],
'team2rankingSS': [team2rankingSS],
'team2rankingS': [team2rankingS],
'team2rankingA': [team2rankingA],
'team2rankingB': [team2rankingB],
'team2rankingC': [team2rankingC],
'team2rankingD': [team2rankingD]
}

data_framee = pd.DataFrame(datas20)
data_framee.to_csv('output20.txt')



datas8 = {'team1compatibilitywinrate': [team1compatibilitywinrate], 
        'team1directmatchupwinrate': [team1directmatchupwinrate],
        'team1indirectmatchupwinrate': [team1indirectmatchupwinrate],
        'team1winrate': [team1winrate],
        'team2compatibilitywinrate': [team2compatibilitywinrate],
        'team2directmatchupwinrate': [team2directmatchupwinrate],
        'team2indirectmatchupwinrate': [team2indirectmatchupwinrate],
'team2winrate': [team2winrate],
'team1ranking': [team1ranking],
'team2ranking': [team2ranking],
}

data_frameeeee = pd.DataFrame(datas8)
data_frameeeee.to_csv('output8.txt')



datas32 = {'team1compatibilitywinratetop': [team1compatibilitywinratetop], 
        'team1compatibilitywinratejg': [team1compatibilitywinratejg],
        'team1compatibilitywinratemid': [team1compatibilitywinratemid],
        'team1compatibilitywinratebot': [team1compatibilitywinratebot],
        'team1compatibilitywinratesup': [team1compatibilitywinratesup],
        'team1directmatchupwinratetop': [team1directmatchupwinratetop],
        'team1directmatchupwinratejg': [team1directmatchupwinratejg],
        'team1directmatchupwinratemid': [team1directmatchupwinratemid],
        'team1directmatchupwinratebot': [team1directmatchupwinratebot],
        'team1directmatchupwinratesup': [team1directmatchupwinratesup],
        'team1indirectmatchupwinratetop': [team1indirectmatchupwinratetop],
        'team1indirectmatchupwinratejg': [team1indirectmatchupwinratejg],
        'team1indirectmatchupwinratemid': [team1indirectmatchupwinratemid],
        'team1indirectmatchupwinratebot': [team1indirectmatchupwinratebot],
        'team1indirectmatchupwinratesup': [team1indirectmatchupwinratesup],
        'team1winrate': [team1winrate],
        'team2compatibilitywinratetop': [team2compatibilitywinratetop],
        'team2compatibilitywinratejg': [team2compatibilitywinratejg],
        'team2compatibilitywinratemid': [team2compatibilitywinratemid],
        'team2compatibilitywinratebot': [team2compatibilitywinratebot],
        'team2compatibilitywinratesup': [team2compatibilitywinratesup],
        'team2directmatchupwinratetop': [team2directmatchupwinratetop],
        'team2directmatchupwinratejg': [team2directmatchupwinratejg],
        'team2directmatchupwinratemid': [team2directmatchupwinratemid],
        'team2directmatchupwinratebot': [team2directmatchupwinratebot],
        'team2directmatchupwinratesup': [team2directmatchupwinratesup],
        'team2indirectmatchupwinratetop': [team2indirectmatchupwinratetop],
        'team2indirectmatchupwinratejg': [team2indirectmatchupwinratejg],
        'team2indirectmatchupwinratemid': [team2indirectmatchupwinratemid],
'team2indirectmatchupwinratebot': [team2indirectmatchupwinratebot],
'team2indirectmatchupwinratesup': [team2indirectmatchupwinratesup],
'team2winrate': [team2winrate]
}
data_frameee = pd.DataFrame(datas32)
data_frameee.to_csv('output32.txt')


anew_df = pd.DataFrame({'team1winrate': predictdatanew['team1winrate'],
                       'team2winrate': predictdatanew['team2winrate'],
                       'winner': predictdatanew['winner']})

anew_df.to_csv('analysisdf.txt')


