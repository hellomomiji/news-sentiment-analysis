from datetime import datetime,date, timedelta

print(date.today())
n_days_ago = date.today() - timedelta(days=7)
print(n_days_ago)