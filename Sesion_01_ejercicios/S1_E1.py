# 8/10
import inspect

name = 'Juan'

def hello_world():
    pass

class Person:
    pass


def main():
    print(explorar_namespace(globals()))

def explorar_namespace(namespace):
    categories = {
        'functions': [],
        'classes': [],
        'modules': [],
        'others': []
    }

    for key, value in namespace.items():
        if key.startswith('_'):
            continue

        if inspect.isfunction(value):
            categories['functions'].append(key)

        elif inspect.isclass(value):
            categories['classes'].append(key)
        
        elif inspect.ismodule(value):
            categories['modules'].append(key)
        
        else:
            categories['others'].append(key)
    
    return categories

        

if __name__ == '__main__':
    main()