import random
import matplotlib.pyplot as plt
import sys
from typing import List, Tuple

# import pygame #Rabimo do naslednjič

class Simulacija:
    def __init__(self,velikost_sveta: Tuple[int, int],populacija: List[int]):
        '''
        velist_sveta -> [dolzina,sirina] je int, ki nam pove koliko celicl imamo v x in koliko v y smeri.
        populacij -> list[pop_trave,pop_ovc,pop_volk] za vsako vrsto podam int število, ki pove, koliko je teh agentov
        '''
        
        grid_x, grid_y = velikost_sveta
        self.size_x=grid_x
        self.size_y=grid_y
        
        Ng, No, Nv = populacija
        self.svet: List[List[List]] = [[[None,None,None] for y in range(grid_y)] for x in range(grid_x)]
        
        #svet[x][y][0] -> Trava
        #svet[x][y][1] -> Ovca
        #svet[x][y][2] -> Volk
        
        self.seznam_volkov=[]
        self.seznam_ovc=[]
        self.seznam_trave=[]
        
        #poselimo svet
        for i in range(Ng):
            x=random.randint(0,grid_x-1)
            y=random.randint(0,grid_y-1)
            
            #V mojem svetu na lokaxiji x,y ustvarim travo
            agent=Simulacija.Trava(x,y)
            self.svet[x][y][0]=agent # type: ignore
            self.seznam_trave.append(agent)
            
        
        for i in range(No):
            x=random.randint(0,grid_x-1)
            y=random.randint(0,grid_y-1)
            # Tukaj želim ustvariti ovco
            agent=Simulacija.Ovca(x,y)
            self.svet[x][y][1]=agent # type: ignore
            self.seznam_ovc.append(agent)
        
        for i in range(Nv):
            x=random.randint(0,grid_x-1)
            y=random.randint(0,grid_y-1)
            # Tukaj želim ustvariti volka
            agent=Simulacija.Volk(x,y)
            self.svet[x][y][2]=agent # type: ignore
            self.seznam_volkov.append(agent)
    
    def posodobi_svet(self):
        Energija=0
        for trava in self.seznam_trave:
            trava.rast_trave()
            Energija+=trava.energija
        
        no=0
        for ovca in self.seznam_ovc:
            ovca.premik(self)
            ovca.obed(self)
            ovca.razmnozevanje(self)
            
            if ovca.status=="Živa":
                no+=1 
            
        nv=0
        for volk in self.seznam_volkov:
            volk.premik(self)
            volk.obed(self)
            volk.razmnozevanje(self)
            if volk.status=="Živa":
                nv+=1 
        
        return [Energija,no,nv]
        
    
    
    class Trava:
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.energija=10
            self.name=f"trava_id_{id(self):04d}"
        
        def rast_trave(self):
            self.energija += 0.2
    
    class Ovca:
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.energija=20
            self.name=f"Ovca_id_{id(self):04d}"
            self.status="Živa"
        
        def premik(self,glob):
            '''
            Premika se lahko gor, dol, levo in desno. !!Periodični robni pogoji
            '''
            
            nov_x = self.x + random.choice([-1,0,1])
            nov_y = self.y + random.choice([-1,0,1])
            
            if nov_x>glob.size_x-1:
                nov_x=0
            if nov_x<0:
                nov_x=glob.size_x-1
    
            if nov_y>glob.size_y-1:
                nov_y=0
            if nov_y<0:
                nov_y=glob.size_y-1
            
            self.x=nov_x
            self.y=nov_y
            self.energija -= 0.2

            if self.energija <= 0:
                self.status="Pokojna"
                glob.svet[self.x][self.y][1]=None
        
        def obed(self,glob):
            if glob.svet[self.x][self.y][0]!=None:
                if glob.svet[self.x][self.y][0].energija>0:
                    self.energija+=glob.svet[self.x][self.y][0].energija
                    glob.svet[self.x][self.y][0].energija=-2
                    
        def razmnozevanje(self,glob):
            #Energijski kriterij#
            
            if self.energija>30:
                baby_x=random.randint(0,glob.size_x-1)
                baby_y=random.randint(0,glob.size_y-1)
                
                while glob.svet[baby_x][baby_y][1]!=None:
                    baby_x=random.randint(0,glob.size_x-1)
                    baby_y=random.randint(0,glob.size_y-1)
                
                self.energija-=20#Toliko energije podeli novi ovci
                
                agent=Simulacija.Ovca(baby_x,baby_y)
                glob.svet[baby_x][baby_y][1]=agent
                glob.seznam_ovc.append(agent)

    class Volk:
        def __init__(self,x,y):
            self.x=x
            self.y=y
            self.energija=50
            self.name=f"Volk_id_{id(self):04d}"
            self.status="Živa"
        
        def premik(self,glob):
            '''
            Premika se lahko gor, dol, levo in desno. !!Periodični robni pogoji
            '''
            
            nov_x = self.x + random.choice([-1,0,1])
            nov_y = self.y + random.choice([-1,0,1])
            
            if nov_x>glob.size_x-1:
                nov_x=0
            if nov_x<0:
                nov_x=glob.size_x-1
    
            if nov_y>glob.size_y-1:
                nov_y=0
            if nov_y<0:
                nov_y=glob.size_y-1
            
            self.x=nov_x
            self.y=nov_y
            self.energija -= 0.5

            if self.energija<0:
                self.status="Pokojna"
                wolf_to_remove = glob.svet[self.x][self.y][2]
                if wolf_to_remove in glob.seznam_volkov: 
                    glob.seznam_volkov.remove(wolf_to_remove)
                glob.svet[self.x][self.y][2]=None
        
        def obed(self,glob):
            if glob.svet[self.x][self.y][1]!=None:
                if glob.svet[self.x][self.y][1].energija>0:
                    self.energija+=glob.svet[self.x][self.y][1].energija
                    glob.svet[self.x][self.y][1]=None
        
        def razmnozevanje(self,glob):
            #Energijski kriterij#
            if self.energija>80:
                print("Novi volk")
                baby_x=random.randint(0,glob.size_x-1)
                baby_y=random.randint(0,glob.size_y-1)
            
                while glob.svet[baby_x][baby_y][2]!=None:
                    baby_x=random.randint(0,glob.size_x-1)
                    baby_y=random.randint(0,glob.size_y-1)
                    
                
                self.energija-=50
                agent=Simulacija.Volk(baby_x,baby_y)
                glob.svet[baby_x][baby_y][2]=agent
                glob.seznam_volkov.append(agent)
    
                
                