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
