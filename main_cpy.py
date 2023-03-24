from Selenium import Browser
from SendMail import Mail
from selenium.webdriver.common.by import By
from time import time, sleep
import os
import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
#Hola

# INICIO DEFINICIÓN DE VARIABLES
driver_path = "drivers/chromedriver"
url_to_scrape ="https://finance.yahoo.com/crypto/"
max_num_row=0
max_num_col=11
row_glb    =0
n_loop     =0

# FIN DEFINICIÓN DE VARIABLES

# INICIO DEFINICIÓN DE FUNCIONES
def fn_write_data_to_file(p_text_list):
    '''Function to write the crypto data to file '''
    line_text =''
    for i, crypto in enumerate(p_text_list):
        if i == len(p_text_list) -1 :
            line_text = (line_text + crypto)
        else:
            line_text =(line_text +  crypto + '|')

    with open(file='files/Cryptocurrencies.txt', mode='a') as crypto_f:
        crypto_f.write(f"{line_text}\n")

def fn_get_header(p_max_num_col : int):
    '''Fuction for getting the header'''
    text_line_list = []
    for i in range(1, p_max_num_col):
        x_path_head = '// *[ @ id = "scr-res-table"] / div[1] / table / thead / tr / th' + '[' + str(i) + ']'
        crypto_table_head = browser.webbrowser.find_elements(By.XPATH, x_path_head)
        text_line_list.append(crypto_table_head[0].text)
    text_line_list.insert(0,'Nro. Row')
    # Delete the file before starting to write new lines
    if os.path.exists('files/Cryptocurrencies.txt'):
        os.remove('files/Cryptocurrencies.txt')
    fn_write_data_to_file(p_text_list=text_line_list)

def fn_get_data_clear(p_max_num_row: int):
    '''Fuction for getting the data and cleanning them'''
    global row_glb
    for i in range(p_max_num_row):
        x_path_row='//*[@id="scr-res-table"]/div[1]/table/tbody/tr' + '[' + str(i + 1) + ']'
        crypto_table= browser.webbrowser.find_elements(By.XPATH,x_path_row)
        row_glb +=1
        text_line = crypto_table[0].text.split()
        text_line_list = []
        coin_name =' '
        for j in range(len(text_line) - 8):
            if j != 0:
                coin_name = coin_name + ' ' + text_line[j]
        text_line_list.append(text_line[0])
        text_line_list.append(coin_name)
        for k in range(len(text_line) - 8, len(text_line)):
            text_line_list.append(text_line[k])
        text_line_list.insert(0, str(row_glb))
        fn_write_data_to_file(p_text_list=text_line_list)

def fn_display_scraper_app():
    global windows
    w_padx          =20
    w_pady          =20
    app_width       =800
    app_height      =600
    windows         =tk.Tk()
    screen_width    =windows.winfo_screenwidth()
    screen_height   =windows.winfo_screenheight()
    windows.title('DISPLAY CRYPTO INFORMATION')
    windows.config(width=app_width,height=app_height,padx=w_padx,pady=w_pady,bg='#E4DCCF')
    x=int((screen_width/2 - app_width/2))
    y=int((screen_height/2 - app_height/2))
    windows.geometry(f'{int(app_width)}x{int(app_height)}+{x}+{y}')
    canvas  = tk.Canvas(width=750,height=550,bg='#E4DCCF',highlightthickness=5)
    canvas.create_text(375,20,text='SCRAPPING : https://finance.yahoo.com/crypto/',font=('Arial',16,'bold'))
    canvas.grid(row=1,column=1)
    frame_main  =tk.Frame(width=750,height=490,borderwidth=1,relief='groove',bg='#E4DCCF')
    frame_main.grid(row=1, column=1)
    windows.update()
    windows.mainloop()
# FIN DEFINICIÓN DE FUNCIONES

# INICIO PROGRAMA PRINCIPAL
print(f'App: {__name__}')
if __name__ =='__main__':
    fn_display_scraper_app()


    # browser = Browser(p_driver_path=driver_path)
    # browser.mth_open_browser(url_page=url_to_scrape)
    # sleep(10)
    # total_blocks  =int(browser.webbrowser.find_element(By.XPATH,'//*[@id="fin-scr-res-table"]/div[1]/div[1]/span[2]').text.split()[2])
    # max_num_row   =int(browser.webbrowser.find_element(By.XPATH,'//*[@id="scr-res-table"]/div[2]/span').text.split()[1])
    # n_loop  =5 #round(total_blocks/max_num_row)
    # print('------------SCRAPPING HEADER------------')
    # fn_get_header(p_max_num_col=max_num_col)
    # for i in range(n_loop):
    #     print(f'{i}------------SCRAPPING DATA------------')
    #     fn_get_data_clear(p_max_num_row=max_num_row)
    #     get_next_btn   =browser.webbrowser.find_element(By.XPATH, '//*[@id="scr-res-table"]/div[2]/button[3]')
    #     get_next_btn.click()
    #     sleep(5)
    # browser.mth_close_browser()
    # mail = Mail(p_host         ="smtp.gmail.com"
    #             ,p_port        =587
    #             ,p_mail_from   ="jorgevinsencio@gmail.com"
    #             ,p_mail_pwd    ="siylsxrabxeshjnq"
    #             ,p_mail_to     ="jvfiguera@hotmail.com"
    #             ,p_subject     ="Crypto file information"
    #             ,p_msg         ="Se anexa información estadisticas del comportamiento de las crypto monedas"
    #             ,p_filename    ='files/Cryptocurrencies.txt'
    #             )
