
import pandas as pd

s = pd.Series([1,2,3,4,5,6,7], index=['a','b','c','d','e','f','g'])
df = pd.DataFrame({"models": ['cr1', 'cr2', 'cr6','cr8','cr9','cr4','cr0'], "index": [ 190, 171, 178, 180, 188, 200, 167 ]})

df.rename(columns={"models":"mens"})
print(df)