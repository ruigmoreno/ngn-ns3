import os
import numpy as np
import matplotlib.pyplot as plt

os.chdir('./scriptResults-all-do-rf-001/')
cwd = os.getcwd()
phy = '80211a'
nb_nodes='81'
packetInterval = '0.01'
listParameter=['PreqTotal', 'PrepTotal', 'PerrTotal']
listModes=['R','RP']
listFlags=['d0-r0', 'd0-r1', 'd1-r0', 'd1-r1']
packetSize='1024'
listFlows=['1','10','30','50','70']
# title = 'Modes with packet interval of '+packetInterval+' s'
#title = 'Modos com intervalo de pacote de '+packetInterval+' s'
# for parameter in listParameter:

plt.axis([0, 71, 0, 30000])
# plt.ylabel('Number of '+parameter+' Messages ')
#strParameter = ', '.join([str(item) for item in listParameter])
#plt.ylabel('Soma das Mensagens '+strParameter+' ')
plt.ylabel('Soma de mensagens de controle iniciadas')

for mode in listModes:
    if mode == 'R':
        color='black'
    elif mode == 'RP':
        color='red'
    for flag in listFlags:
        x_axis = np.array([])
        sumy = np.array([])
        #sumerror = np.array([])
        for nb_flows in listFlows:
            x = np.array([])
            y = np.array([])
	        #error = np.array([])
            for parameter in listParameter:
                load_y = np.loadtxt('./'+mode+'/'+flag+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=1)
                y = np.append(y, load_y)

                load_x = np.loadtxt('./'+mode+'/'+flag+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=0)
                x = np.append(x, load_x)
                
                #load_error=np.loadtxt('./'+mode+'/nb_nodes-'+nb_nodes+'-packetInterval-'+packetInterval+'-'+phy+'-'+nb_flows+'-flows/'+parameter+'-packetSize-'+packetSize, usecols=2)
                    #error = np.append(error, load_error)
            # print(y)
            sumy = np.append(sumy, np.sum(y))
            # print(sumy)
            x = x[0]
            x_axis = np.append(x_axis, x)
            # print('----------')
        if flag == 'd0-r0':
            markerStyle='.'
        elif flag == 'd0-r1':
            markerStyle='s'
        elif flag == 'd1-r0':
            markerStyle='x'
        elif flag == 'd1-r1':
            markerStyle='*'
        # plt.xlabel('flows number')
        plt.xlabel('Número de fluxos')
        plt.errorbar(x_axis, sumy, marker=markerStyle, color=color, label=mode+' '+flag+' '+packetSize+' bytes', capsize=6)
        plt.legend(bbox_to_anchor=(0.1, -.36, .8, .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0)
        plt.grid(True)
#plt.suptitle(title, y=0.925)
# plt.savefig('./plot-'+parameter+'-route-msgs-per-node.pdf', bbox_inches="tight")
plt.savefig('./plot-sum-total-route-msgs-PT.pdf', bbox_inches="tight")
plt.clf() # clear the entire current figure with all its axes
