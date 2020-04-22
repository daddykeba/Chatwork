# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
import requests
import time
import re
from typing import Any, Text, Dict, List, Union
from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import UserUtteranceReverted, SlotSet, SessionStarted, ActionExecuted, EventType

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_iamabot")
        dispatcher.utter_message(template="utter_menu_general")

        return [UserUtteranceReverted()]

class MyFallbackAction(Action):

    def name(self) -> Text:
        return "my_fallback_action"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_ask_rephrase")

        return []


class ActionAffirm(Action):

    def name(self) -> Text:
        return "action_affirm"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_concours")
        return [SlotSet("path","ena")]

class ActionConcoursDa(Action):

    def name(self) -> Text:
        return "action_concours_da"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        concoursAll = tracker.get_slot("concoursAll")

        if (concoursAll == 'direct a' or concoursAll == "cycle a"):
            dispatcher.utter_message(template="utter_concoursDA")
            return [SlotSet("path","ena"),SlotSet("concoursAll","direct a")]
        if (concoursAll == 'direct b' or concoursAll == "cycle b"):
            dispatcher.utter_message(template="utter_concoursDB")
            return [SlotSet("path", "ena"), SlotSet("concoursAll", "direct b")]
        if (concoursAll == 'professionnel a'):
            dispatcher.utter_message(template="utter_concoursPA")
            return [SlotSet("path","ena"),SlotSet("concoursAll","professionnel a")]
        if (concoursAll == 'professionnel b'):
            dispatcher.utter_message(template="utter_concoursPB")
            return [SlotSet("path", "ena"), SlotSet("concoursAll", "professionnel b")]

class ActionSetPath(Action):

    def name(self) -> Text:
        return "action_set_path"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain):
        lastMessage = tracker.latest_message['text']
        if lastMessage =='/help':
            return [SlotSet("path", "teledac")]


class ActionPath(Action):

    def name(self) -> Text:
        return "action_path"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path=='ena' or path=='concours'):
            dispatcher.utter_message(template="utter_concours")
            return [SlotSet("path", "ena")]
        if(path=='teledac' or path=='None'):
            dispatcher.utter_message(template="utter_other_faq")
            return [SlotSet("path", "teledac")]

class ActionInscription(Action):

    def name(self) -> Text:
        return "action_inscription"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        inscrire = tracker.get_slot("inscrire")
        concoursAll = tracker.get_slot("concoursAll")
        path = tracker.get_slot("path")

        if(inscrire!='None' and path=='teledac'):
            dispatcher.utter_message(template="utter_inscription_ena")
            return [SlotSet("path", "teledac")]
        if(inscrire != 'None' and path == 'ena'):
            dispatcher.utter_message(template="utter_incrire_ena")
            return [SlotSet("path", "ena")]
        if(inscrire != 'None' and path == 'ena' and concoursAll == 'direct a'):
            dispatcher.utter_message(template="uttter_inscriptionDA")
            return [SlotSet("path", "ena")]
        if(inscrire!='None' and path=='None'):
            dispatcher.utter_message(template="utter_menu_inscription")

class ActionInscriptionTeledac(Action):

    def name(self) -> Text:
        return "action_inscription_teledac"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_inscription_info")
            return [SlotSet("path", "teledac"), SlotSet("open", None)]
        if(path == 'ena' or path =='concours'):
            dispatcher.utter_message(template="utter_incrire_ena")
            return [SlotSet("path", "ena"), SlotSet("open", None)]

class ActionChoiceProfile(Action):

    def name(self) -> Text:
        return "action_choice_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_choice_profil_teledac")
            return [SlotSet("path", "teledac")]
        if(path == 'ena' or path =='concours'):
            dispatcher.utter_message(template="utter_choice_profil_ena")
            return [SlotSet("path", "ena")]

