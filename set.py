lst_in = ['Пушкин: Сказака о рыбаке и рыбке',
'Есенин: Письмо к женщине',
'Тургенев: Муму',
'Пушкин: Евгений Онегин',
'Есенин: Русь']
lst = [x.split(':') for x in lst_in]
books = {lst[i][0]:lst[i][1] for i  in range(len(lst))}
print(books)