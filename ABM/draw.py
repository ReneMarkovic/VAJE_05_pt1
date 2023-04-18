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
    
    plt.figure(figsize=(15,10))
    plt.subplot(231)
    plt.plot(xx,yt,color="green")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)

    plt.subplot(232)
    plt.plot(xx,yo,color="orange")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)

    plt.subplot(233)
    plt.plot(xx,yv,color="grey")
    plt.xlabel("Iteracija")
    plt.xlim(0,STOP)
    
    
    layer_trava,layer_ovce,layer_volk=convert_to_array(svet)
    print(layer_trava)
    plt.subplot(234)
    plt.imshow(layer_trava,vmin=0,vmax=1)
    plt.colorbar()
    
    plt.subplot(235)
    plt.imshow(layer_trava,cmap="Greys",vmin=0,vmax=1)
    plt.colorbar()
    
    plt.subplot(236)
    plt.imshow(layer_trava,cmap="Greys",vmin=0,vmax=1)
    plt.colorbar()
    
    plt.tight_layout()
    plt.show()