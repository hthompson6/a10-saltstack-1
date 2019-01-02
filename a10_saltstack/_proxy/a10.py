'''
Connect to an a10 device using the a10 proxy by specifying the host information in the
pillar found at '/srv/pillar/a10/a10_proxy.sls'
.. code-block:: yaml
    proxy:
      proxytype: a10
      host: <ip or dns name of host>
      username: <username>
      port: <port number>
      protocol: <https, https, tcp, etc.>
      password: <supersecret>
In '/srv/pillar/a10/top.sls' map the device details with the proxy name.
.. code-block:: yaml
    base:
      'ax':
        - a10_proxy 
After storing the device information in the pillar, configure the proxy \
in '/etc/salt/proxy'
.. code-block:: yaml
    master: <ip or hostname of salt-master>
Run the salt proxy via the following command:
.. code-block:: bash
    salt-proxy --proxyid=ax
'''
from __future__ import absolute_import

import logging

try:
    import a10_saltstack 
    HAS_A10 = True
except ImportError:
    HAS_A10 = False

__proxyenabled__ = ['a10']
__virtualname__ = 'a10'

GRAINS_CACHE = {}
DETAILS = {}

LOG = logging.getLogger(__file__)

ax_session = None


def __virtual__():
    '''
    Only return if all the modules are available
    '''
    if not HAS_A10:
        return False, 'Missing dependency: The a10 proxy minion requires the acos-client Python module.'

    return __virtualname__ 


def proxytype():
    '''
    Returns the name of this proxy
    '''
    return 'a10'


def _validate(**params):
    # Ensure that params contains all the keys.
    requires_one_of = sorted([])
    present_keys = sorted([x for x in requires_one_of if params.get(x)])

    errors = []
    marg = []

    if not len(requires_one_of):
        return REQUIRED_VALID

    if len(present_keys) == 0:
        rc,msg = REQUIRED_NOT_SET
        marg = requires_one_of
    elif requires_one_of == present_keys:
        rc,msg = REQUIRED_MUTEX
        marg = present_keys
    else:
        rc,msg = REQUIRED_VALID

    if not rc:
        errors.append(msg.format(", ".join(marg)))


def init(opts):
    valid = True

    valid, validation_errors = _validate(**opts)
    map(run_errors.append, validation_errors)

    if not valid:
        err_msg = "Validation failure\n".join(run_errors)

    http_cli = axapi_http.HttpClient(opts['host'], opts['port'], opts['protocol'])
    ax_session = session.Session(http_cli, opts['username'], opts['password'])


def get_session():
    return ax_session


def shutdown(opts):
    '''
    For this proxy shutdown is a no-op
    '''
    LOG.debug('a10 proxy shutdown() called...')
