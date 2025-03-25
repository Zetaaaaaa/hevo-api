import os
import importlib
import inspect
import json
import config

def get_functions_from_module(module_name):
    module = importlib.import_module(module_name)
    functions = {
        name: func
        for name, func in inspect.getmembers(module, inspect.isfunction)
        if name != 'load_config'
    }
    return functions

def main():
    while True:
        files = [f[:-3] for f in os.listdir() if f.endswith('.py') and f not in ('main.py', 'loader.py', 'config.py', 'my_api.py')]
        if not files:
            print("No valid modules found.")
            break

        print("\nAvailable modules:")
        for idx, file in enumerate(files, 1):
            print(f"{idx}. {file}")

        try:
            file_number = int(input("\nSelect file by number (or 0 to exit): ")) - 1
            if file_number == -1:
                break
            if file_number < 0 or file_number >= len(files):
                print("Invalid file number")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue

        module_name = files[file_number]
        functions = get_functions_from_module(module_name)

        if not functions:
            print(f"No functions found in '{module_name}'")
            continue

        print("\nAvailable functions:")
        function_list = list(functions.keys())
        for idx, func in enumerate(function_list, 1):
            print(f"{idx}. {func}")

        try:
            function_number = int(input("\nSelect function by number (or 0 to go back): ")) - 1
            if function_number == -1:
                continue
            if function_number < 0 or function_number >= len(function_list):
                print("Invalid function number")
                continue
        except ValueError:
            print("Please enter a valid number")
            continue

        function_name = function_list[function_number]
        function = functions[function_name]

        # Handle parameters
        signature = inspect.signature(function)
        params = signature.parameters
        args = []
        kwargs = {}

        try:
            for param in params.values():
                if param.default == param.empty:
                    value = input(f"Enter value for required '{param.name}': ")
                    args.append(value)
                else:
                    value = input(f"Enter value for optional '{param.name}' (press enter to skip): ")
                    if value:
                        kwargs[param.name] = value

        except ValueError as e:
            print(f"Error: {e}")
            continue

        # Call the function
        try:
            result = function(*args, **kwargs)
            print("\nResult:")
            if isinstance(result, (dict, list)):
                print(json.dumps(result, indent=4))
            else:
                print(result)
        except Exception as e:
            print(f"Error executing function '{function_name}': {e}")

        # Loop control
        cont = input("\nRun another function? (yes/no): ").strip().lower()
        if cont != "yes":
            break

if __name__ == "__main__":
    # Load configuration at the start
    config.set_config()
    main()
