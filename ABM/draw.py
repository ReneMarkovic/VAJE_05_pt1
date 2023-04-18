import matplotlib.pyplot as plt
import numpy as np
from typing import List, Tuple

def convert_to_array(glob):
    plasti=glob.svet
    grid_x=glob.size_x
    grid_y=glob.size_y
    
    layer_trava = np.zeros([grid_x, grid_y], dtype=float)
    layer_ovce = np.zeros([grid_x, grid_y], dtype=float)
    layer_volk = np.zeros([grid_x, grid_y], dtype=float)

    # Iterate through the nested list and fill the arrays
    for i in range(grid_x):
        for j in range(grid_y):
            if plasti[i][j][0]!=None:
            
                layer_trava[i, j] = plasti[i][j][0].energija
            if plasti[i][j][1]!=None:
                layer_ovce[i, j] = plasti[i][j][1].energija
            
            if plasti[i][j][2]!=None:
                layer_volk[i, j] = plasti[i][j][2].energija
    return [layer_trava,layer_ovce,layer_volk]
         


def narisi_graf(seznam,svet,STOP):
    xx,yt,yo,yv=seznam
    
    plt.figure(figsize=(9,9))
    plt.subplot(331)
    plt.plot(xx,yt,color="green")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)

    plt.subplot(332)
    plt.plot(xx,yo,color="orange")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)

    plt.subplot(333)
    plt.plot(xx,yv,color="grey")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)
    

    plt.subplot(334)
    plt.plot(yt,yo,color="green")
    plt.xlabel("Populacija trave")
    plt.ylabel("Populacija ovc")
    plt.scatter(yt[0],yo[0],label="Start")
    plt.scatter(yt[-1],yo[-1],label="End")
    plt.legend()

    plt.subplot(335)
    plt.plot(yo,yv,color="orange")
    plt.ylabel("Populacija volkov")
    plt.xlabel("Populacija ovc")
    plt.scatter(yo[0],yv[0],label="Start")
    plt.scatter(yo[-1],yv[-1],label="End")
    plt.legend()

    plt.subplot(336)
    plt.plot(yt,yv,color="grey")
    plt.ylabel("Populacija volkov")
    plt.xlabel("Populacija trave")
    plt.scatter(yt[0],yv[0],label="Start")
    plt.scatter(yt[-1],yv[-1],label="End")
    plt.legend()
    
    layer_trava,layer_ovce,layer_volk=convert_to_array(svet)
    plt.subplot(337)
    plt.imshow(layer_trava,vmin=0,vmax=1)
    
    plt.subplot(338)
    plt.imshow(layer_ovce,cmap="Greys",vmin=0,vmax=1)
    
    plt.subplot(339)
    plt.imshow(layer_volk,cmap="Greys",vmin=0,vmax=1)
    
    plt.tight_layout()
    plt.savefig("results.png")
    plt.show()