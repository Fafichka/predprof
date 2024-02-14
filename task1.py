import csv
import datetime

with open('scientist.txt', encoding='utf8') as file:
    data = list(csv.DictReader(file, delimiter='#', quotechar='"'))
    swp=True
    while swp: #сортировка по дате
        swp=False
        for i in range(len(data)-1):
            x1,x2,x3 = [int(x) for x in data[i]['date'].split('-')]
            y1,y2,y3 = [int(x) for x in data[i+1]['date'].split('-')]
            d1 = datetime.date(x1,x2,x3)
            d2 = datetime.date(y1,y2,y3)
            if d1> d2:
                data[i], data[i+1] = data[i+1], data[i]
                swp=True
    original_alo = '' #оригинальный создатель аллопуринола
    original = {} #будем записывать всех оригинальных создателей препарата
    alopurinol = {} #те, на кого нужно отправить отчет полиции
    rows = []
    for i in range(len(data)):
        ScientistName, preparation, date, components = data[i]['ScientistName'], data[i]['preparation'],data[i]['date'],data[i]['components']
        if preparation not in original: #если нашли оригинального создателя запишем его, в противном случае пропустим
            original[f'{preparation}'] = ScientistName
            if preparation == 'Аллопуринол': #создатель аллопуринола
                original_alo = ScientistName
            rows.append(data[i]) #запишем оригинального создателя в итоговый файл
        else:
            if preparation == 'Аллопуринол': #нашли злоумышленников
                alopurinol[f'{ScientistName}'] = date
    print('Разработчиками Аллопуринола были такие люди: ')
    for i in alopurinol:
        print(i, '- ', alopurinol[i])
    print('Оригинальный рецепт принадлежит:', original_alo)
with open('scientist_origin.txt', 'w', newline='', encoding='utf8') as f:
    w=csv.DictWriter(f, fieldnames=['ScientistName', 'preparation', 'date', 'components'], delimiter='#')
    w.writeheader()
    w.writerows(rows)
