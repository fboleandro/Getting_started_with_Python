num = 0
tot = 0.0
while True :
    sval = input('Enter a number: ')
    if sval == 'done' :
        break
    try :
        nval = int(sval)
    except:
        print('Invalid imput')
        continue
    # print(nval)
    num = num + 1
    tot = nval + num

# print('All done')
print(tot,num,)
