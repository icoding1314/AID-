for i in range(1,9):
    print('打印第%s页'%i)
    filename = 'day0%s.txt'%str(i)
    with open('爬虫知识点.txt', 'a+', encoding='utf-8') as f1:
    f1.write('\n')
    with open(filename, 'r', encoding='utf-8') as f:
        i = 1
        while True:
            x = f.readline()
            print(x)
            if x == '\n':
                i += 1
                # continue
                if i > 3:
                    print(len(x))
                    # print(type(x))
                    print(i, 'i的值')
                    break
            with open('爬虫知识点.txt', 'a+', encoding='utf-8') as f1:
                f1.write(x)
print('拷贝成功')


