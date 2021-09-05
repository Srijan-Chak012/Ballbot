
def to_send(message):
    msg = message.split()
    con = " ".join(msg[1:])
    print(con)
    if con == "a" or con == "a bc":
        return 'chal gaya'

    return "Not Found"




