table = {
    "%%2305": "The specified user account has expired.",
    "%%2309": "The specified account's password has expired.",
    "%%2310": "Account currently disabled.",
    "%%2311": "Account logon time restriction violation.",
    "%%2312": "User not allowed to logon at this computer.",
    "%%2313": "Unknown user name or bad password."
}

def getDescription(FailureReasonCode):
    return table.get(FailureReasonCode)
