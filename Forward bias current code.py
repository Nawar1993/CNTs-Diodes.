import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from scipy.special import lambertw
#constants
e=1.6*10**(-19)
k=1.38*10**(-23)
h=6.63*10**(-34)
y0=0.2
Eg=0.62*1.6*10**(-19)
n=1.2
T=300
Vf=10**(6)
L=10**(-6)
Is=6.27 *10**-14
VT=k*T/e
R=100
#Forward bias current
V1=np.linspace(0,0.65)
I1=((n*k*T)/(e*R)) *lambertw(e*R*8*e*k*T*y0/(h)  *np.exp(-Eg/(2*k*T)) /(n*k*T) *(np.exp((e*V1)/(n*k*T))))*10**(6)

#Threshold voltage derivation
dIdV = np.gradient(I1, V1)
d2IdV2 = np.gradient(dIdV, V1)
Vth = V1[np.argmax(d2IdV2)]
print(f" {Vth:.4f} ")

#Plot of the forward bias current
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 10))
ax1.plot(V1, I1, 'g')  
ax1.set_xlabel("V(Volt)")
ax1.set_ylabel("I(μA)")
ax1.margins(x=0,y=0)


#Zener voltage derivation
Vr=np.linspace(0,300,100)
E=(Vr)/L
TkwB=np.exp(-np.pi/(4)   *Eg**(2)/(h*Vf*e*E))
I2=4*e**(2)/(h) *TkwB*(Vr-VT*np.log(4))*10**3
dIdV = np.gradient(I2, Vr)
d2IdV2 = np.gradient(dIdV, Vr)
Vth1 = Vr[np.argmax(d2IdV2)]
print(f" {Vth1:.4f} ")


#Zener current plot
V2=np.linspace(-Vth1,0)
I_T=Is*np.ones_like(V2)
E=(V2)/L
TkwB=np.exp(-np.pi/4 *Eg**(2)/(h*Vf*e*E))
Vth2=Vth1-6


Vz = np.array([-Vth1+6.3, -Vth1+5.3, -Vth1+4.3, -Vth1+3.3, -Vth1+2.3,-Vth1+1.5, -Vth1+1.1, -Vth1+0.7, -Vth1+0.3, -Vth1])


for i in range (len(V2)):
	if V2[i]==-Vth1:
	    Iz = np.array([0.00, -0.03, -0.08, -0.15, -0.30,-0.60, -1.10, -1.90, -3.20, -6.00])
	   
	    ax2.plot(Vz,Iz,'b')
	elif V2[i]>-Vth2:
	    I_T[i]=-Is 
	    ax2.plot(V2,I_T,'b',linewidth=3)
	elif V2[i]<-Vth2:
	    I_T[i]=np.nan
	    ax2.plot(V2,I_T)
	    
ax2.set_xlabel("V(Volt)")
ax2.set_ylabel("I(mA)")
ax2.margins(x=0,y=0)
ax2.set_xlim(-30,0)
ax2.spines['left'].set_position('zero')   
ax2.spines['bottom'].set_position('zero') 
ax2.spines['right'].set_color('none')     
ax2.spines['top'].set_color('none')
ax2.yaxis.set_label_position("right")
ax2.xaxis.set_label_position("top")
ax2.yaxis.tick_right()
ax2.xaxis.tick_top()
plt.show()

