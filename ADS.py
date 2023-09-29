import subprocess
from time import sleep


alg = ['reno', 'cubic']
BER = ['100000', '1000000']
e2e_delay = ['10000', '100000']
repeticao = 8

id_exp = 'i1234'
tempo_execucao = '200'
tempo_execucao_server = '50'

ip_pc1 = '10.0.0.20'
ip_pc2 = '10.0.3.20'
ip_pc3 = '10.0.1.20'
ip_pc4 = '10.0.4.20'


bandas = ['500000kbps', '700000kbps']

##### execucao dos experimentos
#para cada uma das repeticoes faca
for rep in range(repeticao):
    for proto in alg:
        for ber in BER:
            for banda_udp in bandas:
                for e2e in e2e_delay:
                
                
                    inicializacao = ['sudo', 'imunes', '-b', '-e', id_exp, 'ADS.imn']


                    # Fluxo background (UDP)
                    init_iperf_servidor_back = ['sudo', 'himage', 'pc3@'+id_exp, 'iperf', '-s', '-u']
                    init_iperf_cliente_back = ['sudo', 'himage', 'pc4@'+id_exp, 'iperf', '-c', ip_pc3, '-u', '-t', tempo_execucao_server, '-b', banda_udp]
                    # Fluxo background (UDP)                

                    # Fluxo principal (TCP)
                    init_iperf_servidor = ['sudo', 'himage', 'pc1@'+id_exp, 'iperf', '-s']
                    init_iperf_cliente = f'sudo himage pc2@{id_exp} iperf -c {ip_pc1} -t {tempo_execucao} -e -Z {proto} -y C >> cliente.csv'
                    echo = f'sudo echo -n {rep},{proto},{ber},{e2e},{banda_udp}, >> cliente.csv'

                    vlink = ['sudo', 'vlink', '-BER', ber,'-dly', e2e, 'router1:router2@'+id_exp]
                    # Fluxo principal (TCP)

                    subprocess.Popen(inicializacao).wait()
                    
                    subprocess.Popen(echo,shell=True,stdout=subprocess.PIPE, text=True).wait()
                    
                    subprocess.Popen(vlink).wait()

                    subprocess.Popen(init_iperf_servidor_back)

                    subprocess.Popen(init_iperf_servidor)
                    
                    subprocess.Popen(init_iperf_cliente_back)

                    subprocess.Popen(init_iperf_cliente,shell=True,stdout=subprocess.PIPE, text=True).wait()

                    subprocess.Popen(['cleanupAll']).wait()
