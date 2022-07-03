import os,csv

#定义查找目录
findPath = 'D:/study/visualStudioFile/pythonStudy/'
#获取查找目录下所有文件
filenames = os.listdir(findPath)
#获取查找关键词
keyWord = "你好"
# 打开结果文件
result_file = open('./pythonStudy/resource/find_result.txt', 'a', encoding='utf-8')
#遍历文件
for file in filenames:
#如果是txt文件    
    if '.txt' in file:
# 找到文件时先打印提示
        print("找到了文件：" + file)
        target_file = findPath  + file
#打开文件，r只读，编码utf-8        
        with open(target_file, 'r', encoding='utf-8') as f:
#读取整个文件            
            fileText = f.read()
#如果关键词在文件中            
            if keyWord in fileText:
#打印文件名                
                print(file)
                result_file.write(target_file + '\n')

# 关闭结果文件
result_file.close()

