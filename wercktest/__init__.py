from .version import version

def build_salute(args):
    return 'Hello %s, this is version %s' % (args, version())

def main(args):
    print(build_salute(args))
