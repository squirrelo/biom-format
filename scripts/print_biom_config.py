#!/usr/bin/env python

"""Print information on the biom-format installation.

For more details, see http://biom-format.org
"""
from sys import platform, version as python_version, executable
try:
    from cogent.util.option_parsing import parse_command_line_parameters, make_option
    from cogent import __version__ as pycogent_lib_version
    from cogent.util.misc import app_path
except ImportError:
    print "\n** ERROR: Cannot import PyCogent - this is a BIOM dependency.\n"
    exit()

__author__ = "Greg Caporaso"
__copyright__ = "Copyright 2012, The BIOM-Format Project"
__credits__ = ["Daniel McDonald", "Jose Clemente", "Greg Caporaso", 
               "Jai Rideout", "Justin Kuczynski", "Andreas Wilke",
               "Tobias Paczian", "Rob Knight", "Folker Meyer", 
               "Sue Huse"]
__url__ = "http://biom-format.org"
__license__ = "GPL"
__version__ = "0.9.3-dev"
__maintainer__ = "Daniel McDonald"
__email__ = "daniel.mcdonald@colorado.edu"

script_info = {}
script_info['brief_description'] = "Print information on the biom-format project installation."
script_info['script_description'] = "Print information on the biom-format project installation. This is useful for debugging install issues."
script_info['script_usage'] = [("","Print configuration information.","%prog")]
script_info['output_description']= ""
script_info['required_options'] = []
script_info['optional_options'] = []
script_info['version'] = __version__
script_info['help_on_no_arguments'] = False

try:
    from numpy import __version__ as numpy_lib_version
except ImportError:
    numpy_lib_version = "ERROR: Not installed - this is required!"
    
try:
    from biom import __version__ as biom_lib_version
    from biom.table import SparseObj
except ImportError:
    biom_lib_version = "ERROR: Can't find the BIOM library code - is it installed and in your $PYTHONPATH?"
    SparseObj = "ERROR: Can't find the BIOM library code - is it installed and in your $PYTHONPATH?"

def get_script_version():
    fp = app_path('convert_biom.py')
    if not fp:
        return "Can't find convert_biom.py - is the script directory in your $PATH?"
    for line in open(fp,'U'):
        if line.startswith('__version__'):
            return line.split('=')[1].strip().strip('"').strip("'")
    return "Something is wrong: can't find __version__ in %s" % fp
            

def print_biom_config():
    
    system_info = [
     ("Platform", platform),
     ("Python/GCC version",python_version.replace('\n', ' ')),
     ("Python executable",executable)]
    
    max_len =  max([len(e[0]) for e in system_info])
    print "\nSystem information"
    print  "==================" 
    for v in system_info:
        print "%*s:\t%s" % (max_len,v[0],v[1])

    version_info = [
     ("PyCogent version", pycogent_lib_version),
     ("NumPy version", numpy_lib_version),
     ("biom-format library version", biom_lib_version),
     ("biom-format script version", get_script_version()),]
    
    max_len =  max([len(e[0]) for e in version_info])

    print "\nDependency versions"
    print  "===================" 
    for v in version_info:
        print "%*s:\t%s" % (max_len,v[0],v[1])
    
    package_info = [
     ("SparseObj type", SparseObj)
    ]
    max_len =  max([len(e[0]) for e in package_info])
    
    print "\nbiom-format package information"
    print   "==============================="
    for v in package_info:
        print "%*s:\t%s" % (max_len,v[0],v[1])
    print ""

if __name__ == '__main__':
    
    option_parser, opts, args = parse_command_line_parameters(**script_info)
    
    print_biom_config()
    
