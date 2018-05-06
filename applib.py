class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def print_header(size: int, name: str):
    """
    Print a header looking like this :
    ------
     NAME
    ------

    :param size: width of the header in characters
    :type size: int
    :param name: name displayed by the header
    :type name: str
    """
    templateBar = "{:-^" + str(size) + "s}"
    templateName = "{:^" + str(size) + "s}"
    print(bcolors.HEADER, flush=True)
    print(templateBar.format(""), flush=True)
    print(templateName.format(name.upper()), flush=True)
    print(templateBar.format(""), flush=True)
    print(bcolors.ENDC, flush=True)


def print_curinfo(text: str):
    """
    Print an info line of an ongoing action

    :param text: text displayed
    :type text: str
    """
    templateName = "... {:s} ..."
    print(templateName.format(text), flush=True)


def print_endinfo(text: str):
    """
    Print an info line of an action that finished

    :param text: text displayed
    :type text: str
    """
    templateName = "{:s}"
    print(bcolors.BOLD + templateName.format(text) + bcolors.ENDC, flush=True)


def print_warning(text: str):
    """
    Print a line containing a warning message

    :param text: text displayed
    :type text: str
    """
    templateName = "{:s}"
    print(bcolors.WARNING + templateName.format(text) + bcolors.ENDC,
          flush=True)


def print_result(text: str):
    """
    Print a line containing the result of an action

    :param text: text displayed
    :type text: str
    """
    templateName = "{}"
    print(bcolors.OKGREEN + templateName.format(text) + bcolors.ENDC,
          flush=True)


def input_(text: str):
    """
    Colorize the text taken in an input

    :param text: prompt for the input
    :type text: str
    """
    inputText = input(text + bcolors.OKBLUE)
    print(bcolors.ENDC, flush=True, end="")
    return inputText
