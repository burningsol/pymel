"""
The ctx module contains all context commands.
"""

import factories

_thisModule = __import__(__name__, globals(), locals(), ['']) # last input must included for sub-modules to be imported correctly
for funcName, data in factories.cmdlist.items():
	if data['type'] == 'ctx':
		func = factories.functionFactory( funcName, None )
		if func:
			func.__module__ = __name__
			setattr( _thisModule, funcName, func )
		else:
			print "could not create ctx function", funcName