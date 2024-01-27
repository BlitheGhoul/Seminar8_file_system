def rewrite1(data, num_file):
    data = [f'{i + 1};{data[i].split(";")[1]};'
            f'{data[i].split(";")[2]};'
            f'{data[i].split(";")[3]};'
            f'{data[i].split(";")[4]}'
            for i in range(len(data))]
    with open(f'db//data_{num_file}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)
        
def rewrite2(num_file):
    with open(f'db//data_{num_file}.txt', 'r', encoding='utf-8') as file:
        data = file.readlines()
    data = [f'{i + 1};{data[i].split(";")[1]};'
                f'{data[i].split(";")[2]};'
                f'{data[i].split(";")[3]};'
                f'{data[i].split(";")[4]}'
                for i in range(len(data))]
    with open(f'db//data_{num_file}.txt', 'w', encoding='utf-8') as file:
        file.writelines(data)