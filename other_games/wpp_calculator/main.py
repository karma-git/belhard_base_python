import eel
import wppr_calculator


@eel.expose
def display_wpprs_pick_up(x, y, z, roll_weight, roll_length):
    try:
        x, y, z, roll_weight, roll_length = float(x), float(y), float(z), float(roll_weight) / 100, float(roll_length) #multiply by 10 coz
        if x <= 0 or y <= 0 or z <= 0 or roll_weight <= 0 or roll_length <= 0:
            return f"Some of the params less then 0!\nPlease have a check"
    except ValueError:
        return f"Wrong params!\nPlease have a check"
    place = wppr_calculator.Room(x, y, z)
    wp = wppr_calculator.WallPapers(roll_weight, roll_length)
    if wp.sqr() <= place.wallpapers_sqr():
        return f"Total room square - {round(place.sqr(), 2)} sq m" \
               f"<br>Square w/o excess objects - {round(place.wallpapers_sqr(), 2)} sq m\n" \
               f"<br>Needs {round(place.roll_count(), 1)} rolls of the wallpapers"
    else:
        return f"Oops. Seems like a roll square higher than Walls square. Have a check please"


eel.init("web")

eel.start("main.html", size=(1280, 768))

