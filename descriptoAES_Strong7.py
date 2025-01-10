def hex_to_utf8(input_file):
    try:
        # Abre o arquivo de entrada para leitura
        with open(input_file, 'r') as infile:
            hex_data = infile.read().strip()  # Lê o conteúdo e remove espaços em branco extras

        # Converte o conteúdo hexadecimal para bytes
        try:
            byte_data = bytes.fromhex(hex_data)
        except ValueError:
            print("Erro: O arquivo contém dados que não são válidos em hexadecimal.")
            return

        # Decodifica os bytes para string UTF-8
        try:
            utf8_text = byte_data.decode('utf-8')
        except UnicodeDecodeError:
            print("Erro: Os dados não são válidos no formato UTF-8.")
            return

        # Imprime o texto UTF-8 na tela
        print(utf8_text)

    except FileNotFoundError:
        print(f"Erro: O arquivo {input_file} não foi encontrado.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

# Exemplo de uso
if __name__ == "__main__":
    entrada = "arquivo-strong-7.in-full.hex"
    hex_to_utf8(entrada)
