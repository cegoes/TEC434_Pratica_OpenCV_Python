import time

# armazena o tempo de início
start_time = time.time() 

# código a ser medido o tempo de execução


# armazena o tempo de término
end_time = time.time() 

elapsed_time = end_time - start_time # calcula o tempo decorrido

print("Tempo de processamento: {:.5f} segundos".format(elapsed_time)) # mostra o tempo de processamento com 5 casas decimais