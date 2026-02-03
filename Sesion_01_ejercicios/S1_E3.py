def process_cli(command):
    command_parts = command.split()
    
    list_of_commands = [
        "create <nombre>",
        "delete <nombre>",
        "list",
        "search <term>",
        "search <term> --limit N"  
    ]
    
    match command_parts:
        case ["create", project]:
            return f"Creating new project: {project}"
        case ["delete", project]:
            return f"Deleting project: {project}"
        case ["help"]:
            return f"This is a list of commands available: \n{list_of_commands}"
        case ["list"]:
            return f"Should print a list of something"
        case ["search", term]:
            return f"Searching for {term} in document"    
        case ["search", term, "--limit", N]:
            return f"Searching for {term} in document (max results: {N})"
        case _:
            return "Unknown command. Type 'help' for available commands"

def main():
    print(process_cli("create proyecto"))
    print(process_cli("delete proyecto"))
    print(process_cli("help"))
    print(process_cli("list"))
    print(process_cli("search python --limit 10")) 

if __name__ == '__main__':
    main()