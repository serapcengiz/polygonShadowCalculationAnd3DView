# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.colors import LightSource
from math import dist


def crdnt(fp):
    vertices_cube = []
    faces_cube = []
    vertices_plane = []
    face_plane = []
    with open(fp,'r') as f:
        v = 8
        f1 = 6
        for line in f:
            if line.startswith('v '):
                vertex = list(map(float, line.split()[1:]))
                vertex[1], vertex[2] = vertex[2], vertex[1]
                if v > 0:
                    vertices_cube.append(vertex)
                else:
                    vertex.remove(vertex[1])
                    vertices_plane.append(vertex)
                v -= 1 
            elif line.startswith('f '):
                face = line.strip().split()[1:]
                face = [int(index.split('/')[0]) -1 for index in face]
                if f1 > 0:
                    faces_cube.append(face)
                else:
                    face_plane.append(vertex)
                f1 -= 1
    return np.array(vertices_cube), np.array(faces_cube,dtype=int), np.array(vertices_plane), np.array(face_plane)



def plt3d(vertices_cube,faces_cube,vertices_plane,face_plane,light_loc = None):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    
    ax.elev = 90
    ax.azim = 270 
    
    xx, yy = np.meshgrid(range(-5,5), range(-5,5))
    z = np.zeros((10,10),dtype=float) 
    z -= 3
    # plot the plane
    ax.plot_surface(xx, yy, z,color='y', alpha=0.8)
    
    
    for face in faces_cube:
        x = vertices_cube[face][:,0]
        y = vertices_cube[face][:,1]
        z = vertices_cube[face][:,2]
        ax.add_collection3d(Poly3DCollection([list(zip(x,y,z))],color='b'))
    
    
    if light_loc is not None:
        ax.scatter(*light_loc, color='r',s= 10)
        
    #-----------------------------------------------------------
    
    lx, ly, lz = light_loc[0], light_loc[1], light_loc[2]
    cube_top_vertices = vertices_cube[vertices_cube[:,2]!=0]
    cube_bottom_vertices = vertices_cube[vertices_cube[:,2]==0]
    
    shadow_vertices = []
    
    for vertex in cube_top_vertices:
        sx = (vertex[0]*lz - lx*vertex[2]) / (lz - vertex[2]) 
        sy = (vertex[1]*lz - ly*vertex[2]) / (lz - vertex[2]) 
        sz = 0
        vertex_ = [sx, sy, sz]
        shadow_vertices.append(vertex_)
    
    shadow_vertices = shadow_vertices + cube_bottom_vertices
    for point in shadow_vertices:
        ax.scatter(*point,color='r',s=10)
    
    """       
    xp = vertices_plane[:, 0]
    yp = vertices_plane[:, 1]
    zp = np.zeros_like(xp)
    zp = zp.reshape((1,4))
    ax.plot_surface(xp,yp,zp,facecolors='g',alpha=0.5)
    
    
    ls = LightSource(azdeg = 315, altdeg = 45)
    cube = Poly3DCollection(faces_cube, linewidths=1,edgecolors = 'k', alpha = 0.6)
    shaded_cube = ls.shade_rgb(cube.get_facecolor().reshape(cube._vecs.shape[0],4),vertice_normals=cube._vecs,blend_mode='soft')
    cube.set_facecolor(shaded_cube)
    ax.add_collection3d(cube)
    """
    
    ax.set_xlim3d(-10,10)
    ax.set_ylim3d(-10,10)
    ax.set_zlim3d(-10,10)
    
    plt.show(block=False)
 
    
    """
def shadow(vertices_cube, light_loc):
    
    lx, ly, lz = light_loc[0], light_loc[1], light_loc[2]
    cube_top_vertices = vertices_cube[vertices_cube[:,2]!=0]
    cube_bottom_vertices = vertices_cube[vertices_cube[:,2]==0]
    
    shadow_vertices = []
    
    for vertex in cube_top_vertices:
        sx = (vertex[0]*lz - lx*vertex[2]) / (lz - vertex[2]) 
        sy = (vertex[1]*lz - ly*vertex[2]) / (lz - vertex[2]) 
        sz = 0
        vertex_ = [sx, sy, sz]
        shadow_vertices.append(vertex_)
    
    shadow_vertices = shadow_vertices + cube_bottom_vertices
    for point in shadow_vertices:
        ax.scatter(*point,color='r',s=5)
    """
    
ofp = "/home/antep/Desktop/staj/cube.obj"
vertices_cube, faces_cube, vertices_plane, face_plane = crdnt(ofp)
          
#faces_cube = [[0,1,2,3], [4,5,6,7], [0,4,5,1],[1,5,6,2],[2,6,7,3], [3,7,4,0]]

light_loc = np.array([0,4,4])
plt3d(vertices_cube, faces_cube, vertices_plane, face_plane, light_loc)    