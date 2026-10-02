# Keylogger Lab

A simple Python project created for learning how keylogging concepts, system information collection, file integrity checking, and logging work.

This project is intentionally limited to recording text entered directly into the program. It does **not** capture system-wide keyboard input.

## Features

- Displays basic operating system information
- Detects the current username
- Shows the current working directory
- Retrieves the local/private IP address
- Calculates the SHA-256 hash of the Python script
- Saves collected system information to `system_info.txt`
- Records user input with timestamps
- Saves captured input to `keylog.txt`

## Project Structure

```text
Keylogger/
├── keylogger.py
├── keylog.txt
├── system_info.txt
└── README.md
```

### `keylogger.py`

Main Python script containing the system information, integrity checking, and input logging functionality.

### `system_info.txt`

Generated when the program runs. Contains information such as:

- Operating system
- OS version and release
- Machine architecture
- Private IP address
- Username
- Current working directory
- SHA-256 hash of `keylogger.py`

### `keylog.txt`

Stores text entered into the program together with a timestamp.

Example:

```text
2026-10-02 10:30:15 | Hello World
```

## Requirements

- Python 3
- No external Python libraries are required

The project uses only Python standard library modules:

```python
os
platform
socket
pathlib
hashlib
datetime
```

## Usage

Clone the repository:

```bash
git clone https://github.com/elcnqlyv/Keylogger.git
cd Keylogger
```

Run the program:

```bash
python keylogger.py
```

or:

```bash
python3 keylogger.py
```

The program will first display system information and save it to:

```text
system_info.txt
```

After that, the input logging lab will start:

```text
Starting terminal keylogger lab...
Type something below.
Type EXIT to stop.

> Hello
Captured: Hello
```

The entered text is appended to:

```text
keylog.txt
```

To stop the program, enter:

```text
EXIT
```

## File Integrity Check

The program calculates the SHA-256 hash of its own source file:

```text
File: keylogger.py
SHA256: <hash>
```

SHA-256 hashes can be used to detect whether a file has changed between executions.

## Purpose

This project was created as a cybersecurity learning exercise to understand:

- basic keylogger concepts
- input logging
- timestamped log files
- system information collection
- local network information
- file hashing
- basic file integrity monitoring
- Python file handling

The implementation deliberately avoids global keyboard hooks and records only input explicitly entered into the running program.

## Disclaimer

This project is intended for educational and laboratory use only.

Do not use keylogging or monitoring software on systems or users without explicit authorization.