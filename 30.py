def arifm_prog (first_element, diff, total_elements):
    prog_list = [first_element]
    for i in range(2,total_elements+1):              
        prog_list.append(first_element+(i-1)*diff)
    print(prog_list)


first = int(input('Введите первый элемент прогрессии '))
differ = int(input('Введите разность прогрессии '))  
total_lenght = int(input('Введите длинну прогрессии '))

arifm_prog(first, differ, total_lenght)