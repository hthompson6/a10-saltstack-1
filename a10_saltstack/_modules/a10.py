# Import Python libraries
from __future__ import absolute_import, print_function, unicode_literals
import logging

__virtualname__ = 'a10'

__proxyenabled__ = ['a10']

try:
    from a10_saltstack import client
    HAS_A10 = True
except ImportError:
    HAS_A10 = False


def __virtual__():
    '''
    We need the Junos adapter libraries for this
    module to work.  We also need a proxymodule entry in __opts__
    in the opts dictionary
    '''
    if HAS_A10 and 'proxy' in __opts__:
        return __virtualname__
    else:
        return (False, 'The a10 module could not be loaded: '
                       'proxy could not be loaded.')


def client(host, port, protocol, username, password):
    return A10Client(__proxy__['a10.get_session'])
