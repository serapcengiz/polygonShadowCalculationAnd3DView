# Staj Project

## The aim of the project is to draw the shadow of the given polygon according to the positon of the sun.
1) It draws a ceratin polygon with points on the plot created with matplotlib and turns this polygon into a 3-dimensional object with the object height requested by the user.
![1aciklama](1acıklama.png) ![1aciklamaresim](1resim.png)
2) 2)An interface is created via tkinter library.Then 2 scales are used in this interface.Scaller is there for the user to set the sun_Azimuth and sun_elevation values. With these values received from the user,sun_positon is determined.
![2aciklama](2acıklama.png) ![1aciklamaresim](2resim.png)
3) It also draws  the plot created with matplotlib to the interface. It draws and updates the shadow on the plot with the update_plot() function in the code according to the values received from the scaler.
![3aciklama](3acıklama.png) 
https://github.com/serapcengiz/stajProject/assets/73667009/463c2679-c1f9-481a-89a2-2024c9009390 



### Requests Library
`import math`  
`import matplotlib.pyplot as plt`  
`import numpy as np`  
`from mpl_toolkits.mplot3d.art3d import Poly3DCollection`  
`import tkinter as tk`  
`from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg`  
`from mpl_toolkits.mplot3d.art3d import Line3DCollection`

