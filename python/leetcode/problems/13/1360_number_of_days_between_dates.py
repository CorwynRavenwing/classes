from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        date_format = '%Y-%m-%d'
        d1 = datetime.strptime(date1, date_format)
        d2 = datetime.strptime(date2, date_format)
        delta = d2 - d1
        return abs(delta.days)

