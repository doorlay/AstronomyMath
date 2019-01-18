# This will do my physics homeowork.
import math 

def temp():
  print("Is the star you're using the sun?")
  sun = input("Type 'yes' or 'no:")
  if sun == "yes":
    ts = 5778
    rs = 695508000
    d = float(input("What is the distance from the sun?"))
    c = 2 * d
    teq = math.sqrt(rs / c) * ts
    print("The temperature of the planet is {} Kelvin." .format(teq))

  else:
    ts = input("What is surface temperature of the star?")
    rs = input("What is the radius of the star?")
    d = input("What is the distance from the star?")
    c = 2 * float(d)
    teq = math.sqrt(float(rs)/c) * float(ts)
    print("The temperature of the planet is {} Kelvin." .format(teq))


def lum():
  r = input("What is the radius of the star?")
  t = input("What is the temperature of the star?")
  Lum1 = float(r) ** 2
  Lum = Lum1 * 4 * math.pi * (5.67 * (10 ** -8))
  Lum2 = float(t) ** 4
  LumWatts = Lum2 * Lum
  SolarUnit = 2.61 * (10 ** -27)
  LumSolar = LumWatts * SolarUnit
  print("The luminosity of the planet is {} Watts, or {} Solar Luminosities." .format(LumWatts, LumSolar))


def start():
  print("Are you solving for temperature or luminosity?")
  answer = input("Type 't' or 'l':")
  if answer == "t":
    temp()
  if answer == "l":
    lum()


start()
