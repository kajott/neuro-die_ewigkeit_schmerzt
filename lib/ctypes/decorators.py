"""
This module implements decorators for native api function calls.

name_library(name, so_name)
cdecl(restype, dllname, argtypes)
stdcall(restype, dllname, argtypes) - windows only
"""

LOGGING = False

import os
import ctypes

_library_map = {} # map short name to so-name
_loaded_libs = {} # map so-names to DLL instance


def name_library(name, so_name):
    """
    name_library(name, so_name)

    Register the <so_name> for a library.  The library will be loaded
    if <name> is referenced in a decorator.
    """
    _library_map[name] = so_name
    _library_map[so_name] = so_name


def _get_library(name):    
    # load and return a library.  The library is cached.
    soname = _library_map.get(name, name)
    try:
        return _loaded_libs[soname]
    except KeyError:
        return _loaded_libs.setdefault(soname, ctypes.CDLL(soname))

def cdecl(restype, dllname, argtypes, logging=False):
    """cdecl(restype, dllname, argtypes, logging=False) -> decorator.

    The decorator, when applied to a function, attaches an '_api_'
    attribute to the function.  Calling this attribute calls the
    function exported from the dll, using the standard C calling
    convention.
   
    restype - result type
    dll - name or instance of a dll/shared library
    argtypes - list of argument types
    logging - if this is True, the result of each function call
        is printed to stderr.
    """
    def decorate(func):
        library = _get_library(dllname)
        api = ctypes.CFUNCTYPE(restype, *argtypes)(func.func_name, library)
        func._api_ = api
        # The following few lines trigger a pychecker bug, see
        # https://sourceforge.net/tracker/index.php?func=detail&aid=1114902&group_id=24686&atid=382217
        if logging or LOGGING:
            def f(*args):
                result = func(*args)
                print >> sys.stderr, "# function call: %s%s -> %s" % (func.func_name, args, result)
                return result
            return f
        return func
    return decorate

if os.name == "nt":
    def stdcall(restype, dllname, argtypes, logging=False):
        """stdcall(restype, dllname, argtypes, logging=False) -> decorator.

        The decorator, when applied to a function, attaches an '_api_'
        attribute to the function.  Calling this attribute calls the
        function exported from the dll, using the MS '__stdcall' calling
        convention.

        restype - result type
        dll - name or instance of a dll
        argtypes - list of argument types
        logging - if this is True, the result of each function call
            is printed to stderr.
        """
        def decorate(func):
            library = _get_library(dllname)
            api = ctypes.WINFUNCTYPE(restype, *argtypes)(func.func_name, library)
            func._api_ = api
            # The following few lines trigger a pychecker bug, see
            # https://sourceforge.net/tracker/index.php?func=detail&aid=1114902&group_id=24686&atid=382217
            if logging or LOGGING:
                def f(*args):
                    result = func(*args)
                    print >> sys.stderr, "# function call: %s%s -> %s" % (func.func_name, args, result)
                    return result
                return f
            return func
        return decorate

################################################################

def _test():
    import os, sys
    from ctypes import c_char, c_int, c_ulong, c_double, \
         POINTER, create_string_buffer, sizeof

    if os.name == "nt":
        from ctypes import WinError

        #@ stdcall(ctypes.c_ulong, "kernel32", [c_ulong, POINTER(c_char), c_ulong])
        def GetModuleFileNameA(handle=0):
            buf = create_string_buffer(256)
            if 0 == GetModuleFileNameA._api_(handle, buf, sizeof(buf)):
                raise WinError()
            return buf.value
        GetModuleFileNameA = stdcall(ctypes.c_ulong, "kernel32",
                                     [c_ulong, POINTER(c_char), c_ulong])(GetModuleFileNameA)

        assert(sys.executable == GetModuleFileNameA())

    if os.name == "nt":
        name_library("libm", "msvcrt")
    else:
        name_library("libm", "libm")

    #@ cdecl(c_double, 'libm', [c_double])
    def sqrt(value):
        return sqrt._api_(value)
    sqrt = cdecl(c_double, 'libm', [c_double])(sqrt)

    assert sqrt(4.0) == 2.0

if __name__ == "__main__":
    _test()
