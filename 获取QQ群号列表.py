import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from lxml import etree
import lxml
from bs4 import BeautifulSoup
import openpyxl
from openpyxl import Workbook
import time



#去字符串两端'\n'、'\t'
def delNT(s):
		       while s.startswith('\n') or s.startswith('\t'):
			
			       s=s[1:]
		       while s.endswith('\t') or s.endswith('\n'):
			      
			       s=s[:-1]
		       return s



def callback():
    wb = Workbook()
    ws = wb.active
    ws.append(["原始数据","QQ群号"])
    a=driver.find_elements_by_class_name('icon-def-gicon')
    Num= len(a)
    time_start=time.time()
    for i in range(0,Num):
        
        #点击进入具体群
        a=driver.find_elements_by_class_name('icon-def-gicon')
        #time.sleep(0.5)
        a[i].click()
        time.sleep(1)
        html=driver.page_source
        soup=BeautifulSoup(html,"lxml")
        groupTit=delNT(soup.find(attrs={'id':'groupTit'}).text)
        groupMemberNum=delNT(soup.find(attrs={'id':'groupMemberNum'}).text)

        try:
            k=0
            for v in groupTit:
                
                if v == '(':
                    f=k
                if v == ')':
                    l=k
                k=k+1
            ws.append([groupTit,groupTit[f+1:l]])
            print(str(int((time.time()-time_start)/60))+':'+str(int((time.time()-time_start)%60)),'第'+str(i+1)+'群,'+str(int((i+1) / Num * 100))+'%  '+groupTit+'  此项完成')
          
            
           
        driver.find_element_by_id('changeGroup').click()
        time.sleep(1)
        wb.save(asksaveasfilename(defaultextension ='.xlsx',filetypes = [('Excel 工作簿', '*.xlsx')]))


driver=webdriver.Chrome()

browser =driver
browser.get("https://qun.qq.com/member.html")
root = tk.Tk()
# 设置窗口标题
root.title('从QQ群管理获取群成员列表——峡州仙士制作')
# 设置窗口大小
root.geometry('400x200')
# 进入消息循环（检测到事件，就刷新组件）
button = tk.Button(root, text='已登陆并打开界面', command=callback)
button.pack()
root.mainloop()
