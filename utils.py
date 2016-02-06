import sys
try:
    import StringIO
    import cStringIO
except ImportError:
    from io import BytesIO

running_python_3 = sys.version[0] == 3


def range_fn(*args):
    if running_python_3:
        return range(*args)
    else:
        return xrange(*args)


def is_string_io(instance):
    if running_python_3:
        return isinstance(instance, BytesIO)
    else:
        return (isinstance, (StringIO.StringIO,
                             cStringIO.InputType,
                             cStringIO.OutputType))
