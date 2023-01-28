# Warzone-win-prediction: Project Overview

- Created a tool that estimates the wins in Warzone based on their stats
- Scraped over 300 player stats from cod.tracker.gg and the api Warzonestats
- Optimized KNeighborsRegressor, LinearRegression and RandomForestRegressor using GridsearchCV to reach the best model
- Build a visualizetion webside using streamlit.io

## Code and Resources Used
**Python Version:** 3.10
**Packages:** pandas, numpy, sklearn, plotly, selenium, streamlit.io, pickle, WarzoneStats
**Scraper Article**: [https://cod.tracker.gg/warzone/leaderboards/battle-royale/](https://cod.tracker.gg/warzone/leaderboards/battle-royale/)

## Web Scraping

Tweaked the web scraper github repo (above) to scrape 300 player stats from cod.tracker.gg. With each stats, we got the following

- name
- level
- record_longest_win_streak
- losses
- total_games_played
- win_loss_ratio
- games_played
- deaths
- wins
- kd_ratio
- suicides
- kills
- assists
- record_kill_streak

## Data Cleaning

After scraping and downloading the data from api, I needed to clean it up so that it was usable for our model. I made the following changes and created the following variables:

- Removed usless and unuseable data
- Made usefull columns (Kills + assists)
- Made columns for diffrent Ratios (death per match, suicides per match, killed by an enemy, kills/match_ratio)

## EDA

Made some usefull plots for the analasys. Made some barplots, Scatterplots, etc.

## Model Building

First splitted the Data to train and test splits with 20% test size

I tried three different models and evaluated them using Mean Absolute Error. I chose MAE because it is relatively easy to interpret and outliers aren’t particularly bad in for this type of model.

I tried three different models:
