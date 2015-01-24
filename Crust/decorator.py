from Crust.colors import Colors


def warn(message):
    return Colors.YELLOW + escape(message)


def error(message):
    return Colors.RED + escape(message)


def success(message):
    return Colors.GREEN + escape(message)


def result(message):
    return Colors.BLUE + escape(message)


def request(message):
    return Colors.MAGENTA + escape(message)


def hint(message):
    return Colors.GREY + escape(message)


def emphasis(message):
    return Colors.BOLD + escape(message)


def attention(message):
    return Colors.CYAN + escape(message)


def escape(message):
    return message + Colors.RESET