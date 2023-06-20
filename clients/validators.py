import re
from validate_docbr import CPF


def cpf_valid(cpf):
    doc = CPF()

    return doc.validate(cpf)

def rg_valid(rg):
    return len(rg) == 9

def name_valid(name):
    return name.isalpha()

def mobile_phone_valid(mobile_phone):
    valid = True
    if len(mobile_phone) != 14:
        valid = False

    mask = '\([0-9]{2}\)9[0-9]{4}-[0-9]{4}'  # (99)90000-0000
    if not re.findall(mask, mobile_phone):
        valid = False

    return valid
