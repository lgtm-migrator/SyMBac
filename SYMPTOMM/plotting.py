import numpy as np
import matplotlib.pyplot as plt

def plot_scene(a, cells, savedir):
    if a%1 == 0:
        for cell in cells:
            vertices = cell.get_vertex_list()
            vertices = np.array(vertices)
            plt.plot(vertices[:,0], vertices[:,1])
            centroid = cell.position
            plt.scatter(centroid[0],centroid[1],s=100)
        plt.ylim(0,720)
        plt.xlim(0,720)
        plt.savefig(savedir+"/image_{}.png".format(str(a).zfill(3)))
        plt.clf()