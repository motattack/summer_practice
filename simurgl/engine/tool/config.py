from configparser import ConfigParser


def write(config):
    with open(file, 'w', encoding="utf-8") as configfile:
        config.write(configfile)


file = 'engine/config.ini'
config = ConfigParser()
config.read(file, encoding="utf-8")

# Theme
theme_style = config.getboolean('Themes', 'theme_style')


def update_theme(style):
    config.set('Themes', 'theme_style', f'{style}')
    write(config)


# Settings
autorun_status = config.getboolean('Settings', 'autorun')
hide_mod_status = config.getboolean('Settings', 'hide_mode')
protect_status = config.getboolean('Settings', 'protect')


def update_autorun(status):
    config.set('Settings', 'autorun', f'{status}')
    write(config)


def update_hide_mode(status):
    config.set('Settings', 'hide_mode', f'{status}')
    write(config)


def get_hide_mode():
    return config.getboolean('Settings', 'hide_mode')


def update_protect(status):
    config.set('Settings', 'protect', f'{status}')
    write(config)


# User
api = config['User']['api']
username = config['User']['username']
is_user = lambda message: message.from_user.username == username


def update_api(token):
    config.set('User', 'api', f'{token}')
    write(config)


def update_username(user):
    config.set('User', 'username', f'{user}')
    write(config)