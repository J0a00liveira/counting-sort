import re

def counting_sort(arr):
    max_val = max(arr)
    
    count = [0] * (max_val + 1)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    output = [0] * len(arr)
    
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
    
    return output

def get_numbers():
    while True:
        input_numbers = input("Digite os números que deseja ordenar, separados por espaço: ").strip()
        if not input_numbers:
            print("Entrada vazia. Por favor, digite pelo menos um número.")
            continue
        
        arr = [int(num) for num in re.findall(r'\d+', input_numbers)]
        
        if not arr: 
            print("Nenhum número válido encontrado. Por favor, tente novamente.")
        else:
            return arr

arr = get_numbers()

sorted_arr = counting_sort(arr)
print("Array ordenado:", sorted_arr)
