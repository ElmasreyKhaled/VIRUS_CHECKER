def shape(text):
    """start"""
    name = len(text)
    num = int(5)
    for i in range(num):
        if i == 0 or i == num - 1:
            print('*' * (name + 2))
        elif i == int(num / 2):
            print('*' + text + '*')
        else:
            print('*' + ' ' * name + '*')
