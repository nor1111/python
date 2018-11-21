from tkinter import *
import tkinter.simpledialog as dl
import tkinter.messagebox as mb
import read

root = Tk()
w = Label(root,text = 'one title')
w.pack

mb.showinfo('welcome',"welcome to every's words")
words = dl.askinteger('','请输入密码')

while words != 8426:
	words = dl.askinteger('','请输入密码')
	
mb.showinfo('output:','your password is right')

print('汉英填空，请在每次输入完答案后单击回车键\n')
words = dict(zip(read.word_list,read.chinese_list))

for english,trans in words.items():
	print(trans)
	result=0
	while result <1 :
		reply=input('English: ')
		if reply == english:
			result=1
			print('答对了！\n')
		else:
			print("答错了，你有两种选择：重试/进行下一题，你可以直接敲击‘回车’键来"
					"进行重试，或者输入'n'来进行下一题")
			order=input('your choice: ')
			if order == 'n':
				print('正确答案： ' + english)
				result = 1
				print('\n')
print('\n恭喜你已完成今天的复习!')
print('给你我的小心心——\n  oo   oo\n o  o o  o\no    o    o\no         o\n'
		' o       o\n   o   o\n     o')		
print('design by Northwest')
