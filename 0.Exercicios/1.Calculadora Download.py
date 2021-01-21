#Faça um programa que peça o tamanho de um arquivo para download (em MB)
# e a velocidade de um link de Internet (em Mbps), calcule e informe o 
# tempo aproximado de download do arquivo usando este link (em minutos).
tamanho = int(input('Digite o tamanho do arquivo: '))
velocidade = int(input('Velocidade da internet em Mbps'))
total_segundos = tamanho / (velocidade/8.4)
total_minutos = total_segundos / 60
total_horas = total_minutos / 60
if __name__ == "__main__":
    print(f"""Tempo estimado  para download:
                {total_segundos} segundos;
                {total_minutos} minutos;
                {total_horas} horas""")
