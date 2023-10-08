import requests
import json
import soco.alarms
import datetime


def fetch_next_alarm():
    response = requests.get("http://<USER>:<PASSWORD>@<MINISERVER_IP>/jdev/sps/io/<NAME_OR_UUID_OF_ALARM_CLOCK>/state")

    if 200 == response.status_code:
        response_dict = json.loads(response.content)
        next_alarm = response_dict["LL"]["value"]
        datetime_now = datetime.datetime.now().replace(second=0, microsecond=0)

        # if date is far off in the future, the "next_alarm" contains a date -> 'Mittwoch, 04.10. 07:00'
        # if not, the following format is used: 'Dienstag, 07:00'
        if 3 == len(next_alarm.split(" ")):
            alarm_day, alarm_date_time = next_alarm.split(", ")
            alarm_date, alarm_time = alarm_date_time.split(" ")
            print("date is far off in the future")
            exit(4)
        else:
            alarm_day, alarm_time = next_alarm.split(", ")
            alarm_hour = int(alarm_time.split(":")[0])
            alarm_minute = int(alarm_time.split(":")[1])
            datetime_alarm = datetime_now.replace(hour=alarm_hour, minute=alarm_minute)

            if alarm_day == "Heute":
                return datetime_alarm
            elif alarm_day == "Morgen":
                datetime_alarm += datetime.timedelta(days=1)
                return datetime_alarm
            else:
                for weekday_int, weekday_str in enumerate(["Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag", "Sonntag"]):
                    if weekday_str == alarm_day:
                        days_until_weekday = (weekday_int - datetime_now.weekday()) % 7
                        datetime_alarm += datetime.timedelta(days=days_until_weekday)
                        return datetime_alarm
    print("Something went horribly wrong :(")
    exit(3)


datetime_lox_alarm = fetch_next_alarm()
alarms = soco.alarms.get_alarms()


filtered_alarms = set()
for alarm in alarms:
    if alarm.zone.player_name == "<NAME_OF_YOUR_SONOS_SPEAKER>":
        filtered_alarms.add(alarm)


if len(filtered_alarms) == 0:
    print("No alarms found :(")
    exit(1)
elif len(filtered_alarms) > 1:
    print("Too many alarms found :(")
    exit(2)
else:
    print("Found exactly one alarm :)")

alarm = filtered_alarms.pop()

# Get the day of the week as a numeric value (0 for Monday, 1 for Tuesday, etc.)
day_of_week_numeric = int(datetime_lox_alarm.strftime("%w"))
alarm.recurrence = f"ON_{day_of_week_numeric}"
alarm.start_time = datetime.time(hour=int(datetime_lox_alarm.strftime("%H")), minute=int(datetime_lox_alarm.strftime("%M")))
alarm.enabled = True
alarm.save()

exit(0)
