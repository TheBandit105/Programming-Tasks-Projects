info = {'name':'Bob' , 'ref':'Python' , 'sys': 'Win'}
print('info:', type(info))
print('Dictionary:', info)

print('\nReference:' , info['ref'])

print('\nKeys:' , info.keys())

del info['name']
info['user'] = 'Tom'
print( '\nDictionary:', info)

print( '\nls There A name Key?:' ,'name' in info)

