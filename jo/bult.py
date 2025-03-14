from datetime import datetime, date, timedelta

# print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))
# print([x**2 for x in [1, 2, 3, 4, 5]])

# print(list(filter(lambda x: x % 2 == 0, [1,2,3,4,5,6])))
# print([x for x in [1,2,3,4,5,6] if x % 2 == 0])

# date_str = "25-12-2024 15:30:45"
# parsed_date = datetime.strptime(date_str, "%d-%m-%Y %H:%M:%S")
# print(parsed_date)  # 2024-12-25 15:30:45

# date1 = date(2025, 3, 12)
# date2 = date(2023, 1, 21)
# print((date1-date2).days)

# future = datetime.now()+timedelta(days=5)
# print(future.strftime('%x'))

# today = datetime.now() + timedelta(days=3)

# print(today.weekday())  # 3 (0 = Пн, 6 = Вс)
# print(today.strftime("%A"))  # Friday (англ. название)

