# >>>>>>>>>>>> GIVE CREDIT <<<<<<<<<<<<<<<<<<
# >>>>>>>>>>>> DAMMI CREDITI <<<<<<<<<<<<<<<<<
import requests

server = "mc.feargames.it" #modify only this
API = "http://api.godalecs.it/api/?server=" #don't modify
req = requests.get(API + server).json() #don't modify
# don't modify <<<<<<<<<
address = req['address']
status = req['status']
port = req['port']
hostname = req['hostname']
player_online = req['player_online']
player_max = req['player_max']
ping = req['ping']
motd = req['motd']
version = req['version']
protocol = req['protocol']
players = req['players']
# don't modify <<<<<<<<
print('IP primario:')
print(address)
print('                   ')
print('Online o Offline?')
print(status)
print('                   ')
print('Porta')
print(port)
print('                   ')
print('IP Secondario')
print(hostname)
print('                   ')
print('Giocatori massimi')
print(player_max)
print('                   ')
print('Giocatori online')
print(player_online)
print('                   ')
print('Ping-Pong')
print(ping)
print('                   ')
print('MoTD')
print(motd)
print('                   ')
print('Versione')
print(version)
print('                   ')
print('Protocol')
print(protocol)
print('                   ')
print('Lista giocatori Online')
print(players)
print('                   ')
print('                   ')
print('                   ')
print('Creato da @JoyIIA')
print('Con aiuto delle API (non le 🐝)')
print('Cambia IP del server su: SERVER = "mc.nameserver.org"')
print('>>> RIGA 3 <<<')
