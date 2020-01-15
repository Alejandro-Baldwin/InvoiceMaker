import pandas as pd
d = {'xq':['ja','ja','ja'],'la':['la','la','la']}
fields = {}
info = ['Alex','3142342']
df1 = pd.DataFrame(data = d)
df1.set_index('la', inplace=True, drop = True)
writer = pd.ExcelWriter('lalala.xlsx', engine ='xlsxwriter', mode = 'w')
df1.to_excel(writer, startrow = 10, startcol= 4)
writer.save() 