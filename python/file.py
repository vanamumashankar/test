import os
def list_of_file(path):
    try:
        files= [
         file for file in os.listdir(path)
           if os.path.isfile(os.path.join(path, file))
        ]
        return files, None
    except FileNotFoundError:
        return None, "Folder not found"
    except PermissionError:
        return None, "Permission not found"
def main():
    paths= input("enter folder path: ").split()
    for path in paths:
        files, error_message = list_of_file(path)
        if files is not None:
             print("files in ", path)
             for file in files:
                 print(file)
        else:
            print(f"Error in {path} is  {error_message}")
if __name__ == "__main__":
    main()
