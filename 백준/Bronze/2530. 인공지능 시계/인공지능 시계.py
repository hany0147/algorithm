hour, minute, second = map(int, input().split()) 
reminder = int(input())

tmp_second = second + reminder
reminder_minute = tmp_second // 60
reminder_second = tmp_second % 60

minute += reminder_minute
second = reminder_second

if minute >= 60:
    hour += minute // 60
    minute %= 60

if hour >= 24:
    hour %= 24

print(hour, minute, second)