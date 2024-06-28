import csv
import gzip

def decompress_csv(input_file, output_file):
    # Abre o arquivo compactado com gzip em modo leitura de texto ('rt')
    with gzip.open(input_file, 'rt', newline='') as f_in:
        # Cria um leitor CSV para ler as linhas do arquivo compactado
        reader = csv.reader(f_in)
        # Lê todas as linhas do arquivo e armazena em uma lista de listas (cada sublista representa uma linha do CSV)
        rows = list(reader)
    
    # Abre o arquivo de saída em modo escrita de texto ('wt')
    with open(output_file, 'wt', newline='') as f_out:
        # Cria um escritor CSV para escrever as linhas descompactadas no arquivo de saída
        writer = csv.writer(f_out)
        # Escreve todas as linhas descompactadas no arquivo de saída
        writer.writerows(rows)

# Defina o caminho do arquivo compactado que você deseja descomprimir
compressed_gz = 'caminho/do/seu/arquivo/compactado.csv.gz'
''' 
Defina o caminho onde deseja salvar o arquivo descompactado, 
deve ser na mesma pasta onde salvou o analisededados.ipynb
e o nome do arquivo deve ser cancelamentos.csv
'''
decompressed_csv = 'caminho/do/seu/arquivo/descompactado.csv'

# Chama a função para descomprimir o arquivo
decompress_csv(compressed_gz, decompressed_csv)
''' 
abra o prompt de comando, navegue até o diretorio onde está o arquivo .gz
Execute o codigo escrevendo no prompt 'python descompressaocancelamentos.py
'''