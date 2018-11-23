1.txt文本
	'''
	用open方法打开一个文件，获取一个文件操作对象，赋值为file，接着使用write方法来将爬取的内容写入文件，最后调用close方法关闭文件
	'''
	file = open('**.txt','a',encoding='utf-8')
	file.write('')
	file.close()
	 
	 
	'''with控制块结束时会自动关闭文件'''
	with open('**.txt','a',encoding='utf-8') as file:
	    file.write('')
2.csv文本
	'''
	首先打开CSV文件，指写的模式，使用writer方法初始化写入对象，再使用writerow方法传入每行的数据
	delimiter参数是用来修改列与列之间的分隔符
	爬虫爬取的都是结构化数据，一般都会使用字典
	如果想追加写入，修改open函数的w为a即可
	encoding解决写入中文时遇到的字符乱码问题
	'''
	import csv
	# 写入
	with open('data.csv','w',encoding='utf-8') as file:
	    writer = csv.writer(file,delimiter='')
	    writer.writerow({['id','name','age']})
	    writer.writerow({['1', 'a', '1']})
	    writer.writerow({['2', 'b', '2']})
	    writer.writerow({['3', 'c', '3']})
	# 读取
	with open('data.csv','r',encoding='utf-8') as file:
	    # 构造CSV的reader对象，然后遍历输出对应的内容
	    reader = csv.reader(file)
	    for row in reader:
	        print(row)
3.json文本
	'''
	loads方法将json文本字符串转化为json对象，
	dumps方法将json对象转化为文本字符串
	json的数据必须使用双引号，使用单引号会报错
	'''
	import json
	str = [{
	    "names":"bbb",
	    "sex":"man",
	}]
	data = json.loads(str)
	data[0]['names']
	data[0].get('name')
	print(data)
	'''
	dumps方法将json对象转为字符串
	indent代表缩进的格数
	ensure_ascii = False  为了输出是中文
	'''
	with open('data.json','w') as file:
	    file.write(json.dumps(data,indent = 2,ensure_ascii = False))