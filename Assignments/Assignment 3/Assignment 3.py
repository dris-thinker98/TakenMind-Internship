import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=exf.parse('PivotTable')
df1=df.groupby(["Age","Year"],as_index=False).sum()
dfu=df1.pivot("Age","Year","Ratio")
dfu.reset_index()
flat=pd.DataFrame(dfu.to_records())
print(flat["Age"])
df1i=flat[:]
del df1i["Age"]
pd.isnull(np.array(df1i, dtype=float))
print(df1i)
plt.figure(figsize=(8,8))
ax=sns.heatmap(df1i,fmt="g", linewidths=.5,yticklabels=flat["Age"],cmap="plasma")
plt.title("Year vs Age - Sex Ratio")
plt.ylabel("Age Range")
plt.xlabel("Year")
plt.savefig("Assignment3.png")
plt.show()
