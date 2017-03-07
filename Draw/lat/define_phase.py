# encoding utf-8

def define_phase(number, i):

    if number == 31320: # old composite
#----------------mmt
        if (i < 721
        or (i > 3480 and i < 4201)
        or (i > 6960 and i < 7681)
        or (i > 10440 and i < 11161)
        or (i > 13920 and i < 14641)
        or (i > 17420 and i < 18121)
        or (i > 20880 and i < 21601)
        or (i > 24360 and i < 25081)
        or (i > 27840 and i < 28561)):
            return 1 
   
#---------------modifier
        elif ((i > 720 and i < 1561)
        or (i > 4200 and i < 5041)
        or (i > 7680 and i < 8521)
        or (i > 11160 and i < 12001)
        or (i > 14640 and i < 15481)
        or (i > 18120 and i < 18961)
        or (i > 21600 and i < 22441)
        or (i > 25080 and i < 25921)
        or (i > 28560 and i < 29401)):
            return 2

#---------------polymer
        else:
            return 3

    elif number == 31230: # new 5 chains
        if (i < 721
        or (i > 3470 and i < 4191)
        or (i > 6940 and i < 7661)
        or (i > 10410 and i < 11131)
        or (i > 13880 and i < 14601)
        or (i > 17350 and i < 18071)
        or (i > 20820 and i < 21541)
        or (i > 24290 and i < 25011)
        or (i > 27760 and i < 28481)):
            return 1
        elif ((i > 720 and i < 1561)
        or (i > 4190 and i < 5031)
        or (i > 7660 and i < 8501)
        or (i > 11130 and i < 11971)
        or (i > 14600 and i < 15441)
        or (i > 18070 and i < 18911)
        or (i > 21540 and i < 22381)
        or (i > 25010 and i < 25851)
        or (i > 28480 and i < 29321)):
            return 2
        else:
            return 3

    elif number == 48420: # new 10 chains
        if (i < 721
        or (i > 5380 and i < 6101)
        or (i > 10760 and i < 11481)
        or (i > 16140 and i < 16861)
        or (i > 21520 and i < 22241)
        or (i > 26900 and i < 27621)
        or (i > 32280 and i < 33001)
        or (i > 37660 and i < 38381)
        or (i > 43040 and i < 43761)):
            return 1
        elif ((i > 720 and i < 1561)
        or (i > 6100 and i < 6941)
        or (i > 11480 and i < 12321)
        or (i > 16860 and i < 17701)
        or (i > 22240 and i < 23081)
        or (i > 27620 and i < 28461)
        or (i > 33000 and i < 33841)
        or (i > 38380 and i < 39221)
        or (i > 43760 and i < 44601)):
            return 2
        else:
            return 3