class ActionProfile(Action):

    def name(self) -> Text:
        return "action_profile"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_ask_profile")
            return [SlotSet("path", "teledac"), SlotSet("modifie", None)]
        if (path =='ena' or path=='concours'):
            dispatcher.utter_message(template="utter_profile_ena")
            return [SlotSet("path", "ena"), SlotSet("modifie", None)]

class ActionPassword(Action):

    def name(self) -> Text:
        return "action_password"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_ask_passwd")
            return [SlotSet("modifie", None)]
        if (path =='ena' or path=='concours'):
            dispatcher.utter_message(template="utter_mdp_ena")
            return [SlotSet("path", "ena"), SlotSet("modifie", None)]

class ActionConnexion(Action):

    def name(self) -> Text:
        return "action_connexion"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_connexion_teledac")
            return [SlotSet("path", "teledac")]
        if (path =='ena' or path=='concours'):
            dispatcher.utter_message(template="utter_connexion_ena")
            return [SlotSet("path", "ena")]

class ActionMail(Action):

    def name(self) -> Text:
        return "action_mail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        path = tracker.get_slot("path")

        if(path == 'teledac'):
            dispatcher.utter_message(template="utter_mail_teledac")
            return [SlotSet("path", "teledac")]
        if (path =='ena' or path=='concours'):
            dispatcher.utter_message(template="utter_mail_ena")
            return [SlotSet("path", "ena")]


class ActionInscriptionEnaMenu(Action):

    def name(self) -> Text:
        return "action_inscription_ena_menu"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_incrire_ena")
        return [SlotSet("path", "ena")]

class ActionInscriptionEna(Action):

    def name(self) -> Text:
        return "action_inscription_ena"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_path = ['ena', 'concours']
        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']


        inscrire = tracker.get_slot("inscrire")
        concoursAll = tracker.get_slot("concoursAll")
        path = tracker.get_slot("path")

        if (inscrire != 'None' and path in list_path and concoursAll in list_da):
            dispatcher.utter_message(template="uttter_inscriptionDA")
            return [SlotSet("path", "ena")]
        if (inscrire != 'None' and path in list_path and concoursAll in list_db):
            dispatcher.utter_message(template="uttter_inscriptionDB")
            return [SlotSet("path", "ena")]
        if (inscrire != 'None' and path in list_path and concoursAll == 'professionnel a'):
            dispatcher.utter_message(template="uttter_inscriptionPA")
            return [SlotSet("path", "ena")]
        if (inscrire != 'None' and path in list_path and concoursAll == 'professionnel b'):
            dispatcher.utter_message(template="uttter_inscriptionPB")
            return [SlotSet("path", "ena")]

class ActionPay(Action):

    def name(self) -> Text:
        return "action_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_path = ['ena', 'concours']
        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']

        concoursAll = tracker.get_slot("concoursAll")
        path = tracker.get_slot("path")
        pay = tracker.get_slot("pay")

        if(concoursAll in list_da and path in list_path):
            dispatcher.utter_message(template="utter_payDA")
            return [SlotSet("path", "ena")]
        if (concoursAll in list_db and path in list_path):
            dispatcher.utter_message(template="utter_payDB")
            return [SlotSet("path", "ena")]
        if (concoursAll =='professionnel a' and path in list_path):
            dispatcher.utter_message(template="utter_payPA")
            return [SlotSet("path", "ena")]
        if (concoursAll =='professionnel b' and path in list_path):
            dispatcher.utter_message(template="utter_payPB")
            return [SlotSet("path", "ena")]

