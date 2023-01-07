from data_scraper import get_warzone_stats
from name_scraper import fetch_names

user = ['LOST_Beniboy_XD', 'Ghost_Balor1916', 'ghost_danjel', 'AmirBacha19', 'IV_40_kirtap']

names_list = fetch_names("./chromedriver", 1)
names_list.extend(user)
print(names_list)
df = get_warzone_stats(names_list)
df.to_csv("warzonestats.csv")

