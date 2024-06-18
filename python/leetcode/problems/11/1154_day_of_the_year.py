import datetime

class Solution:
    def dayOfYear(self, date: str) -> int:
        print(f"{date=}")
        cus_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
        print(f"{cus_date=}")
        day_of_year = cus_date.strftime("%-j")
        print(f"{day_of_year=}")
        return int(day_of_year)

