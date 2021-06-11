# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from rasa_sdk import Action


class BuyHomeForm(FormAction):
 def name(self):
  return "buy_form"

 def required_slots(self,tracker) -> List[Text]:
  return ["country","cost","bedrooms","bathrooms","months","property_type","email"]
 def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	return {
            "country": [
                self.from_text(),
            ],
            "cost": [
                self.from_text(),
            ],
            
            "bedrooms": [
                self.from_text(),
            ],
            "bathrooms": [
                self.from_text(),
            ],
            "months": [
                self.from_text(),
            ],
            "property_type": [
                self.from_text(),
            ],
            "email": [
                self.from_text(),
            ],
        }
 def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_template("utter_thanks", tracker)    
    return []

 class rentHomeForm(FormAction):
  def name(self):
   return "rent_form"

  def required_slots(self,tracker) -> List[Text]:
   return ["time_to_rent","city","email","phone_number"]
  def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	 return {
             "time_to_rent": [
                 self.from_text(),
             ],
             "city": [
                 self.from_text(),
             ],
             "zipcode": [
                 self.from_text(),
             ],
             "email": [
                 self.from_text(),
             ],
             "phone_number": [
                 self.from_text(),
             ],
         }   
  def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_template("utter_thanks", tracker)    
    return []


class contactUsForm(FormAction):
  def name(self):
   return "contact_form"

  def required_slots(self,tracker) -> List[Text]:
   return ["name","complain","email","phone_number"]
  def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
 	 return {
             "name": [
                 self.from_text(),
             ],
             "phone_number": [
                 self.from_text(),
             ],
             "email": [
                 self.from_text(),
             ],
             "complain": [
                 self.from_text(),
             ],
         }   

         
  def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
    dispatcher.utter_template("utter_thanks", tracker)    
    return []
