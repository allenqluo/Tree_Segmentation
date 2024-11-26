
############
## Waddell K.L and B. Hiserote. 2005.
## The PNW - FIA Integrated Database User Guide and Documentation: Version 2.0.
############

import numpy as np

# init vars (or get from data)
def waddell_bm(species, DBH, HT):

    DBH = DBH/2.54
    HT = HT/0.3048
    BA = np.pi*(DBH/2.0)**2

    # White Fir
    if species == 'ABCO':
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
        BA = (6**2) * 0.005454154

        CF4 = 0.299039 + 1.91272*(1/HT) + 0.0000367217*(HT**2/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*(tmp_dbh**2)*HT*CF4
        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            
            if(small_TARIF <= 0.0):
                small_TARIF = 0.01
            CVTS=small_TARIF *((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)


        # factor wood density, covert to kg
        BOLEWT = CVTS*23.09*0.4536

        BB = np.exp(2.1069 + 2.7271*np.log10(DBH*2.54)) / 1000
        BLB = 13.0 + 12.4*(DBH*2.54/100)**2 * HT

        bio = BOLEWT + BB + BLB

    ####################

    # Red Fir
    if(species == 'ABMA'):
        tmp_dbh = DBH
        if (DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.231237 + 0.028176*(HT/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4
        TARIF = CV4*0.912733/(BA-0.087266)

        if (tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)^2 + (1.0+0.063*(6.0-DBH)^2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)
            

        #factor wood density, covert to kg
        BOLEWT = CVTS*22.46*0.4536

        BB = np.exp(1.47146 + 2.8421*np.log10(DBH*2.54)) / 1000
        BLB = np.exp(-4.1817 +  2.3324*np.log10(DBH*2.54/100) )

        bio = BOLEWT + BB + BLB

    ###################

    # Bigleaf maple
    if(species == 'ACMA'):
        
        CVTS=0.010178635*DBH**2.22462*HT**0.57561

        BOLEWT = CVTS*27.46*0.4536

        BB = 0
        BLB = 0

        bio = BOLEWT + BB + BLB

    #####################

    # White alder
    if(species == 'ALRH'):
        CVTSL = -2.672775 + 1.920617 * np.log10(DBH) + 1.074024*np.log10(HT)
        CVTS = 10^CVTSL

        BOLEWT = CVTS*23.09*0.4536
        BB = np.exp(-4.6424 + 2.4617 * np.log10(DBH*2.54) )

        BF = (np.exp(-4.5648 + 2.6232 * np.log10(DBH*2.54)))*(1/(2.7638 + 0.062*(DBH*2.54)**1.3364))
        BLB = np.exp(-4.5648 + 2.6232 * np.log10(DBH*2.54)) - BF

        bio = BOLEWT + BB + BLB

    #######################

    # Mountain dogwood (hardwood: use Pacific dogwood eq.)
    if(species == 'CONU'):
        CVTSL = -2.672775 + 1.920617 * np.log10(DBH) + 1.074024*np.log10(HT)
        CVTS = 10**CVTSL

        BOLEWT = CVTS*43.68*0.4536

        BB = 0
        BLB = 0

        bio = BOLEWT + BB + BLB

    #######################

    # Incense cedar
    if(species == 'LIDE'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.225786 + 4.44236*(1.0/HT)

        if(CF4 < 0.27):
            CF4 = 0.27

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4
        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        BOLEWT = CVTS*21.84*0.4536

        BB = np.exp(-13.3146 + 2.8594*np.log10(DBH*2.54))/1000
        BLB = 0.199 + 0.00381*(DBH*2.54)**2 * HT

        bio = BOLEWT + BB + BLB

    ####################

    if(species == 'PICO'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.422709 -0.0000612236 * (HT**2/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        BOLEWT = CVTS*23.71*0.4536

        BB = 3.2 + 9.1*((DBH*2.54)/100)**2 * HT
        BLB = 7.8 + 12.3 * ((DBH*2.54)/100)**2 * HT

        bio = BOLEWT + BB + BLB

    #####################

    # Jeffrey pine
    if(species == 'PIJE'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.402060 -0.899914 * (1/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF <= 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        BOLEWT = CVTS*23.71*0.4536

        BB = np.exp(-3.6263 + 1.34077 * np.log10(DBH*2.54) + 0.8567*np.log10(HT))
        BLB = np.exp(-4.1068 + 1.5177 * np.log10(DBH*2.54) + 1.0424*np.log10(HT))

        bio = BOLEWT + BB + BLB

    ##################

    # Western white pine
    if(species == 'PIMO'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.35855 - 0.488134 * (1/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        BOLEWT = CVTS*21.84*0.4536

        BB = 1.2 + 11.2 * ((DBH*2.54)/100)**2 * HT
        BLB = 9.5 + 16.8 * ((DBH*2.54)/100)**2 * HT

        bio = BOLEWT + BB + BLB

    ####################

    # Gray pine
    if(species == 'PISA'):
        
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.402060 -0.899914 * (1/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        BOLEWT = CVTS*26.83*0.4536

        BB = np.exp(-3.6263 + 1.34077 * np.log10(DBH*2.54) + 0.8567*np.log10(HT))
        BLB = np.exp(-4.1068 + 1.5177 * np.log10(DBH*2.54) + 1.0424*np.log10(HT))

        bio = BOLEWT + BB + BLB

    #################

    # Quaking aspen (hardwood)
    if(species == 'POTR'):
        CVTSL = -2.63536 + 1.946034 * np.log10(DBH) + 1.024793*np.log10(HT)
        CVTS = 10**CVTSL

        BOLEWT = CVTS*21.84*0.4536

        BB = 1.3 + 27.6 * ((DBH*2.54)/100)**2 * HT
        BLB = 1.7 + 26.2 * ((DBH*2.54)/100)**2 * HT

        bio = BOLEWT + BB + BLB


    ###################

    # Western chokecherry (hardwood: use cherry, no chokecherry found)
    if(species == 'PRVI'):
        CVTSL = -2.672775 + 1.920617 * np.log10(DBH) + 1.074024*np.log10(HT)
        CVTS = 10**CVTSL

        bio = CVTS*29.32*0.4536

    #############

    # Giant Sequoia
    if(species == 'SEGI'):
        CVTS = np.exp(-6.2597+1.9967*np.log(DBH) + 0.9642*np.log(HT))

        # factor wood density, covert to kg
        BOLEWT = CVTS*23.71*0.4536
        # BB = EXP(7.189689 + 1.5837 * np.log10(DBH*2.54) ) /1000
        # BLB = 7.8 + 26.2* ((DBH*2.54)/100 )**2 * HT
        BB=0
        BLB=0
        bio = BOLEWT + BB + BLB

    ###############

    # Canyon live oak
    if(species == 'QUCH'):
        CVTS = 0.0097438611 * DBH**2.20527 * HT**0.6119

        # factor wood density, covert to kg
        BOLEWT = CVTS*49.92*0.4536

        ADBH = (((DBH*2.54)/10)+0.48584)/0.96147
        OUTERVOL = 0.0031670596 * (ADBH**2.32519) * (HT**0.50591)
        INNERVOL = 0.0031670596 * (((DBH*2.54)/10)**2.32519) * (HT**0.50591)
        BB = (OUTERVOL-INNERVOL) * 23.71 * 0.4536
        BLB = 0

        bio = BOLEWT + BB + BLB

    #################

    # Black oak
    if(species == 'QUKE'):
        CVTS = 0.0072695058 * DBH**2.14321 * HT**0.7422

        # factor wood density, covert to kg
        bio = CVTS*34.94*0.4536

    #################

    # ARSP Manzanita speices

    # Sugar pine
    if(species == 'PILA'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0
            BA = 6**2 * 0.005454154

        CF4 = 0.35855 - 0.488134 * (1/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF < 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        # factor wood density, covert to kg
        BOLEWT = CVTS*21.22*0.4536

        BB = np.exp(2.183174 + 2.6610 * np.log10(DBH*2.54) ) /1000
        BLB = np.exp(-7.637 + 3.3648 * np.log10(DBH*2.54) )

        bio = BOLEWT + BB + BLB

    #################

    # Ponderosa pine (softwood)
    if(species == 'PIPO'):
        tmp_dbh = DBH
        if(DBH < 6.0):
            tmp_dbh = 6.0 
            BA = 6**2 * 0.005454154

        CF4 = 0.402060 -0.899914 * (1/tmp_dbh)

        if(CF4 < 0.3):
            CF4 = 0.3
        if(CF4 > 0.4):
            CF4 = 0.4

        CV4 = 0.005454154*tmp_dbh**2*HT*CF4

        TARIF = CV4*0.912733/(BA-0.087266)

        if(tmp_dbh > 6.0):
            CVTS=CV4*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)/(BA-0.087266)
        else:
            small_TARIF = 0.5*(6.0-DBH)**2 + (1.0+0.063*(6.0-DBH)**2) * TARIF
            if(small_TARIF <= 0.0):
                small_TARIF = 0.01

            CVTS=small_TARIF*((1.033*(1.0+1.382937*np.exp(-4.015292*(DBH/10.0))))*(BA+0.087266)-0.174533)

        # factor wood density, covert to kg
        BOLEWT = CVTS*23.71*0.4536

        BB = np.exp(-3.6263 + 1.34077 * np.log10(DBH*2.54) + 0.8567 * np.log10(HT) )
        BLB = np.exp(-4.1068 + 1.5177 * np.log10(DBH*2.54) + 1.0424 * np.log10(HT) )

        bio = BOLEWT + BB + BLB

    ################

    # Willow (softwood)
    if(species == 'SASC'):
        
        CVTS = 0.0067322665 * DBH ** 1.96628 * HT

        # factor wood density, covert to kg
        BOLEWT = CVTS*22.46*0.4536

        BB = 0
        BLB = 0

        bio = BOLEWT + BB + BLB
        
    ###############

    # California netmeg (hardwood)
    if(species == 'TOCA'):

        CVTSL = -2.464614 + 1.701993 * np.log10(DBH) + 1.067038 * np.log10(HT)
        CVTS = 10**CVTSL

        # factor wood density, covert to kg
        BOLEWT = CVTS*31.82*0.4536

        BB = 0.366 + 0.00058 * (DBH*2.54)**2 * HT
        BLB = 0.199 + 0.00381 * (DBH*2.54)**2 * HT

        bio = BOLEWT + BB + BLB

    ###############

    # Colden Chinkapin (softwood)
    if(species == 'CACH'):

        CVTS = 0.0120372264 * DBH**2.02232 * HT^0.68638

        # factor wood density, covert to kg
        BOLEWT = CVTS*29.95*0.4536

        BB = 0
        BLB = 0

        bio = BOLEWT + BB + BLB

    ###############
        
    # Birch (hardwood)
    if(species == 'BESP'):

        CVTSL = -2.672775 + 1.920617 * np.log10(DBH) + 1.074024*np.log10(HT)
        CVTS = 10**CVTSL

        BOLEWT = CVTS*18.72*0.4536

        BB = 0
        BLB = 0

        bio = BOLEWT + BB + BLB

    
    # Return the biomass value
    try:
        return bio
    except:
        print("No species match...")