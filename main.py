import json
from zoneinfo import ZoneInfo
from adhanpy.PrayerTimes import PrayerTimes, CalculationMethod
from datetime import datetime

def clean_format(d: datetime):
    return d.strftime("%H:%M")

def dict_to_string(data: dict) -> str:
    header = "<b>Prayer Time</b>\n\n"
    return header  + "\n".join(f"{key}\t{value}" for key, value in data.items())

time_zone = ZoneInfo("Asia/Jakarta")
today = datetime.now(tz=time_zone)

# FIXME: Harcoded coordinates & methods (use Args)
coordinates = (-6.217281, 106.812991)
cm = CalculationMethod.SINGAPORE

prayer_times = PrayerTimes(coordinates,
                           datetime.now(),
                           cm,
                           time_zone=time_zone
                           )

prayers = ["fajr", "dhuhr", "asr", "maghrib", "isha"]

all_shalat = dict()
next_shalat = dict()
for p in prayers:
    shalat_time = getattr(prayer_times, p, None)

    if not shalat_time:
        continue

    all_shalat[p] = clean_format(shalat_time)

    if len(next_shalat.keys()) == 0 and today < shalat_time:
        next_shalat["name"] = p
        next_shalat["time"] = clean_format(shalat_time)

# TODO: Add custom class to remind shalat
output = {
    "text": f"{next_shalat['name']} {next_shalat['time']}",
    "tooltip": dict_to_string(all_shalat),
    "class": "class"
}

print(json.dumps(output))
