# a10_saltstack
Repository for saltstack modules

This code is now being generated using the SDK generator at https://github.com/a10networks/sdkgenerator

## Summary
a10-salstack is a set of Saltstack modules and example playbooks for interacting with AXAPI v3 for configuration and monitoring of A10 ACOS-based hardware and virtual appliances. The module code and example playbooks are generated using a combination of Python code and Jinja templates.

## Installation
a10-saltstack is distributed as a Python package. It can be installed from the Github repository. It is assumed that saltstack is already installed and configured.

### Github Installation
```console
$ git clone https://github.com/a10networks/a10-saltstack
$ mkdir /srv/salt
$ ln -s a10-saltstack/a10_saltstack/_states /srv/salt/_states
$ ln -s a10-saltstack/a10_saltstack/_proxy /srv/salt/_proxy
$ ln -s a10-saltstack/a10_saltstack/_modules /srv/salt/_modules
```

## Example State Files
Please see (https://github.com/a10networks/a10-saltstack/tree/master/examples/states) for example states.

## Example/Dev Setup Guide (Ubuntu)

- Note that if you are Ubuntu 16.04, you'll need to add the deb in order to access the latest version of saltstack. Follow the steps here: https://repo.saltstack.com/#ubuntu

### Master Server Configuration

1. Install the necessary packages:  
`sudo apt-get install salt-api; sudo apt-get install salt-cloud; sudo apt-get install salt-master; sudo apt-get install salt-ssh; sudo apt-get install salt-syndic`

2. Clone this repository:  
`git clone git@github.com:a10networks/a10-saltstack.git`

3. Pip install the repo:
`cd a10-saltstack; sudo pip install -e .`

4. On the master, create the salt directory:  
`sudo mkdir /srv/salt` 

5. Copy the pillar dir over to the srv directory:  
`sudo cp -r ~/a10-saltstack/a10_saltstack/pillar /srv`

6. Copy the _proxy dir to the salt directory:  
`sudo cp -r ~/a10-saltstack/a10_saltstack/_proxy /srv/salt`

7. Copy the _modules dir to the salt directory:  
`sudo cp -r ~/a10-saltstack/a10_saltstack/_modules /srv/salt`

8. Copy the _states dir to the salt directory:  
`sudo cp -r ~/a10-saltstack/a10_saltstack/_states /srv/salt`

9. Copy the state file dir to the salt directory:  
`sudo cp -r ~/a10-saltstack/examples/states /srv/salt`

10. Ensure that the master is running:  
`sudo service salt-master restart`

11. (Executed after proxy minion is configured an running to accept key):  
`sudo salt-key -y -a a10`

### Proxy Minion Server Configuration

1. On the proxy minion, install the following packages:  
`sudo apt-get install salt-api; sudo apt-get install salt-cloud; sudo apt-get install salt-minion; sudo apt-get install salt-ssh; sudo apt-get install salt-syndic`

2. Clone this repository:  
`git clone git@github.com:a10networks/a10-saltstack.git`

3. Pip install the repo:
`cd a10-saltstack; sudo pip install -e .`

4. Edit `/etc/salt/proxy` and add an entry for your master's location:  
  - `sudo vim /etc/salt/proxy`
  - Add `master: <master server ip>` to file

5. Start the salt-proxy in debug mode:  
`sudo salt-proxy --proxyid=a10 -l debug`


## Bug Reporting and Feature Requests
Please submit bug reports and feature requests via GitHub issues. When reporting bugs, please include the playbook that demonstrates the bug and the Saltstack output. Stack traces are always nice, but state files work well. Please ensure any sensitive information is redacted as Issues and Pull Requests are publicly viewable.

## Contact
If you have a question that cannot be submitted via Github Issues, please email openstack-dl@a10networks.com with "a10-saltstack" in the subject line. 
