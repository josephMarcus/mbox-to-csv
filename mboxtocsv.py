import mailbox
import csv342 as csv

def mbox_to_csv(mbox_file,csv_file):
    with open(csv_file,'w',newline='',encoding='utf-8') as CSVfile:
        fieldnames=['From','Subject','Date','Message']
        writer=csv.DictWriter(CSVfile,fieldnames=fieldnames)
        writer.writeheader()
        mbox=mailbox.mbox(mbox_file)
        for message in mbox:
            0
            writer.writerow({
            'From':message['From'],'Subject':message['Subject'],'Date':message['Date'],'Message':message.get_payload()})
mbox_file='mails.mbox'
csv_file='csvfile.csv'
 
mbox_to_csv(mbox_file,csv_file)
