
from typing import Any, Text, Dict, List
from rasa_sdk import  Tracker
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
import mysql.connector
import pandas as pd
import smtplib, ssl
db = mysql.connector.connect(host="localhost",username="root",password="24122000",database="movies")
dbcurs = db.cursor()


class SendToal(Action):

    def name(self) -> Text:
        return "send_total"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_message = str((tracker.latest_message)['text'])

        messages = []

        for event in tracker.events:
            if event.get("event") == "user":
                messages.append(event.get("text"))
        mv=messages[-3]
        print(mv)
        st=messages[-2]
        print(st)
        dbcurs.execute(f"select price from MovieList where name='{mv}' and seat='{st}'")
        price = 0
        for i in dbcurs:
            price=i[0]
            print(price)
        nost = int(messages[-1])
        total = price*nost
        print(total)
        try:
            fromaddr = 'yashkhant24@gmail.com'
            toaddrs = 'yashnkhant2412@gmail.com'
            msg = f"Subject: Ticket \n\nMovie: {mv} \nSeat: {nost}, {st} \ntotal: {total}"
            username = 'yashkhant24@gmail.com'
            password = "9586536383"
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(username, password)
            server.sendmail(fromaddr, toaddrs, msg)
            server.quit()


            bill = f"Movie: {mv} \nSeat: {nost}, {st} \ntotal: {total}"
            content = "Your Ticket Has Been Booked And Sent over mail"
            dispatcher.utter_message(text=bill)
            dispatcher.utter_message(text=content)

        except:
            content_text = "Sorry system run into trouble.. Can you please check again?"
            dispatcher.utter_message(text=content_text)

        return []


# class SendTotal(Action):
#      def name(self) -> Text:
#         return "send_total"
#
#      def run(self, dispatcher: CollectingDispatcher,
#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         messages = []
#         for event in (list(tracker.events))[:15]:
#             if event.get("event") == "user":
#                 messages.append(event.get("text"))
#
#         movie = messages[-3]
#         print(movie)
#         seat = messages[-2]
#         print(seat)
#         total = messages[-1]
#
#         print(total,movie,seat)
#
#         step1 = movie[movie["Movie"]==movie]
#         step2 = step1[step1["Seat"]==seat]["Price"]
#
#         Amount = int(step2.iloc[0]*total)
#
#         msg = f"Your {total} Tickets total amount is {Amount}"
#
#         dispatcher.utter_message(text = msg)
#
#         return []
