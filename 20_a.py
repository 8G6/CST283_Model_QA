from pandas import DataFrame
dit = {
        'SN': ['1','2','3'],
        'Name':[
                 'Linus Torvalds',
                 'Tim Berners-Lee',
                 'Guido van Rossum'
               ],
        'Country':[
                    'Finland',
                    'England',
                    'Netherlands'
                  ],
        'Contribution':[
                        'Linux Kernel',
                        'World Wide Web',
                        'Python'
                       ],
        'Year':[
                  '1991',
                  '1990',
                  '1991'
               ]
      }

df = DataFrame(dit)

df.to_csv('files\\new.csv')

#without using pd

f = open('files/file.csv','w')

data = [
        ['SN','Name','Country','Contribution','Year'],
        ['1','Linus Torvalds','Finland','Linux Kernel','1991'],
        ['2','Tim Berners-Lee','England','World Wide Web','1990'], 
        ['3','Guido van Rossum','Netherlands','Python','1991']
       ]

for line in data:
    for item in line:
        f.write(item+',')
    f.write('\n')