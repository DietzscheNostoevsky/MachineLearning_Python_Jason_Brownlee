#!/usr/bin/env python
#!/usr/bin/env python3

# check library version numbers

import os
import sklearn
import statsmodels
import pandas
import matplotlib
import numpy
import scipy

os.system("clear")
# scipy
print('scipy: %s' % scipy.__version__)
# numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
print('sklearn: %s' % sklearn.__version__)
