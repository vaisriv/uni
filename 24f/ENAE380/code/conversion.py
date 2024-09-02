minutes_to_convert = 122
convert_label = " Minutes "
if minutes_to_convert == 1:
    convert_label = " Minute "

hours = int(minutes_to_convert / 60)
minutes = minutes_to_convert % 60

hour_label = " Hours, "
if hours == 1:
    hour_label = " Hour, "

minute_label = " Minutes"
if minutes == 1:
    minute_label = " Minute"

print(
    str(minutes_to_convert)
    + convert_label
    + "is the same as:\n"
    + str(hours)
    + hour_label
    + str(minutes)
    + minute_label
)
