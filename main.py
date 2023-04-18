import ABM as abm
import matplotlib.pyplot as plt

n_trave=(int)(20/100*(50*50))
n_ovc=(int)((20*50*50)/100)
n_volkovi=(int)(2/100*(50*50))

velikost_sveta=(50,50)
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
    yt.append(Energija/n_trave)
    yo.append(no)
    yv.append(nv)
    
seznam=[xx,yt,yo,yv]

abm.narisi_graf(seznam,svet,STOP)
