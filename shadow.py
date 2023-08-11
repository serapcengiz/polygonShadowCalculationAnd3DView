#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 10:37:22 2023

@author: antep
"""
#%
import math
import matplotlib.pyplot as plt
import numpy as np

#%%
def shadow(cube_coord, sun_azimuth, sun_altitude, epsilon, cube_height):
        
    alpha = math.pi * sun_altitude / 180
    
    shadow_coord = []
    dx = cube_height * (1/math.tan(alpha)) * math.sin(sun_azimuth)
    dy = - cube_height * math.cos(sun_azimuth) * (1/math.tan(alpha))
    d = np.array(dx,dy)
    
    for vertex in cube_coord:
        vertex = np.array(vertex)        
        shadow_coord.append(vertex + d)        
    
    return shadow_coord





#%%
def plt3d(vertices_cube, sun_azimuth, sun_altitude, epsilon, height):
    fig = plt.figure()
    ax = fig.add_subplot(111,projection='3d')
    

    
    shadow_vertices = [] 
    
    alpha = math.pi * sun_altitude / 180 
    
    for vertex in vertices_cube:
        sx = math.sin(epsilon)*math.cot(alpha)*height
        sy = -math.cos(epsilon)*math.cot(alpha)*height 
        sz = 0
        vertex_ = [sx, sy, sz]
        shadow_vertices.append(vertex_)
    
    shadow_vertices = shadow_vertices 
    
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
 
    