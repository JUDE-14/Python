print('Name: Jude Andrew \nUSN: 1AY24AI049 \nSection: M\n ')

def commaCode(items):
    if len(items) == 0:
        return ''
    elif len(items) == 1:
        return items[0]
    return ', '.join(items[:-1]) + ' and ' + items[-1]

print(commaCode(['apples', 'bananas', 'tofu', 'cats']))
