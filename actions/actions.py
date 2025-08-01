# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import datetime

class ActionTellTime(Action):
    def name(self) -> Text:
        return "action_tell_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        now = datetime.datetime.now().strftime("%I:%M %p")
        dispatcher.utter_message(text=f"Abhi ka time hai {now}")
        return []

class ActionTellDay(Action):
    def name(self) -> Text:
        return "action_tell_day"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        today = datetime.datetime.now().strftime("%A")
        dispatcher.utter_message(text=f"Aaj {today} hai.")
        return []

class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Maaf kijiye, mujhe yeh baat samajh nahi aayi. Kya aap dobara kehna chahenge?")
        return []

