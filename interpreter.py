import json
import os

json_file_path = os.path.join("src", "files", "print.json")

try:
    with open(json_file_path, 'r') as json_file:
        json_data = json.load(json_file)


    def execute_json(json_data):
        if json_data["expression"]["kind"]  == "Print":
            menssage = json_data["expression"]["value"]["value"]
            print(menssage)

        else:
            print("Erro: sintaxe errada!")


    execute_json(json_data)

except FileNotFoundError:
    print(f"Erro: Arquivo JSON não encontrado em '{json_file_path}'.")

except json.JSONDecodeError:
    print(f"Erro: Falha na decodificação do JSON em '{json_file_path}'.")

except Exception as e:
    print(f"Erro desconhecido: {str(e)}")