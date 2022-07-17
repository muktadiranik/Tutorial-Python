def function(**kwargs):
    print(kwargs)


function(a=1, b=2, c='x', d='y')


def function(**n):
    print(n)


function(a=1, b=2, c='x', d='y')
function(a='a', b='b')
