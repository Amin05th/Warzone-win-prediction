import pandas as pd
import plotly.express as px


df = pd.read_csv("cleaned_data.csv")
df.drop(columns="Unnamed: 0", inplace=True)

# scatter plot for games_played and kills
graph = px.scatter(df, x="games_played", y="kills", size="kills", hover_name="name", color="wins")
graph.show()

# barplot of wins
sorted_dataframe_by_wins = df.sort_values("wins", ascending=False)
graph2 = px.bar(sorted_dataframe_by_wins, x="name", y="wins", color="games_played")
graph2.show()

# bar plot of kills + assists
sorted_dataframe_by_kills_assists = df.sort_values("kills_assists", ascending=False)
graph3 = px.bar(sorted_dataframe_by_kills_assists, x="name", y="kills_assists")
graph3.show()

# bar plot of kills and assists
sorted_dataframe_by_kills_assists = df.sort_values("kills_assists", ascending=False)
graph4 = px.bar(sorted_dataframe_by_kills_assists, x="name", y=["kills", "assists", "deaths"], barmode="group", hover_name="games_played")
graph4.show()


# bar plot of wins and losses
sorted_dataframe_by_kills_win_loss_ratio = df.sort_values("win_loss_ratio", ascending=False)
graph5 = px.bar(sorted_dataframe_by_kills_win_loss_ratio, x="name", y=["wins", "losses"], barmode="group", hover_name="games_played")
graph5.show()


# scatter matrix of kd_ratio win_loss_ratio deaths/match_ratio suicides/match_ratio kills/match_ratio
graph6 = px.scatter_matrix(df, dimensions=["kd_ratio", "win_loss_ratio", "deaths/match_ratio",
                                           "suicides/match_ratio", "kills/match_ratio"], hover_name="name")
graph6.show()

# strip of the highest player rank
graph7 = px.strip(df, x="name", y="level")
graph7.show()


