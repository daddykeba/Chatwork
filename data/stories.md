## default story
* out_of_scope
  - action_hello_world

## greet
* greet
  - utter_greet
  
## goodby
* goodbye
  - utter_goodbye
  
## greetgoodby
* greet
  - utter_greet
* goodbye
  - utter_goodbye
  
## inscription
* greet
  - utter_greet
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac

## inscription1
* greet
  - utter_greet
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac
* goodbye
  - utter_goodbye
  
## inscription2
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac
* goodbye
  - utter_goodbye
  
## inscription3
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac
  
## inscription4
* inscription{"path":"ena", "inscrire":"inscrire"}
  - action_inscription_teledac
  
## inscription5
* inscription{"path":"ena", "inscrire":"inscrire"}
  - action_inscription_teledac
* goodbye
  - utter_goodbye
  
## inscription6
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire"}
  - action_inscription_teledac
* goodbye
  - utter_goodbye

## inscription7
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire"}
  - action_inscription_teledac

## inscription-7  
* inscription{"path":"ena", "inscrire":"compte", "open":"creer"}
  - action_inscription_teledac
  
## inscription-7-1  
* inscription{"path":"teledac", "inscrire":"compte", "open":"creer"}
  - action_inscription_teledac
  
## inscription-7-2
* inscription{"inscrire":"compte", "open":"creer"}
  - action_inscription_check
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac
  
## inscription-7-3
* inscription{"inscrire":"compte", "open":"creer"}
  - action_inscription_check
* menu_inscrire_ena
  - utter_incrire_ena
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription8
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription9
* inscription{"path":"ena", "inscrire":"inscription", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription10
* inscription{"path":"ena", "inscrire":"compte", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription11
* inscription{"inscrire":"inscrire"}
  - action_inscription_check
* inscription{"path":"teledac", "inscrire":"inscrire"}
  - action_inscription_teledac
  
## inscription12
* inscription{"inscrire":"inscrire"}
  - action_inscription_check
* menu_inscrire_ena
  - utter_incrire_ena
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription13
* inscription{"path":"concours", "inscrire":"compte", "concoursAll":"direct a"}
  - action_inscription_ena
  
## inscription14
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
  
## inscription15
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
  
## inscription16
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
  
## inscription17
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription18
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription19
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription20
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"direct b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription21
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription22
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel a"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription23
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## inscription24
* greet
  - utter_greet
* inscription{"path":"ena", "inscrire":"inscrire", "concoursAll":"professionnel b"}
  - action_inscription_ena
* pay_concours{"pay":"frais"}
  - action_pay
  
## pay  
* pay_concours{"pay":"frais", "path":"concours"}
  - utter_pay_ena

## pay-1  
* pay_concours{"pay":"frais", "path":"ena"}
  - utter_pay_ena

## pay1
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct a"}
  - action_pay
  
## pay5
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct a"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay12
* greet
  - utter_greet
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct a"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay2  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct b"}
  - action_pay
  
## pay6  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct b"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay11
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"direct b"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay3  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel a"}
  - action_pay
  
## pay7  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel a"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay10
* greet
  - utter_greet  
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel a"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay4 
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel b"}
  - action_pay
  
## pay8 
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel b"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay9
* greet
  - utter_greet 
* pay_concours{"pay":"frais", "path":"ena", "concoursAll":"professionnel b"}
  - action_pay
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require  
* requirement_concours{"requirement":"conditions", "path":"concours"}
  - utter_require_ena

## require-1  
* requirement_concours{"requirement":"conditions", "path":"ena"}
  - utter_require_ena
  
## require1
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct a"}
  - action_require
  
## require5
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct a"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## pay12
* greet
  - utter_greet
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct a"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require2  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct b"}
  - action_require
  
## require6  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct b"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require11
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"direct b"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require3  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel a"}
  - action_require
  
## require7  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel a"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require10
* greet
  - utter_greet  
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel a"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require4 
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel b"}
  - action_require
  
## require8 
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel b"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## require9
* greet
  - utter_greet 
* requirement_concours{"requirement":"conditions", "path":"ena", "concoursAll":"professionnel b"}
  - action_require
* inscription{"inscrire":"inscrire"}
  - action_inscription_ena
  
## login
* greet
  - utter_greet
* login
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye

## login1
* greet
  - utter_greet
* login
  - utter_ask_login
  - utter_call_back
  
## login2
* login
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye
  
## login3
* login
  - utter_ask_login
  - utter_call_back
  
## mdp
* mdp{"path":"teledac", "modifie":"modifier", "password":"mot de passe"}
  - action_password
  
## mdp1
* mdp{"path":"ena", "modifie":"modifier", "password":"mot de passe"}
  - action_password
  
## mdp2
* mdp{"modifie":"modifier", "password":"mot de passe"}
  - utter_menu_mdp
