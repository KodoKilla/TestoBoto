from nerodia.browser import Browser
import time

def basicSearch():
    # Retirado do Site do Nerodia, para teste inicial #
    browser = Browser(browser='chrome')
    browser.goto('google.com')

    search_input = browser.text_field(title='Pesquisar')
    search_input.value = 'nerodia'
    browser.button(value='Pesquisa Google').click()

    browser.close()

def iniciaBot():
    # Inicializacao do Bot #
    browser = Browser(browser='chrome')

    return browser

def loginInvalido(browser):
    # Login Invalido no Sistema Novus #
    browser.goto('localhost/pages/Login.php')

    login = browser.text_field(name='user')
    login.value = 'admin'
    senha = browser.text_field(name='password')
    senha.value = 'teste'
    browser.button(name='submit').click()

def loginNovus(browser, sleep):
    # Login no Sistema Novus #
    browser.goto('localhost/pages/Login.php')

    login = browser.text_field(name='user')
    login.value = 'admin'
    time.sleep(sleep)
    senha = browser.text_field(name='password')
    senha.value = 'admin'
    time.sleep(sleep)
    browser.wait()
    browser.button(name='submit').click()


def insereUser(browser, sleep):
    # Ir ate a tela de adicionar usuario #
    browser.goto('localhost/pages/UsuariosList.php')
    time.sleep(sleep)
    browser.link(value='Adicionar').click()

    # Adicionar um usuario de teste #
    usuario = browser.text_field(id='usuario')
    nome = browser.text_field(id='nome')
    email = browser.text_field(id='email')
    senha = browser.text_field(id='senha')

    usuario.value = 'AutoBot'
    time.sleep(sleep)
    nome.value = 'Bot'
    time.sleep(sleep)
    email.value = 'BotTestadorNovus@gmail.com'
    time.sleep(sleep)
    senha.value = 'AutoBot'

    time.sleep(sleep)
    browser.button(name='salvar').click()

def apagaUser(browser, sleep):
    browser.wait()
    browser.goto('localhost/pages/UsuariosList.php')
    time.sleep(sleep)
    browser.link(id='Bot').click()
    time.sleep(sleep)
    browser.alert.ok()

# 'Main' #
sleep = 0
browser = iniciaBot()
#loginInvalido(browser)
loginNovus(browser, sleep)
insereUser(browser, sleep)
apagaUser(browser, sleep)
