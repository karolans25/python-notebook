# Write your solution here
times = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
groceries_money = float(input("How much money do you spend on groceries in a week? "))

weekly_spend = times * lunch_price + groceries_money
daily_spend = weekly_spend / 7
print("Average food expenditure:")
print(f"Daily: {daily_spend} euros")
print(f"Weekly: {weekly_spend} euros")