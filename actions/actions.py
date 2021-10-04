# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa.shared.core.trackers import DialogueStateTracker, EventVerbosity
import requests
import json
import logging
logger = logging.getLogger(__name__)

#
#
class ActSearchModel(Action):
#
     def name(self) -> Text:
         return "act_search_model"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         """
         for key, value in tracker.slots.items():
             slot_value = value
         logger.debug(str(tracker.latest_message['entities']))
         if('model' in tracker.slots ):
             response = requests.get('https://apidonexp-vc5xcezzwa-uc.a.run.app/api/products/model/'+str(tracker.slots['model']))
             dispatcher.utter_message(text= response.json()['description'])
         else:
             dispatcher.utter_message(text= 'model not found')
         """
         entities={}
         for each in tracker.latest_message['entities']:
             entities[each['entity']]= each['value']
         if(len(entities)>0):
             json_data = json.dumps(entities)
             logger.debug(json_data)
             response = requests.post('https://apidonexp-vc5xcezzwa-uc.a.run.app/api/products/search', json = entities)
             logger.debug(response.json())
             if(len(response.json())>0):
                 dispatcher.utter_message(json_message= response.json())
             else:
                 dispatcher.utter_message(text= 'model not found')
         else:
             dispatcher.utter_message(text= 'model not found')
         return []
     
        
        
     
class ActSearchInfo(Action):
#
     def name(self) -> Text:
         return "act_search_info"
#
     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         """
         for key, value in tracker.slots.items():
             slot_value = value
         logger.debug(str(tracker.latest_message['entities']))
         if('model' in tracker.slots ):
             response = requests.get('https://apidonexp-vc5xcezzwa-uc.a.run.app/api/products/model/'+str(tracker.slots['model']))
             dispatcher.utter_message(text= response.json()['description'])
         else:
             dispatcher.utter_message(text= 'model not found')
         """
         entities={}
         for each in tracker.latest_message['entities']:
             entities[each['entity']]= each['value']
         if(len(entities)>0):
             json_data = json.dumps(entities)
             logger.debug(json_data)
             response = requests.post('https://apidonexp-vc5xcezzwa-uc.a.run.app/api/products/search', json = entities)
             logger.debug(response.json())
             if(len(response.json())>0):
                 dispatcher.utter_message(json_message= response.json())
             else:
                 dispatcher.utter_message(text= 'model not found')
         else:
             dispatcher.utter_message(text= 'model not found')
         return []
     