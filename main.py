import ABM as abm
import matplotlib.pyplot as plt

n_trave=80
n_ovc=20
n_volkovi=1

velikost_sveta=(10,10)
populacija=[n_trave,n_ovc,1]

svet=abm.Simulacija(velikost_sveta,populacija)

print(len(svet.seznam_trave))
print(len(svet.seznam_ovc))
print(len(svet.seznam_volkov))
#seznam=svet.seznam_trave
seznam=svet.seznam_ovc


nx,ny,pokrajina=velikost_sveta[0],velikost_sveta[1],svet.svet

xx=[]
yt=[]
yo=[]
yv=[]

seznam=[]

STOP=1000
for time in range(STOP):
    Energija,no,nv=svet.posodobi_svet()
    
    print(time,Energija,no,nv)
    xx.append(time)
    yt.append(Energija)
    yo.append(no)
    yv.append(nv)
    
seznam=[xx,yt,yo,yv]

abm.narisi_graf(seznam,svet,STOP)
