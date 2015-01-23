from Crust.colors import Colors


def warning(message):
    print(Colors.WARNING + message + Colors.ENDC)


def error(message):
    print(Colors.FAIL + message + Colors.ENDC)


def success(message):
    print(Colors.OKGREEN + message + Colors.ENDC)


def ok(message):
    print(Colors.OKBLUE + message + Colors.ENDC)