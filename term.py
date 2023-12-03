from enum import Enum
from datetime import datetime

spring = "spring"
summer = "summer"
fall = "fall"
season_list = [spring, summer, fall]


class Season(Enum):
    SPRING = spring
    SUMMER = summer
    FALL = fall

    def next_season(self):
        current_index = season_list.index(self.value)
        next_index = (current_index + 1) % len(season_list)
        next_season = season_list[next_index]
        return Season(next_season)

    def previous_season(self):
        current_index = season_list.index(self.value)
        previous_index = (current_index - 1) % len(season_list)
        previous_season = season_list[previous_index]
        return Season(previous_season)


class Term:
    def __init__(self, season: Season, year: int):
        if not isinstance(season, Season):
            raise ValueError(
                "Invalid term. Please use values from the Term Enum.")
        if not isinstance(year, int):
            raise ValueError("Year must be an integer.")
        self.season = season
        self.year = year

    def previous_term(self):
        previous_season = self.season.previous_season()
        previous_year = self.year - 1 if previous_season == Season.FALL else self.year
        return Term(previous_season, previous_year)

    def next_term(self):
        next_season = self.season.next_season()
        next_year = self.year + 1 if next_season == Season.SPRING else self.year

        return Term(next_season, next_year)
    
    def __str__(self):
        return f"{self.season.value.capitalize()} {self.year}"


def get_current_term():
    current_datetime = datetime.now()
    current_month = current_datetime.month

    if 1 <= current_month <= 4:
        current_season = Season.SPRING
    elif 5 <= current_month <= 8:
        current_season = Season.SUMMER
    else:
        current_season = Season.FALL
    current_year = current_datetime.year

    return Term(current_season, current_year)