* mdp{"path":"teledac", "modifie":"modifier", "password":"mot de passe"}
  - action_password
  
## mdp3
* mdp{"modifie":"modifier", "password":"mot de passe"}
  - utter_menu_mdp
* mdp{"path":"ena", "modifie":"modifier", "password":"mot de passe"}
  - action_password
   
## mdp4
* profile{"modifie":"modifier", "path":"teledac"}
  - action_choice_profile
* mdp{"path":"teledac", "modifie":"modifier", "password":"mot de passe"}
  - action_password
  
## mdp5
* profile{"modifie":"modifier", "path":"ena"}
  - action_choice_profile
* mdp{"path":"ena", "modifie":"modifier", "password":"mot de passe"}
  - action_password
  
## profile
* profile{"path":"teledac", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile1
* profile{"path":"ena", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile2
* profile{"path":"teledac", "modifie":"modifier", "attributeProfile":"nom"}
  - action_profile
  
## profile3
* profile{"path":"ena", "modifie":"modifier", "attributeProfile":"nom"}
  - action_profile
  
## profile4
* profile{"modifie":"modifier", "profile":"profil"}
  - utter_menu_profile
* profile{"path":"teledac", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile5
* profile{"modifie":"modifier", "profile":"profil"}
  - utter_menu_profile
* profile{"path":"ena", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile6
* profile{"modifie":"erreur", "attributeProfile":"prenom"}
  - utter_menu_profile
* profile{"path":"teledac", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile7
* profile{"modifie":"erreur", "attributeProfile":"prenom"}
  - utter_menu_profile
* profile{"path":"ena", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile8
* profile{"modifie":"modifier"}
  - utter_choice_plateform
* profile{"path":"teledac", "modifie":"modifier"}
  - action_choice_profile
* profile{"path":"teledac", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile9
* profile{"modifie":"modifier"}
  - utter_choice_plateform
* profile{"path":"ena", "modifie":"modifier"}
  - action_choice_profile
* profile{"path":"ena", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile10
* profile{"modifie":"modifier", "path":"teledac"}
  - action_choice_profile
* profile{"path":"teledac", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## profile11
* profile{"modifie":"modifier", "path":"ena"}
  - action_choice_profile
* profile{"path":"ena", "modifie":"modifier", "profile":"profil"}
  - action_profile
  
## mailconfirm
* confirmMail{"path":"teledac", "inscrire":"inscription", "mail":"mail de confirmation"}
  - action_mail
  
## mailconfirm1
* confirmMail{"path":"ena", "inscrire":"inscription", "mail":"mail de confirmation"}
  - action_mail
  
## mailconfirm2  
* confirmMail{"inscrire":"compte", "mail":"activer"}
  - utter_plateforme_mailconfirm
* confirmMail{"path":"teledac", "inscrire":"inscription", "mail":"mail de confirmation"}
  - action_mail

## mailconfirm3  
* confirmMail{"inscrire":"compte", "mail":"activer"}
  - utter_plateforme_mailconfirm
* confirmMail{"path":"ena", "inscrire":"inscription", "mail":"mail de confirmation"}
  - action_mail
  
## mailconfirm4  
* confirmMail{"mail":"mail de confirmation"}
  - utter_plateforme_mailconfirm
* confirmMail{"path":"teledac", "inscrire":"compte", "connexions":"connecter"}
  - action_mail
  
## mailconfirm5  
* confirmMail{"mail":"mail de confirmation"}
  - utter_plateforme_mailconfirm
* confirmMail{"path":"ena", "inscrire":"compte", "connexions":"connecter"}
  - action_mail
  
## mailconfirm6
* confirmMail{"path":"teledac", "mail":"mail de confirmation"}
  - action_mail
  
## mailconfirm7
* confirmMail{"path":"ena", "mail":"mail de confirmation"}
  - action_mail
  
## connexion
* connexion{"path":"teledac", "inscrire":"compte", "mail":"mail de confirmation"}
  - action_connexion
  
## connexion1
* connexion{"path":"ena", "inscrire":"compte", "connexions":"connecter"}
  - action_connexion
  
## connexion2  
* connexion{"inscrire":"compte", "connexions":"connecter"}
  - utter_plateforme_connexion
* connexion{"path":"teledac", "inscrire":"compte", "connexions":"connecter"}
  - action_connexion

## connexion3  
* connexion{"inscrire":"compte", "connexions":"connecter"}
  - utter_plateforme_connexion
* connexion{"path":"ena", "inscrire":"compte", "connexions":"connecter"}
  - action_connexion
  
## connexion4  
* connexion{"connexions":"connecter"}
  - utter_plateforme_connexion
* connexion{"path":"teledac", "inscrire":"compte", "connexions":"connecter"}
  - action_connexion
  
## connexion5  
* connexion{"connexions":"connecter"}
  - utter_plateforme_connexion
* connexion{"path":"ena", "inscrire":"compte", "connexions":"connecter"}
  - action_connexion
  
## connexion6
* connexion{"path":"teledac", "connexions":"connecter"}
  - action_connexion
  
## connexion7
* connexion{"path":"ena", "connexions":"connecter"}
  - action_connexion
  

## login_connexion
* greet
  - utter_greet
* connexion
  - utter_ask_connexion
  - utter_call_back
* login
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye 
  
## login_connexion1
* greet
  - utter_greet
* connexion
  - utter_ask_connexion
  - utter_call_back
* login
  - utter_ask_login
  - utter_call_back

## login_connexion2
* connexion
  - utter_ask_connexion  
  - utter_call_back
* login
  - utter_ask_login
  - utter_call_back
* goodbye
  - utter_goodbye
  
## login_connexion3
* connexion
  - utter_ask_connexion
  - utter_call_back   
* login
  - utter_ask_login
  - utter_call_back
  
## help
* greet
  - utter_greet
* help
  - action_set_path
  - utter_other_faq
* goodbye
  - utter_goodbye
  
## help1
* greet
  - utter_greet
* help
  - action_set_path
  - utter_other_faq
  
## help2  
* help
  - action_set_path
  - utter_other_faq
* goodbye
  - utter_goodbye
  
## help3  
* help
  - action_set_path
  - utter_other_faq
  
## retrieve folder status
* greet
  - utter_greet
* statusFolder
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
  - utter_call_back
  - form{"name": null}
* goodbye
  - utter_goodbye
  
## retrieve folder status 1
* greet
  - utter_greet
* statusFolder
  - utter_process_status
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
  - utter_call_back
  - form{"name": null}
  
## retrieve folder status 2
* statusFolder
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
  - utter_call_back
  - form{"name": null}
* goodbye
  - utter_goodbye
  
## retrieve folder status 3
* statusFolder
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
* statusFolder
  - find_folder_form
  - utter_call_back
  - form{"name": null}
  
## deactive_form
* greet
  - utter_greet
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back
  
## deactive_form_1
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back
  
## deactive_form_2
* greet
  - utter_greet
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"prenom_nom": "keba"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "776342517"}
  - form{"name": null}
  - utter_call_back
  
## deactive_form_3
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"prenom_nom": "keba"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "776342517"}
  - form{"name": null}
  - utter_call_back
  
## deactive_form_4
* greet
  - utter_greet 
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back
 
## deactive_form_5 
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back

## deactive_form_6
* greet
  - utter_greet  
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
  - form{"name": null}
  - utter_call_back  

## deactive_form_7  
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
  - form{"name": null}
  - utter_call_back

## deactive_form_8
* greet
  - utter_greet  
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back  
  
## deactive_form_9  
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back
  
## deactive_form_10
* greet
  - utter_greet
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}  
  - form{"name": null}
  - utter_call_back
  
## deactive_form_11
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}  
  - form{"name": null}
  - utter_call_back
  
## deactive_form_12
* greet
  - utter_greet
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back

## deactive_form_13 
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
* stop
  - utter_ask_continue
* deny
  - action_deactivate_form
  - form{"name": null}
  - utter_call_back

## deactive_form_14  
* greet
  - utter_greet
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"num_tel": "773842637"}  
  - form{"name": null}
  - utter_call_back  
  
## deactive_form_15  
* statusFolder{"state": "état"}
  - slot{"state": "état"}
  - utter_process_status
  - find_folder_form
  - form{"name": "find_folder_form"}
  - slot{"requested_slot": "prenom_nom"}
* statusFolder
  - find_folder_form
  - slot{"num_dossier": "20140326-DK0035"}
* statusFolder
  - find_folder_form
  - slot{"email": "contact@onclickgaming.com"}
* statusFolder
  - find_folder_form
  - slot{"num_tel": "773842637"}
* stop
  - utter_ask_continue
* affirm
  - find_folder_form
  - slot{"num_tel": "773842637"}  
  - form{"name": null}
  - utter_call_back 
    
## stop
* stop
  - utter_ask_continue  
*deny
 - utter_call_back
  
## stop1
* stop
  - utter_ask_continue  
*affirm
 - utter_call_back
 
## chat     
* chat
   - respond_chat
   - utter_call_back
   
## get_concours_4
* get_path
  - action_path
   
## get_concours_5
* get_path{"path":"concours"}
  - action_path
  
## get_concours_6
* get_path{"path":"ena"}
  - action_path
  
## get_concours_7
* get_path{"path":"teledac"}
  - action_path
  
## get_concours_all
* get_concours_all{"concoursAll":"direct a"}
  - action_concours_da
  - utter_admis
  
## get_concours_all_1
* get_concours_all{"concoursAll":"direct b"}
  - action_concours_da
  - utter_admis
  
## get_concours_all_2
* get_concours_all{"concoursAll":"professionnel a"}
  - action_concours_da
  - utter_admis
  
## get_concours_all_3
* get_concours_all{"concoursAll":"professionnel b"}
  - action_concours_da
  - utter_admis
   
