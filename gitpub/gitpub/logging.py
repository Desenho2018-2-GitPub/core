from django.core.files import File
import os, time

class GitPubDebugger(object):
    _instance = None
    _logfile = None

    _colors = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    _debugmode = os.getenv('GITPUB_DEBUGGER_ON', True)
    _writetofile = os.getenv('GITPUB_DEBUGGER_LOGFILE', True)

    def __new__(cls, *kwargs):
        if GitPubDebugger._instance is None:
            GitPubDebugger._instance = object.__new__(cls)
            print(GitPubDebugger._colors['BOLD'] + '===================================' + GitPubDebugger._colors['ENDC'])
            print(GitPubDebugger._colors['BOLD'] + '=== GitPub debugger initialized ===' + GitPubDebugger._colors['ENDC'])
            print(GitPubDebugger._colors['BOLD'] + '===================================' + GitPubDebugger._colors['ENDC'])

        if GitPubDebugger._logfile is None:
            filename = "gitpub_debugger.txt"
            GitPubDebugger._logfile = File(open(filename, 'w'))
            timestamp =  '[' + time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()) + '] - '
            GitPubDebugger._logfile.write(timestamp + 'DEBUGGER INITIALIZED\n\n')
        return GitPubDebugger._instance

    def get_timestamp(self):
        return '[' + time.strftime('%d-%m-%Y %H:%M:%S', time.localtime()) + '] - '

    def color_timestamp(self):
        return GitPubDebugger._colors['BOLD'] + self.get_timestamp() + GitPubDebugger._colors['ENDC']

    def debug_colored(self, msg):
        return GitPubDebugger._colors['OKGREEN'] + msg + GitPubDebugger._colors['ENDC']

    def error_colored(self, msg):
        return GitPubDebugger._colors['FAIL'] + msg + GitPubDebugger._colors['ENDC']

    def debug(self, msg):
        if GitPubDebugger._debugmode:
            print(self.color_timestamp() + self.debug_colored(msg))
            if GitPubDebugger._writetofile:
                GitPubDebugger._logfile.write("[DEBUG] " + self.get_timestamp() + msg + "\n")

    def error(self, msg):
        if GitPubDebugger._debugmode:
            print(self.color_timestamp() + self.error_colored(msg))
            if GitPubDebugger._writetofile:
                GitPubDebugger._logfile.write("[ERROR] " + self.get_timestamp() + msg + "\n")


def debug(func):
    def decorated(*args, **kwargs):
        debug_instance = GitPubDebugger()
        result = func(*args, **kwargs)
        debug_instance.debug("{}({}) = {}".format(
            func.__name__,
            ', '.join(each.__repr__() for each in args),
            result
            ))
        return result
    return decorated