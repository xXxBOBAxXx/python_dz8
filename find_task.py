def to_find(t):
    search_fragment = input('введите ключевое слово или дату (фрагмент): ')
    find_id = []
    id = 0
    for fragment in t:
        if search_fragment in str(fragment):
            find_id.append(id)     
        else: 
            tras = input('задача не найдена, попробробовать еще раз? 1 - да, любой другой символ - отмена: ')
            if tras == '1': to_find(t)
            else: return
        id += 1
    return find_id