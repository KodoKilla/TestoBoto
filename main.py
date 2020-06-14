# Fiz tudo no main pq sou bagaceiro #

from nerodia.browser import Browser

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

def loginNovus(browser):
    # Login no Sistema Novus #
    browser.goto('localhost/pages/Login.php')

    login = browser.text_field(name='user')
    login.value = 'admin'
    senha = browser.text_field(name='password')
    senha.value = 'admin'
    browser.button(name='submit').click()


def insereUser(browser):
    # Ir ate a tela de adicionar usuario #
    browser.goto('localhost/pages/UsuariosList.php')
    browser.wait()
    browser.link(value='Adicionar').click()

    # Adicionar um usuario de teste #
    usuario = browser.text_field(id='usuario')
    nome = browser.text_field(id='nome')
    email = browser.text_field(id='email')
    senha = browser.text_field(id='senha')

    usuario.value = 'AutoBot'
    nome.value = 'Bot de Teste'
    email.value = 'BotTestadorNovus@gmail.com'
    senha.value = 'AutoBot'

    browser.button(name='salvar').click()


# 'Main' #
browser = iniciaBot()
loginNovus(browser)
insereUser(browser)


