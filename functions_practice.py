def hello():
    print('Hello user')

def pack(x,y,z):
    return[x,y,z]

def eat_lunch(list):
    if len(list) == 0:
        print('my lunchbox is empty!')
    else:
        for i in range(len(list)):
            if i == 0:
                print(f"first i eat {list[0]}")
            else:
                print(f"next i eat {list[1]}")

hello()
pack(1,2,3)
eat_lunch(['eggs', 'bacon'])