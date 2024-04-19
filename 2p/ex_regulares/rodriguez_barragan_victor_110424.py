# Expresiones regulares en python
import re

def read_file(fname):
    data = set()
    for lin in  open(fname, "r", encoding="utf8").readlines():
        t, dat = lin.rstrip().split(":")
        data.add(dat)
    return data

test= read_file("ejemplo_salida_mail_tel.txt")
gold= read_file("goldStandardTest.txt")
tp = gold.intersection(test)
fp = test.difference(gold)
fn = gold.difference(test)
precision = len(tp)/(len(tp) + len(fp))
recall =  len(tp)/(len(tp) + len(fn))
f1 = 2*precision*recall/(precision +recall)
print("PRECISION = ", precision)
print("RECALL = ", recall)
print("F1 = ", f1)
print("\nAciertos:\n", tp)
print("\n=== Datos que NO se deberían recuperar:\n", fp)
print("\n=== Datos que SI se deberían recuperar:\n", fn)

# Part 1: Extracción de correos y teléfonos
def read_html(fname):
    with open(fname, "r", encoding="utf8") as f:
        return f.readlines()

html_file = read_html("datos_testEmail.txt")

# Expresión regular para correos
# contar dentro de tags html y/o corchetes
email_regex = r'[\w\.-]+@[\w\.-]+'

def extract_emails(html_file):
    emails = set()
    for line in html_file:
        emails.update(re.findall(email_regex, line))
    return emails

emails = extract_emails(html_file)
print("=== Correos extraídos ===")
for email in emails:
    print(email + "\n")

# phone_regex = r'\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}'
# def extract_phones(html_file):
#     phones = set()
#     for line in html_file:
#         phones.update(re.findall(phone_regex, line))
#     return phones
#
# phones = extract_phones(html_file)
# print("=== Teléfonos extraídos ===")
# for phone in phones:
#     print(phone + "\n")
