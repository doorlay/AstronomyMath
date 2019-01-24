# imports the math module for some more math functionality
import math

# The code for my new astronomy calculator.
# This will also do my physics homework for me.
# It will calculate temperature of planets, distance from stars, and 
# radius of planets.

def period():
  t = (input("What is the period of the stars orbit, in days?"))
  l = t/365
  return float(l)

def radius():
  hey = input("What is the radius of the star, in relation to the sun?")
  return float(hey)

def temp():
  ts = input("What is the temperature of the star, in Kelvin?")
  return float(ts)

def flux():
  deltaf = input("What is the change in Flux?")
  return float(deltaf)

def mass():
  ms = (input("What is the mass of the star?"))
  return float(ms)

def ask():
  print("Welcome to the astronomy calculator!")
  t = period()
  rs = radius()
  ts = temp()
  deltaf = flux()
  ms = mass()
  distance1 = (t ** 2) * ms
  distance = distance1 ** (1/3)
  print("The distance is {} AU." .format(distance))
  radius1 = deltaf * (rs ** 2)
  radius2 = radius1 ** (1/2)
  print("The radius of the planet is {} radii of the sun." .format(radius2))
  temperature1 = radius2 / (2 * distance)
  temperature = ts * (temperature1 ** (1/2))
  print("The average temperature of the planet is {} Kelvin." .format(temperature))

ask()
