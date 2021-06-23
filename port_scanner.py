rom sys import argv
import socket

s = socket.socket()

target = argv[1]

if "-" in argv[2] :
    l = argv[2].split("-")
    port = range(int(l[0]), int(l[1]))
    
elif "," in argv[2] :
    port = list(map(int, argv[2].split(",")))

elif "n" in argv[2].lower() :
    port = range(0, 65535)
    
elif argv[3].lower() == "ubp" :
    print("Targeting", target, "on UDP ports")
    
    for i in port :
    	
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDPLITE)
    	
        b = s.connect_ex((target, i))
    	
        if b == 0 :
        
            try :
        
                print(f"port {port} is open. {socket.getservbyport(port)}")
        
            except OSError :
        
                print(f"port {port} is open. unknown service")
        s.close()

else :
    port = int(argv[2])

print("Targeting", target, "on", port)

if type(port) == range or type(port) == list:
    for i in port :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b = s.connect_ex((target, i))
        if b == 0 :
            try :
                print(f"port {i} is open. {socket.getservbyport(i)}")
            except OSError :
                print(f"port {i} is open. unknown service")
        s.close()

elif type(port) == int :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        b = s.connect_ex((target, port))
        if b == 0 :
            try :
                print(f"port {port} is open. {socket.getservbyport(port)}")
            except OSError :
                print(f"port {port} is open. unknown service")
        s.close()
