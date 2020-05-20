import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from bs4 import BeautifulSoup
import lxml
import openpyxl
from openpyxl import Workbook

def callback():
    driver.switch_to_frame('webpay-iframe')
    iframe =driver.find_element_by_xpath('//*[@id="midas-webpay-main-1450000186"]/div[2]/div[1]/iframe')
    driver.switch_to_frame(iframe)
    html=driver.page_source
    soup=BeautifulSoup(html,"lxml")
    a=soup.find_all(attrs={'class':'icon-friend-s'})
    wb = Workbook()
    ws = wb.active
    ws.append(["原始数据","分组","显示名","QQ号"])
    for i in a:
        if i.next_sibling !=' {{el.name}}({{el.qq}})':
            #re,qq匹配：
            #pattern = re.compile(r'[1-9][0-9]{4,}')
            #re,括号匹配：
            #pattern = re.compile(r'(?<=\().*?(?=\))')
            #m = pattern.search(i.next_sibling)
            k=0
            for x in i.next_sibling:
                
                if x == '(':
                    f=k
                if x == ')':
                    l=k
                k=k+1
            ws.append([i.next_sibling,i.next_sibling.parent.parent.parent.parent.find(attrs={'class':'icon-more-friend'}).next_sibling,i.next_sibling[:f],i.next_sibling[f+1:l]])
            print([i.next_sibling,i.next_sibling.parent.parent.parent.parent.find(attrs={'class':'icon-more-friend'}).next_sibling,i.next_sibling[:f],i.next_sibling[f+1:l]])
		
    wb.save(asksaveasfilename(defaultextension ='.xlsx',filetypes = [('Excel 工作簿', '*.xlsx')]))


#浏览器位置
driver=webdriver.Chrome()

browser =driver
browser.get("https://pay.qq.com/index.shtml")
root = tk.Tk()
# 设置窗口标题
root.title('从QQ充值获取好友列表——峡州仙士制作')
# 设置窗口大小
root.geometry('400x200')
# 进入消息循环（检测到事件，就刷新组件）
button = tk.Button(root, text='已登陆并打开充值界面，且点开列表', command=callback)
button.pack()
root.mainloop()
