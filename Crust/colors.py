class Colors:

    ESC = '\033['
    RESET = ESC + '0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    GREY = ESC + '90m'
    RED = ESC + '91m'
    GREEN = ESC + '92m'
    YELLOW = ESC + '93m'
    BLUE = ESC + '94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'


if __name__ == "__main__":
    print(Colors.GREY + 'TEST')
    print(Colors.RED + 'TEST')
    print(Colors.GREEN + 'TEST')
    print(Colors.YELLOW + 'TEST')
    print(Colors.BLUE + 'TEST')
    print(Colors.MAGENTA + 'TEST')
    print(Colors.CYAN + 'TEST')
    print(Colors.RESET + 'TEST')