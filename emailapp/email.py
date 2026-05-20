class Email:
    def __init__(self, id, title, description, time, status):
        self.id = id
        self.title = title
        self.description = description
        self.time = time
        self.status = status


EMAIL_STORE = [
    Email(0, "Thong bao lich phong van", "Phong van luc 14h00", "04/06/2026", True),
    Email(1, "Ket qua phong van", "Chuc mung ban", "04/07/2026", False),
    Email(2, "Thong bao lich lam viec", "Thu 2 den thu 6", "11/07/2026", True),
]


def get_email_list():
    return EMAIL_STORE


def get_email_by_id(id):
    emails = get_email_list()
    return emails[id]


def delete_email_by_id(id):
    global EMAIL_STORE
    EMAIL_STORE = [email for email in EMAIL_STORE if email.id != id]
