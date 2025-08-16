from datetime import date, timedelta

start_date = date(2025, 8, 16)
end_date = date(2025, 12, 31)

current_date = start_date

while current_date <= end_date:
    print(current_date.strftime("%d/%m/%Y"))
    current_date += timedelta(days=1)
