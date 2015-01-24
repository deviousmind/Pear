class Colors:

    ESC = '\033['
    RESET = ESC + '0m'
    BOLD = ESC + '1m'
    GREY = ESC + '90m'
    RED = ESC + '91m'
    GREEN = ESC + '92m'
    YELLOW = ESC + '93m'
    BLUE = ESC + '94m'
    MAGENTA = ESC + '95m'
    CYAN = ESC + '96m'


if __name__ == "__main__":
    print(Colors.BOLD + 'TEST')
    print(Colors.GREY + 'TEST')
    print(Colors.RED + 'TEST')
    print(Colors.GREEN + 'TEST')
    print(Colors.YELLOW + 'TEST')
    print(Colors.BLUE + 'TEST')
    print(Colors.MAGENTA + 'TEST')
    print(Colors.CYAN + 'TEST')
    print(Colors.RESET + 'TEST')