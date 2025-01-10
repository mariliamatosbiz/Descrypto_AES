def decode_hex_to_text(hex_string):
    """
    Tenta decodificar uma string hexadecimal usando diferentes codificações"""

    # Remove espaços em branco e quebras de linha
    hex_string = hex_string.strip()
    
    # Converte hex para bytes
    try:
        byte_data = bytes.fromhex(hex_string)
    except ValueError as e:
        return f"Erro ao converter hex: {e}"
    
    # Lista de codificações para tentar
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'ascii' ]
    
    results = {}
    
    # Tenta cada codificação
    for encoding in encodings:
        try:
            decoded_text = byte_data.decode(encoding)
            results[encoding] = decoded_text
        except UnicodeDecodeError:
            results[encoding] = f"Não foi possível decodificar usando {encoding}"
    
    return results

def main():
    # Lê o arquivo hex
    with open('arquivo-strong-7.in-full.hex', 'r') as f:
        hex_content = f.read()
    
    # Decodifica o conteúdo
    results = decode_hex_to_text(hex_content)
    
    # Imprime os resultados
    print("Resultados da decodificação:\n")
    for encoding, text in results.items():
        print(f"\n=== Decodificação usando {encoding} ===\n")
        print(text)
        print("\n" + "="*50 + "\n")
if __name__ == "__main__":
    main()