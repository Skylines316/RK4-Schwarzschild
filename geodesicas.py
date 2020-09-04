import numpy as np
import matplotlib.pyplot as plt
import math as ma

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

end=26*ma.pi			#es el intervalo de 0 a
s=100000		#es el numero de puntos
h=end/s
theta=np.linspace(0,end,s)

#variables de geodesicas
lam=18
r_g=1

y_n=0      #velocidad inversa inicial
u_n=2/lam    #radio inverso inicial




r=[]


#punto de referencia
for i in range(s):
    r_el=1/u_n
    r.append(r_el)
    
    k_0=h*y_n
    l_0=h*(1/lam-u_n+1.5*r_g*u_n**2)
    
    k_1=h*(y_n+l_0/2)
    l_1=h*(1/lam-u_n-k_0/2+1.5*r_g*(u_n+k_0/2)**2)
    
    k_2=h*(y_n+l_1/2)
    l_2=h*(1/lam-u_n-k_1/2+1.5*r_g*(u_n+k_1/2)**2)
    
    k_3=h*(y_n+l_2/2)
    l_3=h*(1/lam-u_n-k_2+1.5*r_g*(u_n+k_2)**2)
    
    y_n1=y_n+(l_0+2*l_1+2*l_2+l_3)/6
    u_n1=u_n+(k_0+2*k_1+2*k_2+k_3)/6

    y_n=y_n1
    u_n=u_n1

    #print(u_n,r_el)
    
#print(r)
#print('separacion')
#print(r)
ax.plot(theta, r)
#ax.set_rmax(2)
#ax.set_rticks([0.5, 1, 1.5, 2])  # Less radial ticks
#ax.set_rlabel_position(-22.5)  # Move radial labels away from plotted line
ax.grid(True)

ax.set_title("Desviación de Einstein", va='bottom')
plt.show()