class ActionRequire(Action):

    def name(self) -> Text:
        return "action_require"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_path = ['ena', 'concours']
        list_da = ['direct a', 'cycle a']
        list_db = ['direct b', 'cycle b']

        concoursAll = tracker.get_slot("concoursAll")
        path = tracker.get_slot("path")
        requirement = tracker.get_slot("requirement")

        if(concoursAll in list_da and path in list_path):
            dispatcher.utter_message(template="utter_requireDA")
            return [SlotSet("path", "ena")]
        if (concoursAll in list_db and path in list_path):
            dispatcher.utter_message(template="utter_requireDB")
            return [SlotSet("path", "ena")]
        if (concoursAll =='professionnel a' and path in list_path):
            dispatcher.utter_message(template="utter_requirePA")
            return [SlotSet("path", "ena")]
        if (concoursAll =='professionnel b' and path in list_path):
            dispatcher.utter_message(template="utter_requirePB")
            return [SlotSet("path", "ena")]

class ActionInscriptionCheck(Action):

    def name(self) -> Text:
        return "action_inscription_check"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_menu_inscription")

class FindFolderForm(FormAction):

    def name(self) -> Text:
        return "find_folder_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["prenom_nom", "num_dossier", "email", "num_tel"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "prenom_nom": [self.from_entity(entity="prenom_nom"), self.from_text(not_intent=["deny","stop","affirm"])],
            "num_dossier": [self.from_entity(entity="num_dossier"), self.from_text(not_intent=["deny", "stop","affirm"])],
            "email": [self.from_entity(entity="email"), self.from_text(not_intent=["deny", "stop","affirm"])],
            "num_tel": [self.from_entity(entity="num_tel"), self.from_text(not_intent=["deny", "stop","affirm"])],
        }


    def validate_num_dossier(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> Dict[Text, Any]:

        base_url = "http://localhost:8084/referentiel-botdossier/dossier/bot/{refDos}"
        url = base_url.format(**{'refDos': value})
        # http://horoscope-api.herokuapp.com/horoscope/today/capricorn
        res = requests.get(url)
        num = res.json()['message']

        if (num == "Disponible"):
            return {"num_dossier": value}
        else:
            dispatcher.utter_message(text="Votre numéro de dossier est invalide")
            return {"num_dossier": None}

    def validate_email(self, value: Text, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any], ) -> Dict[Text, Any]:
        """Validate email value."""


        if re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", value):
            return {"email": value}
        else:
            dispatcher.utter_message(text="L'email saisi est invalide")
            return {"email": None}

    def validate_num_tel(self,value: Text,dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any],) -> Dict[Text, Any]:
        """Validate numéro de téléphone value."""
        if re.match("^7[0-9]{8}$", value) or re.match("^7[0-9]{1} [0-9]{3} [0-9]{2} [0-9]{2}$", value) or re.match("^7[0-9]{1} [0-9]{3} [0-9]{2}[0-9]{2}$", value):
            # validation succeeded, set the value of the "num_tel" slot to value
            return {"num_tel": value}
        else:
            dispatcher.utter_message(text="La numéro de téléphone saisie est invalide")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"num_tel": None}


    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ## type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
        prenomNom = tracker.get_slot("prenom_nom")
        numDossier = tracker.get_slot("num_dossier")
        email = tracker.get_slot("email")
        numTel = tracker.get_slot("num_tel")

        base_url = "http://localhost:8084/referentiel-botdossier/dossier/{refDos}/{emailDos}/{telMobileDos}"
        url = base_url.format(**{'refDos':numDossier,'emailDos':email,'telMobileDos':numTel})
        # http://horoscope-api.herokuapp.com/horoscope/today/capricorn
        res = requests.get(url)
        state = res.json()['message']
        if state != "Incorrect":
            response = "{}, votre dossier {} est {}".format(prenomNom,numDossier,state.lower())
            dispatcher.utter_message(response)
            dispatcher.utter_message(template="utter_call_back")
        else:
            response = "{}, les informations que vous avez saisi sont incorrectes ".format(prenomNom)
            dispatcher.utter_message(response)
            dispatcher.utter_message(text="Réssayer à nouveau en reprenant votre question")

        return [ SlotSet("prenom_nom",None),SlotSet("num_dossier",None),SlotSet("email",None),SlotSet("num_tel",None)]