
def main():
    validar_nombre = create_validator(min_len=2, max_len=50, data_type=str)
    print(validar_nombre('12345'))

def create_validator(min_len, max_len, data_type):
    def validate(name):
        data_type_ok = isinstance(name, data_type)
        max_len_ok = max_len is None or len(name) <= max_len
        min_len_ok = len(name) >= min_len
        
        return data_type_ok and max_len_ok and min_len_ok
    
    return validate

if __name__ == '__main__':
    main()