# -*- coding: utf-8 -*-
"""
calculator for astrophysics problems
"""

import math

#constants
m_sun = 2e30 #kg
r_sun = 7e8 #meters
r_earth = 6.38e6 #meters

#star/planet parameters
period = 18.77 #days
i = 89.80 #degrees
m_star = 0.09 #solar masses
r_star = 0.12 #solar radii
depth = 0.04

a = (m_star * (period/365)**2)**(1/3) #AUs

b = a*1.5e11*math.cos(i*2*math.pi/360)/(r_star*r_sun) #stellar radii

r_planet = r_star*r_sun*(depth)**(1/2) / r_earth #earth radii

t_dur = period*24*60 / math.pi *((r_star*r_sun/(a*1.5e11))**2-(math.cos(i*2*math.pi/360))**2)**(1/2)

print(a,r_planet,b,t_dur)