import re


def username_is_valid(username: str) -> bool:
    padrao_username = re.compile('^[a-zA-Z]+[.]?[a-zA-Z]+$')
    match = padrao_username.match(username)
    if not match:
        return False
    return True


def email_is_valid(email: str) -> bool:
    padrao_email = re.compile('^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$')
    match = padrao_email.match(email)
    if not match:
        return False
    return True


def cnpj_is_valid(cnpj: str):
    padrao_cnpj = re.compile('^\d{2}[\.]?\d{3}[\.]?\d{3}[\/]?\d{4}[-]?\d{2}$')
    if not padrao_cnpj.match(cnpj):
        return False
    return True
