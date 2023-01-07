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
        try:
            name = profile['data']['username']
            name_list.append(name)
        except Exception:
            name_list.append("-1")
        try:
            level = profile['data']['level']
            level_list.append(level)
        except Exception:
            level_list.append("-1")
        try:
            record_longest_win_streak = profile['data']['lifetime']['all']['properties']['recordLongestWinStreak']
            record_longest_win_streak_list.append(record_longest_win_streak)
        except Exception:
            record_longest_win_streak_list.append("-1")
        try:
            losses = profile['data']['lifetime']['all']['properties']['losses']
            losses_list.append(losses)
        except Exception:
            losses_list.append("-1")
        try:
            total_games_played = profile['data']['lifetime']['all']['properties']['totalGamesPlayed']
            total_games_played_list.append(total_games_played)
        except Exception:
            total_games_played_list.append("-1")
        try:
            win_loss_ratio = profile['data']['lifetime']['all']['properties']['winLossRatio']
            win_loss_ratio_list.append(win_loss_ratio)
        except Exception:
            win_loss_ratio_list.append("-1")
        try:
            games_played = profile['data']['lifetime']['all']['properties']['gamesPlayed']
            games_played_list.append(games_played)
        except Exception:
            games_played_list.append("-1")
        try:
            deaths = profile['data']['lifetime']['all']['properties']['deaths']
            deaths_list.append(deaths)
        except Exception:
            deaths_list.append("-1")
        try:
            wins = profile['data']['lifetime']['all']['properties']['wins']
            wins_list.append(wins)
        except Exception:
            wins_list.append("-1")
        try:
            kd_ratio = profile['data']['lifetime']['all']['properties']['kdRatio']
            kd_ratio_list.append(kd_ratio)
        except Exception:
            kd_ratio_list.append("-1")
        try:
            suicides = profile['data']['lifetime']['all']['properties']['suicides']
            suicides_list.append(suicides)
        except Exception:
            suicides_list.append("-1")
        try:
            kills = profile['data']['lifetime']['all']['properties']['kills']
            kills_list.append(kills)
        except Exception:
            kills_list.append("-1")
        try:
            assists = profile['data']['lifetime']['all']['properties']['assists']
            assists_list.append(assists)
        except Exception:
            assists_list.append("-1")
        try:
            record_kill_streak = profile['data']['lifetime']['all']['properties']['recordKillStreak']
            record_kill_streak_list.append(record_kill_streak)
        except Exception:
            record_kill_streak_list.append("-1")

        print(f"player {i} got scraped")

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
