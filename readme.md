# Simulacija populacije

Simulacija temelji na interakciji med tremi agenti:

- Trava
- Ovce
- Volkovi

Vsak agent se nahaja v svoji plasti. Ogredje za simulacijo populacije je napisano v Python-u z uporabo tehnike Agent-Based Modeling (ABM).

# Kako deluje

V tej simulaciji se na 2D mreži simulira življenje treh vrst agentov: trave, ovac in volkov. V začetku simulacije so agenti naključno postavljeni po mreži, pri čemer se število agentov posamezne vrste določi s pomočjo parametrov, ki se podajo ob zagonu simulacije. Parametri se nastavijo v **main.py** datoteki in so trenutno nstavljeni na:

```Python
import ABM as abm

nx=50 #Velikosti pokrajine v x smeri
ny=50 #Velikosti pokrajine v y smeri
N=nx*ny #Površina pokrajine

n_trave=(int)(N*20/100) #Začetno število celic matrike, kjer je prisotna trava
n_ovc=(int)(N*20/100) #Začetno število ovc
n_volkovi=(int)(N*2/100)#Začetno število volkov

```

Vsak agent ima svojo energijo. Agenti se premikajo po mreži na naključne pozicije in se hranijo s sosednjimi agenti, če so ti primerni (npr. volk poje ovco | ovca poje travo). Če agentova energija pade pod določeno mejo (trenutna vrednost je 0), agent umre. Poleg tega se agenti razmnožujejo, če imajo dovolj energije. S tem ko se agenti premikajo tako zgubljajo energijo in jo s hrano nadomeščajo.

Vsaka simulacija se izvaja v več korakih, v katerih se agenti premikajo, hranijo, razmnožujejo ter umirajo. Med posameznimi koraki se lahko energija agentov povečuje ali zmanjšuje, odvisno od različnih dejavnikov, kot so na primer rast trave ali lov na ovce.

# Kako začeti simulacijo

- Namestite Python
- Prenesite datoteke simulacije
- Namestite potrebne knjižnice s pomočjo ukaza pip - install -r requirements.txt

- Zaženite datoteko main.pyž

# Prilagoditve simulacije

Simulacija se lahko prilagodi glede na različne dejavnike, kot so na primer:

- Velikost mreže, po kateri se agenti premikajo
- - Število agentov vsake vrste, ki se postavijo na mrežo ob začetku simulacije
- Energijski kriteriji za preživetje, premikanje in razmnoževanje agentov
- Vsak od teh dejavnikov se lahko prilagodi v datoteki main.py.

Simulacija je licencirana pod MIT licenco.