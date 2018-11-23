import os
import os.path
import fnmatch
import logging
import ycm_core
import re

def Settings( **kwargs ):
    return { 'flags': [ 
     '-x', 
     'c++', 
     '-Wall', 
     '-Wextra',
     '-Werror',
     '-Wno-long-long'
     '-Wno-variadic-macros'
     '-fexceptions',
     '-ferror-limit=10000',
     '-DNDEBUG',
     '-std=c++11',
     '-xc++',
     '-I/usr/lib/',
     '-I/usr/include',
     '-I/usr/lib/llvm-6.0/include',
     '-I/usr/lib/llvm-6.0/lib/clang/6.0.0/include',
     '-I/usr/include/x86_64-linux-gnu/c++/7.3.0',
     '-I/usr/include/c++/7.3.0/backward',
     ], }
