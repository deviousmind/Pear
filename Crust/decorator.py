from Crust.colors import Colors


def warning(message):
    print(Colors.YELLOW + message + Colors.RESET)


def error(message):
    print(Colors.RED + message + Colors.RESET)


def success(message):
    print(Colors.GREEN + message + Colors.RESET)


def ok(message):
    print(Colors.BLUE + message + Colors.RESET)