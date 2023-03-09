import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import csv
#hotmail import 
import random
from time import sleep
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
#URLS
SINGN_UP:str = "https://signup.live.com/signup"
FAKE_USER_GENERATOR:str ="https://www.fakenamegenerator.com/gen-random-us-uk.php"
PROOFS_ADD:str = "https://account.live.com/proofs/Add"
LOGIN:str = "https://outlook.live.com/owa/?nlp=1"

# PROXY VARIABLES
HOST :list[str] = []
PORT :str = str

# creating a hotmail class 

class Hotmail:
    ''' hotmail class for creation and saving seeds '''

    def __init__(self) -> None:
        self.host = str
        self.port = str
        self.firstname = str
        self.lastname = str
        self.email = str
        self.password = str
        self.birthday = str
        self.confirmation_mail = str
    
    def get_host(self)->str:
        ''' get host'''
        return self.host
    def set_host(self,host)->None:
        ''' set host'''
        self.host = host
    
    def get_port(self)->str:
        ''' get port'''
        return self.port
    def set_port(self,port)->None:
        '''set port'''
        self.port = port

    def get_email(self)->str:
        '''get email'''
        return self.email
    def set_email(self,email)->None:
        '''set email'''
        self.email = email
    
    def get_password(self)->str:
        ''' get password'''
        return self.password
    def set_password(self,password)->None:
        ''' set password'''
        self.password = password
    
    def get_confirmation_mail(self)->str:
        '''get_confirmation_mail'''
        return self.confirmation_mail
    
    def set_confirmation_mail(self,confirmation_mail)->None:
        '''set_confirmation_mail'''
        self.confirmation_mail = confirmation_mail

    def my_proxy(self)->webdriver:
        ''' open a firfox profile using a specifique proxy '''
        try:
            try:
                firefoxProfile:FirefoxProfile = FirefoxProfile()
                firefoxProfile.set_preference("network.proxy.type", 1)
                firefoxProfile.set_preference("network.proxy.http",self.host)
                firefoxProfile.set_preference("network.proxy.http_port",int(self.port))
                firefoxProfile.set_preference("network.proxy.ssl",self.host)
                firefoxProfile.set_preference("network.proxy.ssl_port",int(self.port))
                firefoxProfile.set_preference("general.useragent.override","whater_useragent")
                firefoxProfile.update_preferences()
                binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
                browser = webdriver.Firefox(executable_path=r'C:\\WebDrivers\\geckodriver.exe', firefox_binary=binary,firefox_profile=firefoxProfile)
            except Exception:
                self.host = random.choice(HOST)
                firefoxProfile:FirefoxProfile = FirefoxProfile()
                firefoxProfile.set_preference("network.proxy.type", 1)
                firefoxProfile.set_preference("network.proxy.http",)
                firefoxProfile.set_preference("network.proxy.http_port",int(self.port))
                firefoxProfile.set_preference("network.proxy.ssl",self.host)
                firefoxProfile.set_preference("network.proxy.ssl_port",int(self.port))
                firefoxProfile.set_preference("general.useragent.override","whater_useragent")
                firefoxProfile.update_preferences()
                binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
                browser = webdriver.Firefox(executable_path=r'C:\\WebDrivers\\geckodriver.exe', firefox_binary=binary,firefox_profile=firefoxProfile)
        except Exception:
            try:
                firefoxProfile:FirefoxProfile = FirefoxProfile()
                firefoxProfile.set_preference("network.proxy.type", 1)
                firefoxProfile.set_preference("network.proxy.http",self.host)
                firefoxProfile.set_preference("network.proxy.http_port",int(self.port))
                firefoxProfile.set_preference("network.proxy.ssl",self.host)
                firefoxProfile.set_preference("network.proxy.ssl_port",int(self.port))
                firefoxProfile.set_preference("general.useragent.override","whater_useragent")
                firefoxProfile.update_preferences()
                browser = webdriver.Firefox(firefox_profile=firefoxProfile)
            except Exception:
                self.host = random.choice(HOST)
                firefoxProfile:FirefoxProfile = FirefoxProfile()
                firefoxProfile.set_preference("network.proxy.type", 1)
                firefoxProfile.set_preference("network.proxy.http",)
                firefoxProfile.set_preference("network.proxy.http_port",int(self.port))
                firefoxProfile.set_preference("network.proxy.ssl",self.host)
                firefoxProfile.set_preference("network.proxy.ssl_port",int(self.port))
                firefoxProfile.set_preference("general.useragent.override","whater_useragent")
                firefoxProfile.update_preferences()
                browser = webdriver.Firefox(firefox_profile=firefoxProfile)
        return browser

    def clear_and_input(self,id:any,value:str,browser:webdriver)->None:
        """ clear and put value in input field """
        elem = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.ID, id))
        )
        elem.clear()
        elem.send_keys(value)
    
    def click_(self,browser,id:any)->None:
        """ click on submit button """
        elem = WebDriverWait(browser, 20).until(
            EC.presence_of_element_located((By.ID, id))
        )
        elem.click()

    def generate_user_info(self,browser):
        browser.get(FAKE_USER_GENERATOR)
        user = browser.find_element(By.CLASS_NAME,'address').find_element(By.TAG_NAME,'h3').text
        user = user.split(' ')
        del user[1]
        self.firstname = str(user[0])
        self.lastname = str(user[1])
        self.email = str(user[1])+"_"+str(user[0])+"_"+str(random.randint(1,1000))+'@hotmail.com'
        self.password = self.firstname+self.lastname+str(random.randint(1,500))+'@'
        
    def create(self,_host) -> None:
        ''' create a hotmail account '''
        # get a random proxy
        while True:
            try:
                self.set_host(_host)
                self.set_port(int(PORT))
                browser = self.my_proxy()
                break
            except Exception:
                print(f'{self.host} not working')
                
        #get user info {firstname,lastname,email,password}
        self.generate_user_info(browser)

        # change the window
        browser.execute_script("window.open('');")
        browser.switch_to.window(browser.window_handles[1])
        #get sign-up url
        browser.get(SINGN_UP)
        try:
            self.clear_and_input("MemberName",self.email,browser)
            self.click_(browser=browser,id="iSignupAction")
            self.clear_and_input(id="PasswordInput",value=self.password,browser=browser)
            # input the password 
            try:
                elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, 'iSignupAction'))
                )
                elem.click()
            except Exception:
                elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.ID, 'PasswordForm'))
                )
                elem.submit()
            finally:
                sleep(3)        
            self.clear_and_input(id="FirstName",value=self.firstname,browser=browser)
            self.clear_and_input(id="LastName",value=self.lastname,browser=browser)
            self.click_(browser=browser,id="iSignupAction")

            #create a random date of birth 
            day = int(random.randint(2,29))
            month = int(random.randint(2,13))
            year = random.randint(1976,2004)
            self.birthday = str(day)+'/'+str(month-1)+'/'+str(year)
            _day = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.ID, "BirthDay"))
            )
            Select(_day).select_by_index(day)
            _month = WebDriverWait(browser, 30).until(
                EC.presence_of_element_located((By.ID, "BirthMonth"))
            )
            Select(_month).select_by_index(month)
            self.clear_and_input(id="BirthYear",value=str(year),browser=browser)

            #submit all info to get the captcha
            browser.find_element(By.ID,"iSignupAction").click()
            self.confirmation_mail = self.firstname+'_'+self.lastname+str(random.randint(1,20))+'@mailnesia.com'
            browser.switch_to.window(browser.window_handles[0])
            browser.close()
        except Exception:
            browser.close()
            browser.close()

    def get_code(self,email,browser)->str:
        ''' get code from the mail box '''
        sleep(5)
        self.clear_and_input(id="mailbox",value=email,browser=browser)
        self.click_(browser=browser,id="sm")
        tBody = browser.find_element(By.TAG_NAME,'table').find_element(By.TAG_NAME,'tbody')
        tr = tBody.find_elements(By.TAG_NAME,'tr')
        td = tr[0].find_elements(By.TAG_NAME,'td')
        td[4].click()
        table = browser.find_elements(By.TAG_NAME,'table')
        _tr = table[1].find_element(By.TAG_NAME,'tbody').find_elements(By.TAG_NAME,'tr')
        td = _tr[3].find_element(By.TAG_NAME,'td')
        code :str = td.find_element(By.TAG_NAME,'span').text  

        return code

    def recover(self) ->None:
        ''' add recovery mail to the email created'''
        browser = self.my_proxy()
        try:
            browser.get(PROOFS_ADD)
            valide = False
            try:
                self.clear_and_input(id="i0116",value=self.email,browser=browser)
                self.click_(browser=browser,id="idSIButton9")
                sleep(3)
                pwd = browser.find_element(By.ID,"i0118")
                pwd.send_keys(self.password)
                browser.find_element(By.ID,"idSIButton9").click()
                self.clear_and_input(id="EmailAddress",value=self.confirmation_mail,browser=browser)
                self.click_(browser=browser,id="iNext")

                browser.execute_script("window.open('');")
                browser.switch_to.window(browser.window_handles[1])
                browser.get("https://mailnesia.com/")

                # get email verification code 
                code = self.get_code(email=self.confirmation_mail,browser=browser)

                browser.switch_to.window(browser.window_handles[0])
                self.clear_and_input(id="iOttText",value=code,browser=browser)
                self.click_(browser=browser,id="iNext")
            except Exception:
                valide = True

            elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'table'))
                )
            elem.click()
            self.clear_and_input(id="idTxtBx_SAOTCS_ProofConfirmation", value=self.confirmation_mail,browser=browser)    
            self.click_(browser=browser,id="idSubmit_SAOTCS_SendCode")
            if valide == True:
                browser.execute_script("window.open('');")
                browser.switch_to.window(browser.window_handles[1])
                browser.get("https://mailnesia.com/")
            else:
                browser.switch_to.window(browser.window_handles[1])

            # get email verification code
            code = self.get_code(email=self.confirmation_mail,browser=browser)
            browser.close()
            browser.switch_to.window(browser.window_handles[0])
            self.clear_and_input(id="idTxtBx_SAOTCC_OTC",value=code,browser=browser)
            self.click_(browser=browser,id="idSubmit_SAOTCC_Continue")
            sleep(3)
            browser.close()
        except:
            print(self.email)
            browser.close()  

    def go_junk(self,browser):
        browser.get("https://outlook.live.com/mail/junkemail")

    def reply(self,browser):
        pass

    def flag(self,browser):
        button = browser.find_elements(By.CLASS_NAME,"splitPrimaryButton ")   
        button[4].click()

    def ping(self,browser):
        self.click_(browser=browser,id="548")

    def reporting(self):    
        browser = self.my_proxy()     
        browser.get(LOGIN)
        self.clear_and_input(id="i0116",value=self.email,browser=browser)
        self.click_(browser=browser,id="idSIButton9")
        sleep(3)
        pwd = browser.find_element(By.ID,"i0118")
        pwd.send_keys(self.password)
        browser.find_element(By.ID,"idSIButton9").click()   
        
        self.click_(browser=browser,id="idBtn_Back")
        sleep(1)
        self.go_junk(browser=browser)
        try:
            elem = WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "zXLz3"))
            )
            mails = elem.find_elements(By.TAG_NAME,"div")
            total_mails = len(mails)
            for i in range(total_mails):
                n = random.randrange(1,150)
                mails[1].click()
                sleep(5)
                if n%2 == 0:
                    self.flag(browser=browser)
                    sleep(5)
                browser.find_element(By.ID,"540").click()
                inbox = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.NAME, "Boîte de réception"))
                )
                inbox.click()
                try:
                    form = WebDriverWait(browser, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "form"))
                    )
                    form.submit()
                except Exception:
                    pass
                try:
                    elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "zXLz3"))
                    )
                    mails = elem.find_elements(By.TAG_NAME,"div")
                except Exception:
                    browser.close()
        except Exception:
            browser.close()
            
    def send(self,to,subject):
        browser = self.my_proxy()     
        browser.get(LOGIN)
        try: 
            self.clear_and_input(id="i0116",value=self.email,browser=browser)
            self.click_(browser=browser,id="idSIButton9")
            sleep(3)
            pwd = browser.find_element(By.ID,"i0118")
            pwd.send_keys(self.password)
            browser.find_element(By.ID,"idSIButton9").click()  
            try: 
                elem1 = WebDriverWait(browser,5).until(
                    EC.presence_of_element_located((By.id,'iShowSkip'))
                )
                elem.click()
            except Exception:
                self.click_(browser=browser,id="idBtn_Back")
            sleep(1)
            self.go_junk(browser=browser)
            sleep(10)
            buttons =browser.find_elements(By.CLASS_NAME,"splitPrimaryButton")
            buttons[0].click()
            elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "UKx9j"))
                )
            sub_elem = elem.find_elements(By.TAG_NAME,"div")
            sub_elem[1].send_keys(to)
            elem = WebDriverWait(browser, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "ms-TextField-field"))
                )
            elem.send_keys(subject)
            
            browser.find_element(By.XPATH,'//*[@title="Envoyer (Ctrl+Entrée)"]').click()
            sleep(5)
        except Exception:
            print(self.email)
        finally:
            browser.close()
    
    def delete_spam(self):
        browser = self.my_proxy()     
        browser.get(LOGIN)
        try:
            self.clear_and_input(id="i0116",value=self.email,browser=browser)
            self.click_(browser=browser,id="idSIButton9")
            sleep(3)
            pwd = browser.find_element(By.ID,"i0118")
            pwd.send_keys(self.password)
            browser.find_element(By.ID,"idSIButton9").click()   
            
            self.click_(browser=browser,id="idBtn_Back")
            sleep(1)
            self.go_junk(browser=browser)
        
            sleep(5)
            elem = WebDriverWait(browser,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,'vQae6'))
            )
            elem.click()
            buttons = browser.find_elements(By.CLASS_NAME,'splitPrimaryButton')
            buttons[1].click()
            ok = WebDriverWait(browser,10).until(
                EC.presence_of_element_located((By.ID,'ok-1'))
            )
            ok.click()
            sleep(5)
        except Exception:
            print(self.email)
        finally:
            browser.close()

    def login(self):
        browser = self.my_proxy()     
        browser.get(LOGIN)
        try:
            self.clear_and_input(id="i0116",value=self.email,browser=browser)
            self.click_(browser=browser,id="idSIButton9")
            sleep(3)
            pwd = browser.find_element(By.ID,"i0118")
            pwd.send_keys(self.password)
            browser.find_element(By.ID,"idSIButton9").click()   
            
            self.click_(browser=browser,id="idBtn_Back")
        except Exception:
            browser.close()

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.numSeedsToCreate = QSpinBox()
        self.to = QLineEdit()
        self.subject = QLineEdit()
        self.textEdit = QTextEdit()
        self.port = QLineEdit()
        grid = QGridLayout()
        grid.addWidget(self.create(), 0, 0)
        grid.addWidget(self.recover(), 0, 1)
        grid.addWidget(self.reporting(),0, 2)
        grid.addWidget(self.send(), 1, 0)
        grid.addWidget(self.proxy(), 1, 1)
        grid.addWidget(self.features(), 1, 2)


        self.setLayout(grid)
        
        self.setWindowTitle("hotmail app")
        self.setFixedSize(1000, 900)
    def use_list(self):        
        _host = self.textEdit.toPlainText().split("\n")

        if len(_host) > 0:
            for h in _host:
                HOST.append(h)
            print(len(HOST))
            QMessageBox.about(self, "success","proxies added succesfully")
            
        else:
            QMessageBox.about(self, "error","proxy list is empty")
    def add_port(self):
        PORT = int(self.port.text())
        if PORT:
        print(PORT)
            QMessageBox.about(self, "success","port added succesfully")
            
    def add_proxy(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            with open(list(filepath)[0], 'r',encoding='UTF-8') as f:   
                reader = csv.reader(f, delimiter=',')
                for line in reader:
                    if line:
                        HOST.append(line[0])
        print(len(HOST))
    # functional logique
    def _create(self):  
        _host = random.choice(HOST)

        i = 0
        if int(self.numSeedsToCreate.text()) > 0:
            folderpath = QFileDialog.getExistingDirectory(self, 'Select Folder')
            if folderpath:
                while i < int(self.numSeedsToCreate.text()):
                    #create a hotmail obj
                    _hotmail = Hotmail()
                    #create a hotmail mail
                    try:
                        _hotmail.create(_host)
                        DATA = {
                            'host':_hotmail.get_host(),
                            'port':_hotmail.get_port(),
                            'email':_hotmail.get_email(),
                            'password':_hotmail.get_password(),
                            'confirmation_mail':_hotmail.get_confirmation_mail()
                        }
                        _date = datetime.datetime.now()
                        filename =str(f'{_date.day}-{_date.month}-{_date.year}.csv')
                        with open(f"{folderpath}\{filename}",'a') as csvfile:
                            writer = csv.writer(csvfile)
                            writer.writerow(DATA.values())
                    except Exception:
                        print(_hotmail.get_host())
                    #incriment
                    i+=1
        else:
            QMessageBox.about(self, "Error", "number must be greater then 0")

    def _reporting(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            seeds:list=[]
            with open(list(filepath)[0],'r',encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if line:
                        seeds.append(line)
            for seed in seeds:
                h = Hotmail()
                h.set_host(seed[0])
                h.set_port(seed[1])
                h.set_email(seed[2])
                h.set_password(seed[3])
                h.reporting()
    
    def _recover(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            seeds:list=[]
            with open(list(filepath)[0],'r',encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if line:
                        seeds.append(line)
            for seed in seeds:
                h = Hotmail()
                h.set_host(seed[0])
                h.set_port(seed[1])
                h.set_email(seed[2])
                h.set_password(seed[3])
                h.set_confirmation_mail(seed[4])
                h.recover()
    
    def _send(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            seeds:list=[]
            with open(list(filepath)[0],'r',encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if line:
                        seeds.append(line)
            for seed in seeds:
                h = Hotmail()
                h.set_host(seed[0])
                h.set_port(seed[1])
                h.set_email(seed[2])
                h.set_password(seed[3])
                h.send(self.to.text(),self.subject.text())
    
    def delete_spam(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            seeds:list=[]
            with open(list(filepath)[0],'r',encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if line:
                        seeds.append(line)
            for seed in seeds:
                h = Hotmail()
                h.set_host(seed[0])
                h.set_port(seed[1])
                h.set_email(seed[2])
                h.set_password(seed[3])
                h.delete_spam()
    
    def login(self):
        filepath = QFileDialog.getOpenFileName(self, 'Select Folder')
        if list(filepath)[0]:
            seeds:list=[]
            with open(list(filepath)[0],'r',encoding='UTF-8') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for line in reader:
                    if line:
                        seeds.append(line)
            for seed in seeds:
                h = Hotmail()
                h.set_host(seed[0])
                h.set_port(seed[1])
                h.set_email(seed[2])
                h.set_password(seed[3])
                h.login()
   # layout 
    def create(self):
        groupBox = QGroupBox("create seeds")
        label = QLabel("")

        buttonBox = QPushButton("create")
        buttonBox.clicked.connect(self._create)
        buttonBox.setFixedSize(100,30)

        vbox = QVBoxLayout()
        vbox.addWidget(self.numSeedsToCreate)
        vbox.addWidget(label)
        vbox.addWidget(buttonBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        groupBox.setFixedSize(300,250)
        return groupBox
    
    def recover(self):
        groupBox = QGroupBox("recover seeds")
        label = QLabel("import csv file with this form: ")
        labe2 = QLabel("host,port,email,password,mailrecovery")

        buttonBox = QPushButton("recover")
        buttonBox.clicked.connect(self._recover)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(labe2)

        vbox.addWidget(buttonBox)        
        vbox.addStretch(1)
        groupBox.setLayout(vbox)
        groupBox.setFixedSize(300,250)

        return groupBox
    
    def reporting(self):
        groupBox = QGroupBox("reporting junck to inbox")
        label = QLabel("import csv file with this form")
        labe2 = QLabel(": host,port,email,password")

        buttonBox = QPushButton("reporting")
        buttonBox.clicked.connect(self._reporting)
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(labe2)
        vbox.addWidget(buttonBox)
        vbox.addStretch(1)
        groupBox.setLayout(vbox)    
        groupBox.setFixedSize(300,250)

        return groupBox
    
    def send(self):
        groupBox = QGroupBox("send mail a spesific mail box")
        label = QLabel("to")
        labe2 = QLabel("subject")

        buttonBox = QPushButton("send")
        buttonBox.clicked.connect(self._send)
        buttonBox.setFixedSize(100,30)

        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(self.to)
        vbox.addWidget(labe2)
        vbox.addWidget(self.subject)
        vbox.addWidget(buttonBox)

        vbox.addStretch(1)
        groupBox.setLayout(vbox)  
        groupBox.setFixedSize(300,250)

        return groupBox
    
    def proxy(self):
        groupBox = QGroupBox("import proxies")
        
        buttonBox = QPushButton("add proxy")
        buttonBox.clicked.connect(self.add_proxy)
        buttonBox2 = QPushButton("use this list")
        buttonBox2.clicked.connect(self.use_list)
        buttonBox3 = QPushButton("add port")
        buttonBox3.clicked.connect(self.add_port)

        vbox = QVBoxLayout()
        vbox.addWidget(self.port)
        vbox.addWidget(buttonBox3)
        vbox.addWidget(buttonBox)
        vbox.addWidget(self.textEdit)
        vbox.addWidget(buttonBox2)

        vbox.addStretch(1)
        groupBox.setLayout(vbox)  
        groupBox.setFixedSize(300,250)

        return groupBox
    
    def features(self):
        groupBox = QGroupBox("login or delete spam ")
        
        label = QLabel("import csv file with this form:")
        labe2 = QLabel(" host,port,email,password")

        buttonBox = QPushButton("login")
        buttonBox2 = QPushButton("empty spam folder")
        buttonBox.clicked.connect(self.login)
        buttonBox2.clicked.connect(self.delete_spam)
        vbox = QVBoxLayout()
        vbox.addWidget(label)
        vbox.addWidget(labe2)

        vbox.addWidget(buttonBox)
        vbox.addWidget(buttonBox2)

        vbox.addStretch(1)
        groupBox.setLayout(vbox)  
        groupBox.setFixedSize(300,250)

        return groupBox

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Window()
    clock.show()
    sys.exit(app.exec_())
