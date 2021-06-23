# Port_Scanner

this is my first tool using python.

it is simple but the code can be a little complex for some people.

the udp option is not working (I don't know why and I won't fix it until i write another port scanner (you can use Nmap :) )).

how to use it :
- run the script using python3.
- put the target as the first argument
- use options (n, -, .) to choose the ports you want to scan (example: python3 port_scanner.py 192.168.1.1 n)

ports options :
- n (used to scan all ports from 1 tp 65535)
- "-" (used to scan range of ports example : python3 port_scanner.py 192.168.1.1 1-100)
- , (used to scan a specific list of ports example : python3 port_scanner.py 192.168.1.1 21,22,443,80)

examples :
- python3 port_scanner.py 127.0.0.1 n


any comment or suggestion to send on my Twitter is welcome.
