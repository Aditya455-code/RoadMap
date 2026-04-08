import pandas as pd
import numpy as np
# print(pd.DataFrame({'A':[1,3,4]}))
# s=pd.Series([1,2,3,np.nan,5,7])
# print(s)

# dates=pd.date_range("20040811",periods=10)
# # print(dates)
# df=pd.DataFrame(np.random.randn(10,4),index=dates,columns=list('ABCD'))
# # print(df)

# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )



# # print(df2[0:3])
# print(df2.loc[dates[0]])

# print(df2.sort_index(axis=1, ascending=False))
# print(df2.sort_values(by='C'))

# print(df2.loc[:,["A","B"]])

df1=pd.DataFrame(
    {
        "A":['A0','A1','A2','A3'],
        "B":['B0','B1','B2','B3'],
        "C":['C0','C1','C2','C3'],
        "D":['D0','D1','D2','D3']
    },
    index=[0,1,2,3]
)
df3=pd.DataFrame(
    {
      "B":['B2','B3','B6','B7'],
      "D":['D2','D3','D6','D7'],
      "F":['F2','F3','F6','F7']
    },
    index=[2,3,6,7]
)

print(df3.merge(df1,how='outer'))
