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
    from a10_saltstack import axapi_http
    from a10_saltstack import session
    HAS_A10 = True
except ImportError:
    HAS_A10 = False

REQUIRED_NOT_SET = (False, "One of ({}) must be set.")
REQUIRED_MUTEX = (False, "Only one of ({}) can be set.")
REQUIRED_VALID = (True, "")

__proxyenabled__ = ['t_proc']
__virtualname__ = 't_proc'

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
    return 't_proc'


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

    return rc,errors

def init(opts):
    valid = True

    run_errors = []
    proxyinfo = opts['proxy']
    valid, validation_errors = _validate(**opts)
    map(run_errors.append, validation_errors)

    if not valid:
        err_msg = "Validation failure\n".join(run_errors)

    http_cli = axapi_http.HttpClient(proxyinfo['host'], proxyinfo['port'], proxyinfo['protocol'])
    ax_session = session.Session(http_cli, proxyinfo['username'], proxyinfo['password'])


def get_session():
    return ax_session


def shutdown(opts):
    '''
    For this proxy shutdown is a no-op
    '''
    LOG.debug('a10 proxy shutdown() called...')
