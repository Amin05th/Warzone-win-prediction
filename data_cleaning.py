import numpy as np
import pandas as pd

df = pd.read_csv("warzonestats.csv")

# remove Unnamed column
df.drop(columns="Unnamed: 0", inplace=True)

# remove all not found data
indexes_of_not_found_players = df.index[df['name'] == "-1"].tolist()
df.drop(indexes_of_not_found_players, inplace=True, axis=0)

# remove duplicated columns
df.drop(columns="total_games_played", inplace=True)

# Kills + assists
df['kills_assists'] = df['kills'] + df['assists']

# death per match
df['deaths/match_ratio'] = df['deaths'] / df['games_played']

# suicides per match
df['suicides/match'] = df['suicides'] / df['games_played']

# killed by an enemy
df['killed_by_enemies'] = df['deaths'] - df['suicides']

# kills/match_ratio
df['kills/match_ratio'] = df['kills'] / df['games_played']

print(df.to_csv("cleaned_data.csv"))
