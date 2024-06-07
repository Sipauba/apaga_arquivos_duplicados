import os

def delete_duplicate_files(folder_path):
    # Dicionário para armazenar arquivos por nome (sem extensão)
    file_dict = {}

    # Iterar sobre todos os arquivos na pasta
    for filename in os.listdir(folder_path):
        # Ignorar diretórios
        if os.path.isdir(os.path.join(folder_path, filename)):
            continue
        
        # Obter o nome do arquivo sem extensão
        name, ext = os.path.splitext(filename)
        
        # Adicionar o arquivo ao dicionário, agrupando por nome (sem extensão)
        if name in file_dict:
            file_dict[name].append(filename)
        else:
            file_dict[name] = [filename]

    # Iterar sobre o dicionário para encontrar e apagar arquivos duplicados
    for name, files in file_dict.items():
        if len(files) > 1:
            print(f"Duplicados encontrados para '{name}': {files}")
            for file in files:
                file_path = os.path.join(folder_path, file)
                os.remove(file_path)
                print(f"Arquivo removido: {file_path}")

# Exemplo de uso
folder_path = 'C:/Users/normady/Desktop/TESTE APAGA ARQUIVOS/imagens'
delete_duplicate_files(folder_path)
