from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM('de4c5eaf83e119351d5cf61a5e4477ba')
mgr = owm.weather_manager()

place = input("Enter your city/country: ")
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(place)
w = observation.weather

print(w)
