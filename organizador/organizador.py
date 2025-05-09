import os
from shutil import move
import argparse

def organize_files(path):
    # Categorias e extensões
    print(f'📂 Iniciando organização da pasta: {path}\n')
    extensions = {
        'TextFiles': ['.txt', '.docx'],
        'Comand': ['.bat'],
        'PDFs': ['.pdf'],
        'Canvas': ['.canvas'],
        'Ink': ['.ink'],
    }

    files = os.listdir(path)

    for file in files:
        full_path = os.path.join(path, file)

        if not os.path.isfile(full_path):
            continue

        # Pega a extensão
        _, ext = os.path.splitext(file)

        # Encontra a pasta principal correspondente
        target_folder = None
        for folder, exts in extensions.items():
            if ext.lower() in exts:
                target_folder = folder
                break

        if not target_folder:
            print(f'🔍 Ignorado (sem categoria definida): {file}')
            continue  # pula arquivos sem categoria definida

        # Cria a pasta principal (categoria)
        main_folder_path = os.path.join(path, target_folder)
        os.makedirs(main_folder_path, exist_ok=True)

        # Cria subpasta com o nome da extensão
        subfolder = ext.lower().replace('.', '')  # remove o ponto
        subfolder_path = os.path.join(main_folder_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)

        # Move o arquivo
        new_path = os.path.join(subfolder_path, file)
        move(full_path, new_path)
        print(f'✅ Moved {file} to {target_folder}/{subfolder}/')

    print('\n📂 Organização concluída!'
    )

def moveFile(file, path):
    print(f'📌 Tentando mover arquivo específico: {file}')

    if not os.path.exists(file):
        print(f"❌ Arquivo '{file}' não encontrado.")
        return

    _, ext = os.path.splitext(file)

    extensions = {
        'TextFiles': ['.txt', '.docx'],
        'Comand': ['.bat'],
        'PDFs': ['.pdf'],
        'Canvas': ['.canvas'],
        'Ink': ['.ink'],
    }

    # Encontra a pasta principal correspondente
    target_folder = None
    for folder, exts in extensions.items():
        if ext.lower() in exts:
            target_folder = folder
            break

    if target_folder is None:
        print(f"⚠️ A extensão '{ext}' não está mapeada em nenhuma pasta de destino.")
        return

    # Define subpasta e caminhos
    subfolder = ext.lower().replace('.', '')
    destination_folder = os.path.join(path, target_folder, subfolder)
    os.makedirs(destination_folder, exist_ok=True)

    new_path = os.path.join(destination_folder, os.path.basename(file))

    if os.path.exists(new_path):
        answer = input('⚠️ Arquivo já existente, sobrescrever, ignorar ou renomear? (s/i/r) ').strip().lower()

        if answer == 's':
            os.remove(new_path)
            print('🗑️ Arquivo removido.')
        elif answer == 'i':
            print('🚫 Arquivo ignorado.')
            return
        elif answer == 'r':
            new_name = input('Novo nome (sem extensão): ')
            new_path = os.path.join(destination_folder, new_name + ext)
            if os.path.exists(new_path):
                print('❌ Arquivo com esse nome já existe.')
                return
            else:
                print('✅ Arquivo renomeado.')
        else:
            print('❗ Opção inválida.')
            return

    move(file, new_path)
    print(f'✅ {os.path.basename(file)} - Arquivo movido para: {target_folder}/{subfolder}/')


parser = argparse.ArgumentParser(description='Organizador de arquivos por extensão.')
parser.add_argument('--path', '-p', type=str, help='Caminho da pasta a ser organizada')
parser.add_argument('--file', '-f', type=str, help='Mover arquivo específico para a pasta de destino')

if __name__ == '__main__':
    # Tudo que depende de argumentos vai aqui dentro
    args = parser.parse_args()

    if args.path:
        if not os.path.exists(args.path):
            print(f"❌ Pasta não encontrada: {args.path}")
        else:
            if args.file:
                moveFile(args.file, args.path)
            organize_files(args.path)
    else:
        print("❗ Você precisa passar ao menos o argumento --path.")

    print('🚀 ORGANIZADOR DE ARQUIVOS\n')



# Execução
print('🚀 ORGANIZADOR DE ARQUIVOS\n')

