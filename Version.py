# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 07/12/2019.

import sys

VERSION = (1, 0, 5, '', 1)

if VERSION[3] and VERSION[4]:
	VERSION_TEXT = '{0}.{1}.{2}{3}{4}'.format(*VERSION)
else:
	VERSION_TEXT = '{0}.{1}.{2}'.format(*VERSION[0:3])

VERSION_EXTRA = ''
LICENSE = 'Apache 2.0'#MIT
EDITION = ''  # Added in package names, after the version
KEYWORDS = "mvc, oop, module"

PYVERSION_MA = sys.version_info.major
PYVERSION_MI = sys.version_info.minor

