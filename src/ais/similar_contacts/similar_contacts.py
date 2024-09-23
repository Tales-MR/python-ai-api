import numpy as np
text = "teste"


def division_hash_function(any_input, table_size):
    """Returns a hash value to an string input
    
    Keyword arguments:
    input - string to be hased
    Return: a hash
    """
    
    value_to_hash   = any_input
    value_formatted = 0
    unique_number   = 7
    
    if isinstance(value_to_hash, str):
        word_divided = [char for char in value_to_hash]
        word_each_sum = 0
        
        for each in word_divided:
            word_each_sum += ord(each) 

        value_formatted = word_each_sum % unique_number
        
    elif isinstance(value_to_hash, (int, float)):
        value_formatted = value_to_hash % unique_number
    
    
    return value_formatted



def build_hash_table_with_division(array_input, table_size):
    
    # Defina o tamanho da tabela (número de linhas)
    table_size = table_size  # Exemplo: N = 10
    
    # Crie uma tabela vazia com duas colunas
    table = np.empty((table_size, 2), dtype=object)

    
    # Preencha a primeira coluna com a sequência de 0 a N-1
    table[:, 0] = np.arange(table_size)
    
    array_input = array_input
    size = table_size
    
    if (len(array_input) > size):
        print("array_input cannot has more elements than the table_size value")
        return
    

    for value in array_input:
        
        key = division_hash_function(value, size)
        

        table[key][1] = value

    return table        




    
text_formatted = build_hash_table_with_division(["banana", "cherry", "apple"], 7)
print(text_formatted)