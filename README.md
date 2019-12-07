# pytonik ip and vpn checker

[![Build Status](https://img.shields.io/pypi/v/pytonik_ip_vpn_checker)](https://pypi.python.org/pypi/pytonik_ip_vpn_checker)
[![Downloads](https://img.shields.io/pypi/dm/pytonik_ip_vpn_checker)](https://pypi.python.org/pypi/pytonik_ip_vpn_checker/)
[![Wheel](https://img.shields.io/pypi/wheel/pytonik_ip_vpn_checker.svg)](https://pypi.python.org/pypi/pytonik_ip_vpn_checker)
[![Python Version](https://img.shields.io/pypi/pyversions/pytonik_ip_vpn_checker)](https://pypi.python.org/pypi/pytonik_ip_vpn_checker)
[![License](https://img.shields.io/pypi/l/pytonik_ip_vpn_checker)](https://pypi.python.org/pypi/pytonik_ip_vpn_checker)

[pytonik](https://pypi.python.org/pypi/pytonik) IP and VPN checker Module checks visitors/audiences, proxy, sock, and VPN IP address. it returns a response such as :- **hostname**, **country**, **city**, **region**, **loc**, **org** and more. 

## Install pytonik ip and vpn checker
```
pip install pytonik_ip_vpn_checker

```
## Import Module
```
from pytonik_ip_vpn_checker.ip import ip
```
### how to get HTTP IP ADDRESS
ip.get().ip

### how to get VPN IP ADDRESS
```
ip.vpn().ip
```

### how to check if visitor is using VPN
```
ip.vpn().is_vpn
```

### how to get IP ADDRESS and PROPERTIES
```
pytonik_user = ip.get()
pytonik_user.ip
pytonik_user.hostname
pytonik_user.city
pytonik_user.region
pytonik_user.country
pytonik_user.loc
pytonik_user.org

```

### default check IP ADDRESS
```
ip.property('41.190.30.100').hostname
ip.property('41.190.30.100').city
ip.property('41.190.30.100').region
ip.property('41.190.30.100').country
ip.property('41.190.30.100').loc
ip.property('41.190.30.100').org
	
```

pytonik is open to questions and contributions, feel free to ask.

## Contact Information:

**Name:**  pytonik MVC

**Email:** pytonikmvc@gmail.com
