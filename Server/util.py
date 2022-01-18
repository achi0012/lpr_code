import datetime
# import hashlib
# from urllib.parse import quote


def strtodate_yyyymmddhhmmss(s: str):
    return datetime.datetime.strptime(s, "%Y%m%d%H%M%S")


def to_date_path(d: datetime):
    return d.strftime("%Y/%m/%d/%H/")


def datetostr_yyyymmddhhmiss(d: datetime):
    return d.strftime("%Y%m%d%H%M%S")


# def to_key(s):
#     sha = hashlib.sha256()
#     sha.update(quote(str(s)).encode("utf-8"))
#     return sha.hexdigest().upper()
