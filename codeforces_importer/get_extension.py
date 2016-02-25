def get_extension(prog_lang):
    """Decides extension to be given to file based on programming_language"""

    return {
        'GNU C': 'c',
        'GNU C++11': 'cpp',
        'GNU C++': 'cpp',
        'Java 8': 'java',
        'Python 2': 'py'
    }.get(prog_lang, 'txt')
