#!/home/homero/miniconda3/bin/python
import matplotlib.pyplot as plt
import numpy as np

#beta = 1.00001

# # parameters used by Vasques & Castro (UECE)
# beta_quarantine = 2.7
# gamma = .03
# n_days = 35
# release_quarantine = 12*7

# # my parameters 2 peaks
# beta_quarantine = .24
# beta_no_quarantine = 1.
# gamma = .14
# n_days = 500
# release_quarantine = 12*7

# my parameters 2 peaks faster
beta_quarantine = .8
beta_no_quarantine = 1.2
gamma = .7
n_days = 35*7
release_quarantine = 12*7


dt=.1 # in days
beta = beta_quarantine
t=0
n = 9000000.  # Ceara population
s = n
i = 7606.  # initially infected by beginning of May
r = 0.
n_steps = int(n_days/dt)

s_all=np.zeros(n_steps)
i_all=np.zeros(n_steps)
r_all=np.zeros(n_steps)
s_all[0]=s
i_all[0]=i
r_all[0]=r

for x in range(n_steps):
    ds = -beta*s*i/n*dt
    dr = gamma*i*dt
    di = -ds-dr

    t+=dt
    s+=ds
    i+=di
    r+=dr

    s_all[x]=s
    i_all[x]=i
    r_all[x]=r

    if 0<=x*dt-release_quarantine<=dt:
        print('hey')
        beta=beta_no_quarantine
    
plt.figure()
plt.subplot(2,1,1)
plt.title("Evolucao epidemiologica\n parametros: beta=%f, gamma=%.3f" % (beta_quarantine, gamma))
plt.plot(np.arange(len(s_all))*dt/7+1, s_all/n*100, '-', label='suscetivel')
plt.plot(np.arange(len(s_all))*dt/7+1, r_all/n*100, '-', label='recuperado')
plt.plot(np.arange(len(s_all))*dt/7+1, i_all/n*100, '-', label='infectado')
if n_days>=release_quarantine:
    plt.axvline(release_quarantine/7+1) 
plt.ylabel('% populacao')
plt.xlabel('Semanas')
plt.legend()
plt.subplot(2,1,2)
plt.plot(np.arange(len(s_all))*dt/7+1, i_all, '-', label='infectado', color='green')
if n_days>=release_quarantine:
    plt.axvline(release_quarantine/7+1) 
plt.ylabel('# infectados')
plt.xlabel('Semanas')
plt.legend()
plt.tight_layout()

# plt.figure()
# plt.title("beta=%f, gamma=%.3f" % (beta, gamma))
# plt.plot(i_all/n, '-', label='infectado')
# plt.ylabel('Percentual da populacao (%)')
# plt.xlabel('Dias')
# plt.legend()

plt.show()
