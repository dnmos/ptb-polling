import csv
import datetime

# write data to csv
def statistics(user_id, username, userfullname, command):
  date = datetime.datetime.today().strftime("%Y-%m-%d")
  with open('data.csv', 'a', newline="") as file:
    wr = csv.writer(file, delimiter=';')
    wr.writerow([date, user_id, username, userfullname, command])