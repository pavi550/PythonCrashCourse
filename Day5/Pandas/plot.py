import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',periods=10), columns=list('ABCD'))

df.plot()