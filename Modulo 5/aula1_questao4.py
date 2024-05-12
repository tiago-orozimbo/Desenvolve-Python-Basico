import datetime
data = datetime.datetime.now ()
data2 = data.strftime("%d %m %Y")
data2 = "{}/{}/{}".format(data.day, data.month, data.year)
hora = data.strftime("%H:%M")
print(f'Data: {data2}')
print(f'Hora: {hora}')
