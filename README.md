# Anti-keylogger

Anti-keylogger is a program that can detect any running keyloggers and stop the process

## Implementation

- Python is used to code the program
- Unlike using signatures, we check all the running processes(APIs) and check if any of them has a keylogger running
- The program then stops the keylogger process if found and the user can be sure that they are not tracked by anyone