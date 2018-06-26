import datetime
import os
import time
from tkinter import *
from tkinter import messagebox

import psutil
from PIL import Image
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

url = 'http://www.jd.com'
try_url = 'http://try.jd.com/activity/getActivityList?page=1&activityType=3&activityState=0'
file_name = r'C:\Users\Quincy_C\Desktop\jd.png'


def msg_show():
    """
    信息提示
    :return:
    """
    root = Tk()
    root.title('')
    (width, height) = (0, 0)
    root.geometry('%dx%d+%d+%d' % (
        width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
    root.maxsize(0, 0)
    root.minsize(0, 0)
    label = Label(root, )
    label.pack()
    root.withdraw()  # 将主窗体隐藏
    messagebox.showwarning('消息', '扫码完成登陆后请按确定')


def jd_login():
    """
    登录函数
    :return:
    """
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_link_text('你好，请登录').click()
    time.sleep(4)

    driver.get_screenshot_as_file(file_name)
    f = open(file_name, 'rb')
    image = Image.open(f)
    image.show()
    msg_show()
    # TODO:点击确定后自动关闭图片√
    f.close()
    w, h = image.size
    # 1291 659
    # print(w, h)
    if w == 1291 or h == 659:
        os.remove(file_name)
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        # print('pid-%s,pname-%s' % (pid, p.name()))
        if p.name() == 'dllhost.exe':
            cmd = 'taskkill /F /IM dllhost.exe'
            os.system(cmd)
    # 获取浏览器标题
    title = driver.title
    if title == '京东-欢迎登录':
        print('登录失败！', datetime.date.today())
    else:
        print('登录成功！', datetime.date.today())


def try_goods():
    """
    试用功能发起
    :return:
    """
    driver.get(try_url)
    time.sleep(2)
    total_page = driver.find_element_by_xpath('//*[@id="J_bottomPage"]/span[2]/em[1]/b').text
    # total_goods = driver.find_element_by_xpath('//*[@id="J_resCount"]').text
    for i in range(int(total_page)):
        print('正在申请第{}页'.format(i + 1))
        driver.get('http://try.jd.com/activity/getActivityList?page=%s&activityType=3&activityState=0' % str(i + 1))
        time.sleep(2)

        now_handle_tab = driver.current_window_handle
        li_count = driver.find_elements_by_xpath('//*[@id="goods-list"]/div[2]/div/ul')[0].find_elements_by_class_name(
            'item')
        # TODO:查出子元素个数√
        apply_count = 0
        for j in range(1, len(li_count) + 1):
            time.sleep(2)
            a = '/html/body/div[4]/div[2]/div/div[1]/div[2]/div/ul/li[' + str(j) + ']/div/a'
            try:
                driver.find_element_by_xpath(a).click()
                apply_count += 1
            except:
                print('全部申请完毕，共：', apply_count)
                driver.close()
                break
            time.sleep(1)
            # 新开一个浏览器Tab窗口
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(0.5)

            try:
                if driver.find_element_by_link_text('申请试用'):
                    time.sleep(1)
                    # 找到产品名字
                    product_name = driver.find_element_by_xpath(".//*[@id='product-intro']/div[2]/div[1]/span").text
                    driver.find_element_by_link_text('申请试用').click()
                    # 打印产品名字
                    print(product_name, datetime.datetime.now())
                    time.sleep(0.5)
                elif driver.find_element_by_link_text('查看更多试用'):
                    time.sleep(0.5)

            except Exception:
                print('该商品已申请过~')

            try:
                time.sleep(0.8)
                if driver.find_element_by_link_text('取消'):
                    driver.find_element_by_link_text('取消').click()
                    time.sleep(1)
                elif driver.find_element_by_link_text('申请成功！'):
                    time.sleep(0.1)
                elif driver.find_element_by_link_text('操作不要太快哦！'):
                    time.sleep(2)
            except Exception:
                pass

            driver.close()
            driver.switch_to.window(now_handle_tab)


if __name__ == '__main__':
    jd_login()
    while True:
        try_goods()
    # pids = psutil.pids()
    # for pid in pids:
    #     p = psutil.Process(pid)
    #     print('pid-%s,pname-%s' % (pid, p.name()))
