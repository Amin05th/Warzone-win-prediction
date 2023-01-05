from data_scraper import get_warzone_stats

user = ['LOST_Beniboy_XD', 'Ghost_Balor1916', 'ghost_danjel', 'AmirBacha19', 'IV_40_kirtap']

df = get_warzone_stats(user)
df.to_csv("warzonestats.csv")
