def updatefile(file_path, key, value):
    with open(file_path, 'r') as file:
        lines= file.readlines()
    with open(file_path, 'w') as file:
        for line in lines:
            if key in line:
                
                file.write(key + "=" + value + "\n")
                print(f'updated {key} changed to {value}')
                
            else:
                file.write(line)
file_path='server.config'
file_key= input("enter which key to change")
file_value= input("enter value")
updatefile(file_path, file_key, file_value)

