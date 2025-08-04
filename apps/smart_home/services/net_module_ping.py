import subprocess
import sys
import socket
import time

def test_connectivity(ip):
    try:
        # Проверка корректности IP-адреса
        socket.inet_aton(ip)
    except socket.error:
       
        return None

    try:
        start_time = time.time()
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            capture_output=True,
            text=True,
            check=False
        )
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if result.returncode == 0:
            
            return 1
        else:
            
            return 0
        
    except Exception as e:
       
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
       
        sys.exit(1)
    
    ip = sys.argv[1]
    result = test_connectivity(ip)
    if result is not None:
        print(result)