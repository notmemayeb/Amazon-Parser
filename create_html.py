def create_html(products):
    with open('results.html', 'w', encoding="utf-8") as file:
        for index,item in enumerate(products):
            h1 = f'\n\n\n<a href="{item["Url"]}" target="_blank"><h1>{index+1}. {item["Name"]}</h1></a>\n\n'
            file.write(h1)
            price = f'<p>{item["Price"]}€</p>\n\n\n'
            file.write(price)
            img = '<a href="{}" target="_blank"><img src="{}"></a>'.format(item["Url"],item['Img'])
            file.write(img)