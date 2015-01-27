class Colors:

    ESC = ''
    RESET = ''
    BOLD = ''
    GREY = ''
    RED = ''
    GREEN = ''
    YELLOW = ''
    BLUE = ''
    MAGENTA = ''
    CYAN = ''

    @staticmethod
    def colorify():
        esc = '\033['
        Colors.RESET = esc + '0m'
        Colors.BOLD = esc + '1m'
        Colors.GREY = esc + '90m'
        Colors.RED = esc + '91m'
        Colors.GREEN = esc + '92m'
        Colors.YELLOW = esc + '93m'
        Colors.BLUE = esc + '94m'
        Colors.MAGENTA = esc + '95m'
        Colors.CYAN = esc + '96m'


if __name__ == "__main__":
    Colors.colorify()
    print(Colors.BOLD + 'TEST')
    print(Colors.GREY + 'TEST')
    print(Colors.RED + 'TEST')
    print(Colors.GREEN + 'TEST')
    print(Colors.YELLOW + 'TEST')
    print(Colors.BLUE + 'TEST')
    print(Colors.MAGENTA + 'TEST')
    print(Colors.CYAN + 'TEST')
    print(Colors.RESET + 'TEST')