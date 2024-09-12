---

# Simple Bruteforcer

A simple Python-based password-cracking tool inspired by Hydra. Supports SSH, HTTP, and FTP brute-force attacks. 

## Features

- **Protocol Support**: SSH, HTTP, FTP
- **Multithreading**: Speed up the brute-force process
- **Logging**: Records all login attempts
- **Configurable**: Number of threads and login URL (for HTTP)

## Requirements

- Python 3.x
- `paramiko` for SSH brute-force
- `requests` for HTTP brute-force
- `ftplib` for FTP brute-force

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SaadSaid158/Basic-Bruteforcer.git
   cd Basic-Bruteforcer
   ```

2. **Install dependencies**:
   ```bash
   pip install paramiko requests
   ```

## Usage

### General Syntax

```bash
python3 main.py -t TARGET -p PROTOCOL -u USERLIST -w WORDLIST [-l LOGIN_URL] [-T THREADS]
```

### Arguments

- `-t, --target`: Target IP address or URL (required).
- `-p, --protocol`: Protocol to brute-force (`ssh`, `http`, `ftp`) (required).
- `-u, --userlist`: File with usernames (required).
- `-w, --wordlist`: File with passwords (required).
- `-l, --login-url`: Login URL for HTTP brute-force (required for HTTP).
- `-T, --threads`: Number of threads (default: 4).

### Examples

- **SSH Brute-Force**:
  ```bash
  python3 main.py -t 192.168.1.10 -p ssh -u users.txt -w passwords.txt
  ```

- **HTTP Brute-Force**:
  ```bash
  python3 main.py -t http://example.com -p http -u users.txt -w passwords.txt -l http://example.com/login
  ```

- **FTP Brute-Force**:
  ```bash
  python3 main.py -t 192.168.1.10 -p ftp -u users.txt -w passwords.txt
  ```

## Logging

All attempts are logged in files named according to the protocol:
- `ssh_attempts.log`
- `http_attempts.log`
- `ftp_attempts.log`

## Contributing

Feel free to submit issues or pull requests to improve the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Hydra, a very popular brute forcing tool in the industry.
- Uses `paramiko`, `requests`, and `ftplib` libraries

---
