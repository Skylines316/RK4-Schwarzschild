# RK4-Schwarzschild
An numerical solution to space-like geodesics of the Schwarzschild Solution

Tenemos la siguiente ecuación

<img src="https://render.githubusercontent.com/render/math?math=u''%2Bu-3\dfrac{r_g}{2}u^2=\dfrac{1}{\lambda}">

Esta ecuación diferencial de segundo orden se puede expresar como dos ecuaciones de primer orden.

sea <img src="https://render.githubusercontent.com/render/math?math=u'(t)=y(t)"> entonces tenemos que 

<img src="https://render.githubusercontent.com/render/math?math=y'=\dfrac{1}{\lambda}-u%2B3\dfrac{r_g}{2}u^2">

entonces

<img src="https://render.githubusercontent.com/render/math?math=y_{n+1}=y_n+\dfrac{1}{6}\left(l_0+2l_1+2l_2+l_3\right)">

y

<img src="https://render.githubusercontent.com/render/math?math=u_{n+1}=u_n\frac{1}{6}\left(k_0+2k_1+2k_2+k_3\right)">


