
---


# Simple Bruteforcer

A simple Python-based password-cracking tool inspired by Hydra. Supports SSH, HTTP, and FTP brute-force attacks. 

## Disclaimer

**_Use this tool responsibly. This tool is intended for educational purposes and legitimate security testing only._** Unauthorized use of this tool against systems you do not own or have explicit permission to test is illegal and unethical. The creator of this tool is not responsible for any misuse or legal consequences resulting from its use. Always obtain proper authorization before performing security testing. 

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

## Improvements to be Made

- [ ] Add support for additional protocols like IMAP, POP3, etc.
- [ ] Improve error handling and retry mechanisms for robustness.
- [ ] Develop a graphical user interface (GUI) for easier configuration and use.
- [ ] Implement rate limiting to handle targets with rate limits more gracefully.
- [ ] Integrate features for generating password lists dynamically based on patterns.
- [ ] Enhance logging with timestamps and more detailed failure reasons.
- [ ] Allow configuration via a file for easier setup of multiple parameters.
- [ ] Optimize threading and resource management for better performance.

## Project Status

- **Current State**: Alpha
- **In Development**: Basic functionality is working. Ongoing development to add new features and improve stability.
- **Planned Features**: See the "Improvements to be Made" section for upcoming features and enhancements.
- **Known Issues**: Limited support for some protocols and error handling may need improvement.

## Contributing

Feel free to submit issues or pull requests to improve the tool.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by Hydra, a _very_ popular brute forcing tool in the industry.
- Uses `paramiko`, `requests`, and `ftplib` libraries

---
