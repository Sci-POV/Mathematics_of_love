# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import numpy as np



a = -1 #
b= +1 #
c = +1#
d = -1#




nR, nJ = (20, 20)

R = np.linspace(-5, 5, nR)

J = np.linspace(-5, 5, nJ)

RR, JJ = np.meshgrid(R, J)

Rdot = a*RR + b*JJ

Jdot = c*RR + d*JJ

        

fig, ax = plt.subplots(1,1,figsize=(20,20))


ax.quiver(RR,JJ,Rdot,Jdot)

ax.set(xlim=(-5, 5), ylim=(-5, 5))
ax.set_aspect(aspect=1)      

ax.set_title("Love Space",fontsize=25)

ax.set_ylabel('Juliet',fontsize=25)
ax.set_xlabel(' Romeo',fontsize=25)

