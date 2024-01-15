import os
a = int(input("a : "))
b = int(input("b : "))

with open('index.js', 'w') as file:
	print('var mainElement = document.getElementsByTagName("main")[0];', file=file)
	print("var content = ``;", file=file)
	while a<=b:
		folder_path = str(a)
		file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
		print("",file=file)
		print(f'content += `<h1>Halaman {a}</h1>`', file=file)
		print('for (let i = 0; i <=',file_count,'; i++) {',file=file)
		print('	content += `<div><img src="'+str(a)+'/${i}.kiryuu.id.jpg"/></div>`',file=file)
		print('}',file=file)
		a+=1
	print('mainElement.innerHTML = content;',file=file)
