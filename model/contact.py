from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 adress=None, phone_home=None, phone_mobile=None, phone_work=None, fax=None, email=None, emal2=None,
                 email3=None, homepage=None, bday=None, bmonth=None, byear=None, aday=None, amonth=None, ayear=None,
                 adresess2=None, phone2=None, notes=None, group=None, id=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.adress = adress
        self.phone_home = phone_home
        self.phone_mobile = phone_mobile
        self.phone_work = phone_work
        self.fax = fax
        self.email = email
        self.emal2 = emal2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.adresess2 = adresess2
        self.phone2 = phone2
        self.notes = notes
        self.group = group
        self.id = id

    def __repr__(self):
        return "%s:%s, %s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
