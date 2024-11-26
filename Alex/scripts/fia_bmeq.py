import numpy as np

#### Equations

# 1
def eq1(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a + b * (np.log10(DBH**c))
    return biomass
# 2
def eq2(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b * DBH + c * (np.log(DBH**d)) + e*ht
    return biomass

# 3
def eq3(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b * np.log(DBH) + c * (d + e * np.log(DBH))
    return biomass

# 4
def eq4(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b * DBH + c * (DBH ** d) + e*(DBH**2)*HT
    return biomass

# 5
def eq5(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b * DBH + c * (DBH ** 2) + d * (DBH**3) + e*DBH*HT
    return biomass

# 6
def eq6(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a * (np.exp(b + c * np.log(DBH) + d * DBH))
    return biomass

# 7
def eq7(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + (b * DBH**c)/(DBH**c + d)
    return biomass

# 8
def eq8(*args):
    a,b = args[0],args[1]
    biomass = a + b * np.log10(DBH)
    return biomass

# 9
def eq9(*args):
    a,b = args[0],args[1]
    biomass = np.log(a) + (b * np.log(DBH))
    return biomass

# 10
def eq10(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass= np.exp(a + b*np.log(DBH))*np.exp(c + d/DBH)
    return biomass

# 11
def eq11(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + b*(DBH**2)*HT + c*(DBH**3) + d*DBH*HT
    return biomass

# 12
def eq12(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a + b*np.log(DBH) + c*np.log(HT)
    return biomass

# 13
def eq13(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = np.exp(a + b*np.log(DBH) + d*np.log(HT))*c
    return biomass

# 14
def eq14(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = np.exp(a + b*np.log(DBH))/(c + d*(DBH**e))
    return biomass

# 15
def eq15(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a + b*HT + c*(HT**2)
    return biomass

# 16
def eq16(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a * (DBH**b) * (HT**c)
    return biomass

# 17
def eq17(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b*DBH + c*(DBH**2) + d*HT + e*(DBH**2)*HT
    return biomass

# 18
def eq18(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + b*np.log(DBH) + c*np.log(CR) + d*np.log(CR*HT)
    return biomass

# 19
def eq19(*args):
    a,b,c = args[0],args[1],args[2]
    ratio = 1 - (np.exp(a*TopD**b*DBH**c))
    return ratio

# 20
# BIOMASS_FIA_NC
# 21
# BIOMASS_FIA_NE
# 22
# BIOMASS_FIA_RM
# 23
# BIOMASS_FIA_RM2
# 24
# BIOMASS_FIA_SE
# 25
# BIOMASS_FIA_NW
# 26
# BIOMASS_FIA_NW_STANDISH
# 27
# BIOMASS_FIA_NW_SHAW
# 28
# BIOMASS_FIA_NW_GHOLZ1
# 29
# BIOMASS_FIA_NW_GHOLZ2
# 30
# BIOMASS_FIA_NW_SNELL
# 31
# BIOMASS_FIA_NW_PILLSBURY
# 32
# BIOMASS_FIA_NW_REDWOOD
# 33
def eq33(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    
    if DBH < 11:
        biomass = a * (DBH**2)**b
    else:
        biomass = c * (DBH**2)**d
    
    return biomass

# 34
def eq34(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    
    if DBH < 11:
        biomass = a * (DBH**2 * HT)**b
    else:
        biomass = c * (DBH**2)**d * HT**e
    
    return biomass

# 35
def eq35(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + b*DBH**3 + c*(DBH**2)*CR + d*(DBH**2)*HT*CR
    return biomass

# 36
def eq36(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b*(DBH**2) + c*(DBH**2)*ht + d*DBH*HT*CR + e*(DBH**2)*HT*CR
    return biomass

# 37
def eq37(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a + b*np.log(DBH*HT) + c*np.log(HT*CR)
    return biomass

# 38
def eq38(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + b*HT + c*HT*CR + d*DBH*HT*CR
    return biomass

# 39
def eq39(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a * DBH**b * HT**c * np.exp(d*CL/HT)
    return biomass

# 40
def eq40(*args):
    a,b,c,d,e = args[0],args[1],args[2],args[3],args[4]
    biomass = a + b*(DBH**c) * (HT**d) * (CL**e)
    return biomass

# 41
def eq41(*args):
    a,b = args[0],args[1]
    biomass = BRL/(1+a*DBH**b)
    return biomass

# 42
def eq42(*args):
    a,b,c = args[0],args[1],args[2]
    biomass = a*(DBH**b) * np.exp(c*HT)
    return biomass

# 43
def eq43(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a*(DBH**2)*HT*(b+c*TopD/DBH+d*(TopD/DBH)**2)/100
    return biomass
                                       
# 100
def eq100(*args):
    a,b,c,d = args[0],args[1],args[2],args[3]
    biomass = a + b*np.log(DBH) + c*np.log(HT) + d*np.log(p)
    return biomass

# 101
def eq101(*args):
    a,b = args[0],args[1]
    biomass = a + b*np.log(D2H*p)
    return biomass

# 102
def eq102(*args):
    a,b = args[0],args[1]
    biomass = a + (D2H*p)**b
    return biomass

# 103
# BIOMASS_FIA_PACIFIC_ISLANDS

##############
####### 
##############

equationDict = {"1":eq1,'2':eq2,'3':eq3,"4":eq4,"5":eq5,"6":eq6,"7":eq7,"8":eq8,"9":eq9,'10':eq10,"11":eq11,
                "12":eq12,"13":eq13,"14":eq14,"15":eq15,"16":eq16,"17":eq17,"18":eq18,"19":eq19,"33":eq33,
                "34":eq34,"35":eq35,"36":eq36,"37":eq37,"38":eq38,"39":eq39,"40":eq40,"41":eq41,"42":eq42,
                "43":eq43,"100":eq100,"101":eq101,"102":eq102}

## Equation searcher
def bm_eq(id=None,DBH=None,HT=None,BA=None,CR=None,*args):
    BA = np.pi*(DBH/2.0)**2
    eq = equationDict[id](*args, **kwargs)
    bio = eq(args)

    # return the calculated biomass
    return bio