from get_entity import *
import json
cables=readcables("/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/delhi/wiki Embassy Baghdad03-06")
city=[]
i=1
for cable in cables:
    pos=parts_of_speech(cable)
    entity=find_entities(pos)
    city.append(entity)
    print "processing  cable",i
    i=i+1
entity=[]
for i in city:
    for j in i:
        entity.append(j)
pg=dict((i,entity.count(i)) for i in entity)
gp=sorted(pg.items(),key=lambda (k,v):v)
f=open("/home/hp/Downloads/nlp_phase1/iitd_nlp/prototype/small/delhi/count wiki Embassy Baghdad03-06","a+")
for i in range(len(gp)):
    c=gp[i][0]+"::"+str(gp[i][1])
    f.write(c)
    f.write("\n")
f.close
    

