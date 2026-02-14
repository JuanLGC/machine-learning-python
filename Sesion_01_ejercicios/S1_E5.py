class Transaccion:
    def __init__(self):
        self.operaciones = []
    
    def __enter__(self):
        print("Iniciando transacción...")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print(f"COMMIT - {len(self.operaciones)} operaciones confirmadas")
        else:
            print(f"ROLLBACK - Error: {exc_val}")
            self.operaciones = []
            return True
        pass
    
    def ejecutar(self, sql):
        print(f"ejecutando: {sql}")
        self.operaciones.append(sql)
        return

def main():
    with Transaccion() as tx:
        print("estoy dentro del with")
        tx.ejecutar("INSERT INTO users VALUES ('Ana')")
        raise Exception("¡Fallo en la base de datos!") #Simular error
        tx.ejecutar("UPDATE accounts SET balance = 100")
    pass

if __name__ == "__main__":
    main()