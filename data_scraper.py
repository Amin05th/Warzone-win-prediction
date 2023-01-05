import json
from WarzoneStats import Api
import pandas as pd


def get_warzone_stats(user):
    name_list = []
    level_list = []
    record_longest_win_streak_list = []
    losses_list = []
    total_games_played_list = []
    win_loss_ratio_list = []
    games_played_list = []
    deaths_list = []
    wins_list = []
    kd_ratio_list = []
    suicides_list = []
    kills_list = []
    assists_list = []
    record_kill_streak_list = []

    platform = "psn"
    sso = "MTU1NTYzMzE1MzYyNDgyNDE2MTY6MTY3NDA0NDcxMjgzMjoyYjYxYmUxM2JhNWE0ZDEzZmJmMTk4ZDBlMjZhMDIzYQ"
    for i in user:
        api = Api(i, platform, sso)
        profile = api.get_profile()

        name = profile['data']['username']
        name_list.append(name)
        level = profile['data']['level']
        level_list.append(level)
        record_longest_win_streak = profile['data']['lifetime']['all']['properties']['recordLongestWinStreak']
        record_longest_win_streak_list.append(record_longest_win_streak)
        losses = profile['data']['lifetime']['all']['properties']['losses']
        losses_list.append(losses)
        total_games_played = profile['data']['lifetime']['all']['properties']['totalGamesPlayed']
        total_games_played_list.append(total_games_played)
        win_loss_ratio = profile['data']['lifetime']['all']['properties']['winLossRatio']
        win_loss_ratio_list.append(win_loss_ratio)
        games_played = profile['data']['lifetime']['all']['properties']['gamesPlayed']
        games_played_list.append(games_played)
        deaths = profile['data']['lifetime']['all']['properties']['deaths']
        deaths_list.append(deaths)
        wins = profile['data']['lifetime']['all']['properties']['wins']
        wins_list.append(wins)
        kd_ratio = profile['data']['lifetime']['all']['properties']['kdRatio']
        kd_ratio_list.append(kd_ratio)
        suicides = profile['data']['lifetime']['all']['properties']['suicides']
        suicides_list.append(suicides)
        kills = profile['data']['lifetime']['all']['properties']['kills']
        kills_list.append(kills)
        assists = profile['data']['lifetime']['all']['properties']['assists']
        assists_list.append(assists)
        record_kill_streak = profile['data']['lifetime']['all']['properties']['recordKillStreak']
        record_kill_streak_list.append(record_kill_streak)

    return pd.DataFrame(
        {
            "name": name_list,
            "level": level_list,
            "record_longest_win_streak": record_longest_win_streak_list,
            "losses": losses_list,
            "total_games_played": total_games_played_list,
            "win_loss_ratio": win_loss_ratio_list,
            "games_played": games_played_list,
            "deaths": deaths_list,
            "wins": wins_list,
            "kd_ratio": kd_ratio_list,
            "suicides": suicides_list,
            "kills": kills_list,
            "assists": assists_list,
            "record_kill_streak": record_kill_streak_list,
        })
