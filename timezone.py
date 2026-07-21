from datetime import datetime,timedelta,timezone
current_time_utc=datetime.now(timezone.utc)

offest_hours=int(input("Enter offest in hours : "))

user_timezone=timezone(timedelta(hours=offest_hours))

convert_time=current_time_utc.astimezone(user_timezone)

print(f"Current time in utc :{current_time_utc}")

print(f"The specified timezone : {convert_time}")