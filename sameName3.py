def spam():
    global eggs
    eggs = 'spam'

def bacon():
    eggs = 'bacon'
    print(eggs)

def ham():
    print(eggs)

eggs = 42
print(eggs)
spam()
bacon()
print(eggs)