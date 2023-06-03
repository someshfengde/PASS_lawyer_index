import streamlit as st 
from streamlit_chat import message 
import openai 
from nanoid import generate # unique ids for every messages.
import requests 


def structurize_message(message_ , is_user):
    return {"role": "user" if is_user else "assistant", "content": message_}

def get_response(messages , model):
    messages = "\n".join([message["content"] for message in messages])
    resp = requests.get("https://ed1d-2a09-bac5-3afb-18d2-00-279-32.ap.ngrok.io/query", params={"search": messages})
    # print(resp.text)
    new_data = {
            "docs": [
                {
                "pageContent": " if such person is found to\nhave directly or indirectly attempted to indulge or knowingly assisted or knowingly is\na party or is actually involved in one or more of the following processes or activities\nconnected with proceeds of crime, namely: —\n(a) concealment; or\n(b) possession; or\n(c) acquisition; or\nDirectorate Of Enforcement vs Padmanabhan Kishore on 31 October, 2022\nIndian Kanoon - http://indiankanoon.org/doc/58987970/\n3\n\f(d) use; or\n(e) projecting as untainted property; or\n(f) claiming as untainted property, in any manner whatsoever;\n(ii) the process or activity connected with proceeds of crime is a continuing activity\nand continues till such time a person is directly or indirectly enjoying the proceeds of\ncrime by its concealment or possession or acquisition or use or projecting it as\nuntainted property or claiming it as untainted property in any manner whatsoever.\n4. Punishment for money-laundering.— Whoever commits the offence of money-laundering shall be\npunishable with rigorous imprisonment for a term which shall not be less than three years but which\nmay extend to seven years and shall also be liable to fine: Provided that where the proceeds of crime\ninvolved in money-laundering relates to any offence specified under paragraph 2 of Part A of the\nSchedule, the provisions of this section shall have effect as if for the words “which may extend to\nseven years”, the words “which may extend to ten years” had been substituted.”\n11. Paragraph 8 of the Part-A of the Schedule to the PML Act deals with offences under the PC Act\nand said paragraph is to the following effect: -\n“PARAGRAPH 8 OFFENCES UNDER THE PREVENTION OF CORRUPTION ACT,\n1988 (49 of 1988) Section Description of offence\n7. Offence",
                "metadata": {
                    "id": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore-5",
                    "case_name": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore",
                    "case_date": "31_October_2022.PD"
                }
                },
                {
                "pageContent": " the offence of money laundering is independent of the\nschedule offence because the PMLA deals with the process or activity with respect to the proceeds of\ncrime including concealment, possession, acquisition or use, however in the light of the explanation\nof Section 44(1) of PMLA, the argument of the appellant was repelled. The High Court further held\nthat if any observation has come in the bail application, having no material to connect with the\ncommission of any offence, would not be enough to quash the proceedings. The Court relied upon\nthe seizure made by the I.T. Department including that of the currency notes of denomination of Rs.\n2000 in the context that the currency notes of denomination of Rs. 500 and Rs. 1000 ceased to be\nlegal tender by order of the Government at the time of demonetization and the people were in queue\nto exchange those old currency notes for new ones. As the seizure of currency notes of Rs. 33 crores\nin the denomination of Rs. 2000 was made, therefore, the closure report made by Central Bureau\nJ. Sekar @ Sekar Reddy vs Directorate Of Enforcement on 5 May, 2022\nIndian Kanoon - http://indiankanoon.org/doc/166692106/\n1\n\fInvestigation (in short ‘CBI’) in schedule offence cannot be relied upon.\n2. Briefly, the facts relevant for the purpose of the appeal are that the appellant J. Sekar Reddy is the\nManaging Partner of M/s SRS Mining which is a partnership firm engaged in sand mining since\n2013 and he had deposited Rs 312.64 Crores in three bank accounts of the firm. On 08.12.2016 and\n09.12.2016, the Income Tax Department, Chennai (for short “I.T. Department”) conducted search in\nthe official/commercial premises of the appellant",
                "metadata": {
                    "id": "J_Sekar_Sekar_Reddy_vs_Directorate_Of_Enforcement-1",
                    "case_name": "J_Sekar_Sekar_Reddy_vs_Directorate_Of_Enforcement",
                    "case_date": "5_May_2022.PD"
                }
                },
                {
                "pageContent": " of offence of\nmoney- laundering. If the statement made by him reveals the offence of money-laundering or the\nexistence of proceeds of crime, that becomes actionable under the Act itself. To put it differently, at\nthe stage of recording of statement for the purpose of inquiring into the relevant facts in connection\nwith the property being proceeds of crime is, in that sense, not an investigation for prosecution as\nsuch;\nSignature Not Verified ARORA Signing Date:08.02.2023 12:07:41 and in any case, there would be\nno formal accusation against the noticee. Such summons can be issued even to witnesses in the\ninquiry so conducted by the authorised officials. However, after further inquiry on the basis of other\nmaterial and evidence, the involvement of such person (noticee) is revealed, the authorised officials\ncan certainly proceed against him for his acts of commission or omission. In such a situation, at the\nstage of issue of summons, the person cannot claim protection under Article 20(3) of the\nConstitution. However, if his/her statement is recorded after a formal arrest by the ED official, the\nconsequences of Article 20(3) or Section 25 of the Evidence Act may come into play to urge that the\nsame being in the nature of confession, shall not be proved against him. Further, it would not\npreclude the prosecution from proceeding against such a person including for consequences under\nSection 63 of the 2002 Act on the basis of other tangible material to indicate the falsity of his claim.\nRaman Bhuraria vs Directorate Of Enforcement on 8 February, 2023\nIndian Kanoon - http://indiankanoon.org/doc/62003795/\n18\n\fThat would be a matter of rule of evidence.\n444. ..The third aspect which had weighed with the Court in Tofan Singh692 is that the police officer",
                "metadata": {
                    "id": "Raman_Bhuraria_vs_Directorate_Of_Enforcement-36",
                    "case_name": "Raman_Bhuraria_vs_Directorate_Of_Enforcement",
                    "case_date": "8_February_2023.PD"
                }
                },
                {
                "pageContent": " to offence mentioned in said paragraph 8 of Part-A of the Schedule would certainly be\n“proceeds of crime”.\n14. The further question to be answered is: whether the role played by respondent could come\nwithin the purview of Section 3 of the PML Act?\n15. Said Section 3 states, inter alia, that whoever knowingly assists or knowingly is a party or is\nactually involved in any process or activity connected with proceeds of crime including its\nconcealment, possession, acquisition or use shall be guilty of offence of money-laundering\n(emphasis added by us).\n16. It is true that so long as the amount is in the hands of a bribe giver, and till it does not get\nimpressed with the requisite intent and is actually handed over as a bribe, it would definitely be\nuntainted money. If the money is handed over without such intent, it would be a mere entrustment.\nIf it is thereafter appropriated by the public servant, the offence would be of misappropriation or\nspecies thereof but certainly not of bribe. The crucial part therefore is the requisite intent to hand\nover the amount as bribe and normally such intent must necessarily be antecedent or prior to the\nmoment the amount is handed over. Thus, the requisite intent would always be at the core before\nthe amount is handed over. Such intent having been entertained well before the amount is actually\nhanded over, the person concerned would certainly be involved in the process or activity connected\nwith “proceeds of crime” including inter alia, the aspects of possession or acquisition thereof. By\nhanding over money with the intent of giving bribe, such person will be assisting or will knowingly\nbe a party to an activity connected with the proceeds of crime. Without such active participation on\npart of the person concerned, the money would not assume the character of being proceeds of crime.\nThe relevant expressions",
                "metadata": {
                    "id": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore-7",
                    "case_name": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore",
                    "case_date": "31_October_2022.PD"
                }
                }
            ],
            "response": [
                {
                "argument_res": {
                    "text": "The case involves the Directorate of Enforcement accusing the respondent of involvement in an activity connected with proceeds of crime. The High Court had initially accepted the respondent's submission that they could not be connected with proceeds of crime as the money had assumed the character of being proceeds of crime only after it was received by a public servant. However, the Supreme Court found this to be incorrect and allowed the appeal, stating that the respondent should continue to be proceeded against in accordance with the law in E.C.I.R No. 13 of 2016. The observations made by the court regarding the involvement of the respondent are prima facie in nature, and the matter will be considered purely on merits at the appropriate stages."
                },
                "interpretation_res": {
                    "text": "The appeal challenges the final judgment and order dated 1.3.2021 passed by the High Court of Judicature at Madras in Writ Petition No. 25670/2019. The writ petition was filed by the respondent seeking quashing of proceedings initiated against him under the provisions of the Prevention of Money Laundering Act, 2002 (“PML Act”, for short). It is believed that the respondent was prima facie involved in the activity connected with the proceeds of crime. The view taken by the High Court that the respondent cannot be held liable for the offense under the PML Act is completely incorrect. The appeal is allowed, and the respondent will continue to be arrayed and proceeded against in accordance with ECIR No. 13 of 2016 registered by the Enforcement Directorate. Further, the involvement of the respondent is considered prima facie in nature and will be considered purely on merits at the appropriate stage(s)."
                },
                "articles_res": {
                    "text": "The documents refer to a case of alleged money laundering and corruption involving Padmanabhan Kishore and others. The Enforcement Directorate registered a case and filed a complaint under the Prevention of Money Laundering Act. The respondent allegedly handed over a sum of Rs.50,00,000/- to a public servant, leading to the registration of a crime under the Indian Penal Code and the Prevention of Corruption Act. The respondent's defense was that the money in question was not tainted until it was received by the public servant. The PML Act defines money laundering and provides punishment for the offense. Paragraph 8 of the Part-A of the Schedule to the PML Act deals with offenses under the PC Act."
                },
                "background_res": {
                    "text": "The document is a judgment by the Supreme Court of India regarding a writ petition filed by Padmanabhan Kishore seeking to quash proceedings initiated against him under the Prevention of Money Laundering Act. The court allowed the appeal by the Directorate of Enforcement and set aside the judgment and order passed by the High Court, allowing the respondent to be proceeded against in accordance with the law."
                },
                "clause_res": {
                    "text": "The Supreme Court of India allowed an appeal and set aside the judgment and order passed by the High Court, and the respondent shall continue to be proceeded against in accordance with law in E.C.I.R. No. 13 of 2016 registered by the Enforcement Directorate under the provisions of the Prevention of Money Laundering Act. The respondent was found to be prima facie involved in the activity connected with the proceeds of crime. The observations made by the court regarding involvement of the respondent are prima facie in nature and the matter shall be considered purely on merits at the appropriate stage(s)."
                },
                "points_res": {
                    "text": "The document is a judgement from the Supreme Court of India regarding an appeal by the Directorate of Enforcement against the quashing of proceedings initiated against Padmanabhan Kishore under the Prevention of Money Laundering Act. The court allowed the appeal and set aside the judgement and order passed by the High Court, stating that the respondent shall continue to be proceeded against in accordance with the law."
                },
                "submission_res": {
                    "text": "The document is a judgment from the Supreme Court of India in a criminal appeal case between the Directorate of Enforcement and Padmanabhan Kishore. The appeal challenges the High Court's decision to quash proceedings against the respondent under the Prevention of Money Laundering Act. The High Court accepted the argument that the respondent cannot be said to be connected with proceeds of crime and could not be proceeded against under the PML Act. The Supreme Court heard arguments from both parties and reserved judgment."
                },
                "case": {
                    "date": "31_October_2022.PD",
                    "name": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore"
                }
                },
                {
                "argument_res": {
                    "text": "The documents discuss the quashment of two FIRs and the order of the Adjudicating Authority in relation to an alleged offence under PMLA. The court found that the evidence of continuation of the offence was not sufficient and the chances of proving the allegations in court were bleak. The High Court's findings were set aside and the appeal was allowed. The I.T. Department conducted a search and was satisfied that the cash recovered from the premises was explained and tax was paid. The letter from the I.T. Department is included in the documents."
                },
                "interpretation_res": {
                    "text": "The document discusses legal proceedings and judgments related to a case, including the importance of a certain parameter, the definition of proceeds of crime under PMLA, and the lack of evidence for the schedule offence. The appeal is ultimately allowed and the High Court's order is set-aside."
                },
                "articles_res": {
                    "text": "The IT Department conducted a search in the official and commercial premises of the appellant and others and seized a large amount of currency and gold. The CBI and Enforcement Directorate registered offenses against the appellant and others under various sections of the IPC and PC Act. The ED felt that the provisions under Sections 2(1)(x) and 2(1)(y) of the PMLA would attract. The CBI had filed a custody petition which was dismissed by the Special Court. The Court found that the allegations must be proved beyond reasonable doubt in the court and that the person is innocent until proven guilty. The closure report of the schedule offense in RC MA1 2016 A0040 was accepted and two FIRs were quashed by the High Court."
                },
                "background_res": {
                    "text": "The documents contain legal discussions regarding adjudication proceedings and prosecution related to allegations of contravention of provisions of a certain act. The High Court's order is set aside, and it is concluded that the chances of proving the allegations in court are bleak. Lack of evidence and lack of identity of the source of collected money are mentioned in relation to seizures and possession of property relevant for proceeds of crime."
                },
                "clause_res": {
                    "text": "The documents discuss legal proceedings related to allegations of contravention of provisions of the Act. The Adjudicating Authority found the evidence of continuation of the offense to be insufficient and there was no incriminating material produced to prove the case beyond reasonable doubt. The chance of proving the allegations in court is deemed to be bleak. The High Court's order was set aside, and the chances of conviction in a criminal case are not high. The possession and recovery of seized property must be innocent under PMLA, and the schedule offense has not been made out due to a lack of evidence. The Adjudicating Authority found that the record regarding banks and officials involved in the offense was not on record."
                },
                "points_res": {
                    "text": "There are multiple documents discussing investigations and alleged offenses, including the quashment of FIRs and the insufficient evidence to prove allegations under PMLA. One case involves accusations of causing wrongful loss to the Indian government and obtaining corresponding gain, but there is no substantiated evidence to support prosecution. Another case involves the registration of an ECIR under PMLA and the attachment of property, but the evidence collected does not seem to be enough to prove the alleged offenses beyond reasonable doubt. Overall, it seems that the courts are not convinced of the allegations and the cases have been closed."
                },
                "submission_res": {
                    "text": "The document discusses the quashment of two FIRs by the High Court, the evidence of continuation of offense being insufficient, and the CBI submitting a closure report for lack of sufficient evidence. The court set aside the impugned order passed by the High Court and allowed the appeal. The investigation made by the I.T. Department on the basis of search is closed."
                },
                "case": {
                    "date": "5_May_2022.PD",
                    "name": "J_Sekar_Sekar_Reddy_vs_Directorate_Of_Enforcement"
                }
                },
                {
                "argument_res": {
                    "text": "In the first content, it is mentioned that the Agreement is governed by English law. In the second content, the president did not mention Michael Jackson. The remaining content is about a case where bail is being granted to the petitioners due to the trial likely to take some time, lack of relevant documents, and little scope for the accused to hamper the investigation by influencing witnesses. There is also a mention of the investigation turning towards the role of bank officers in siphoning off bank funds through dummy entities/transactions, but no witness was summoned to investigate the role of the applicant till November 13, 2021."
                },
                "interpretation_res": {
                    "text": "The documents discuss various legal cases and arguments, including the admissibility of statements given voluntarily and the availability of bail for economic offenses. One case involves a decision to grant bail to petitioners due to the documentary nature of evidence and likelihood of a lengthy trial. In another case, the lack of relevant documents to support allegations is noted."
                },
                "articles_res": {
                    "text": "The documents discuss two separate legal cases. One involves a bail grant for two petitioners in a case with evidence primarily consisting of documentary evidence and recorded statements. The other involves an applicant in a case where the evidence consists of five documents that do not show guilt and no satisfactory explanation for the lack of documents pointing to the applicant as the \"mastermind.\" The IO's observation is also considered in determining whether the applicant is prima facie not guilty."
                },
                "background_res": {
                    "text": "The first document discusses the decision to continue day-to-day trial in a case and grant bail to the petitioners due to the primarily documentary nature of evidence. The second document discusses the lack of relevant documents to support allegations of money laundering and the admissibility of statements made under Section 50 of PMLA as evidence. It also mentions retractions of statements made by individuals involved in the case."
                },
                "clause_res": {
                    "text": "The first document discusses the need for a day-to-day trial to continue for a case involving PMLA violations, and grants bail to the petitioners due to the documentary nature of the evidence and the requirement for trials in two separate cases to be held together. The second document discusses the lack of relevant documents to support allegations against an applicant in a case involving SBFL, and the importance of IO observation in determining the applicant's guilt. The document also cites legal precedents related to bail for economic offenses. The third document provides an overview of the PMLA and discusses the importance of bail conditions in cases related to economic offenses."
                },
                "points_res": {
                    "text": "The documents discuss various legal cases relating to charges of money laundering and the admissibility of certain types of evidence in those cases. One case involves the grant of bail to petitioners due to the lengthy trial process, while another case involves the lack of relevant documents to support allegations against an applicant. The admissibility of statements made under Section 50 of PMLA is also discussed, though some of these statements have since been retracted."
                },
                "submission_res": {
                    "text": "The first document is discussing the directions of the Hon'ble Supreme Court regarding a trial and granting bail to petitioners. The second document discusses allegations against an applicant but lacks relevant documents to support them. The third document discusses the admissibility of statements made under Section 50 of PMLA as evidence, but also notes that some of those statements have been retracted."
                },
                "case": {
                    "date": "8_February_2023.PD",
                    "name": "Raman_Bhuraria_vs_Directorate_Of_Enforcement"
                }
                },
                {
                "argument_res": {
                    "text": "The case involves the enforcement of the Prevention of Money Laundering (PML) Act against the respondent, who was allegedly involved in activity connected with the proceeds of crime according to the complaint made by the Enforcement Directorate. The High Court initially accepted the respondent's submission that he could not be said to be connected with proceeds of crime, but this decision was later overturned on appeal by the Supreme Court. The observations made by the Supreme Court regarding the involvement of the respondent were prima facie in nature and the matter will be considered purely on merits at the appropriate stage(s). The appeal was allowed and the respondent shall continue to be proceeded against in accordance with the law."
                },
                "interpretation_res": {
                    "text": "The appeal challenges the final judgment and order passed by the High Court of Judicature at Madras in Writ Petition No. 25670/2019. The writ petition was filed by the respondent seeking quashing of proceedings initiated against him under the provisions of the Prevention of Money Laundering Act, 2002. The complaint made by the Enforcement Directorate showed that the respondent was prima facie involved in the activity connected with the proceeds of crime and thus, the view taken by the High Court that the respondent cannot be held liable for the offense under the PML Act is incorrect. The observations made by the Supreme Court regarding involvement of the respondent are prima facie in nature and need to be considered on merits further. The appeal is allowed and the respondent shall continue to be proceeded against in accordance with the law in E.C.I.R. No. 13 of 2016 registered by the Enforcement Directorate."
                },
                "articles_res": {
                    "text": "The documents relate to a case involving the Prevention of Money Laundering Act and allegations against Padmanabhan Kishore for offenses related to bribery and corruption. The basic argument made on behalf of the respondent is that the money in question was not tainted until it was received by the public servant. The PML Act defines money laundering and specifies punishment for committing the offense. Additionally, paragraph 8 of the Part-A of the Schedule to the PML Act deals with offenses under the Prevention of Corruption Act."
                },
                "background_res": {
                    "text": "The document is a judgment of a criminal appeal case in the Supreme Court of India, where the Directorate of Enforcement appealed against the High Court's judgment to quash proceedings initiated against the respondent under the Prevention of Money Laundering Act. The Supreme Court allowed the appeal, set aside the High Court's judgment, and directed that the respondent continue to be proceeded against in accordance with the law."
                },
                "clause_res": {
                    "text": "The Supreme Court of India allowed an appeal by the Directorate of Enforcement against Padmanabhan Kishore, stating that he can be held liable for an offence under the Prevention of Money Laundering Act and should continue to be proceeded against in accordance with the law. The judgment also stated that the involvement of Padmanabhan Kishore is prima facie in nature and will be considered on merits at the appropriate stage(s)."
                },
                "points_res": {
                    "text": "The document is a judgment from the Supreme Court of India regarding a writ petition seeking quashing of proceedings under the Prevention of Money Laundering Act. The appeal challenges the judgment and order passed by the High Court and was allowed. The respondent shall continue to be arrayed and proceeded against in accordance with law."
                },
                "submission_res": {
                    "text": "The document is a judgment from the Supreme Court of India regarding a writ petition filed by Padmanabhan Kishore seeking the quashing of proceedings initiated against him under the PML Act for his alleged involvement in corrupt activities. The High Court had ruled in favor of Kishore stating that the prosecution against him under the PML Act was misconceived. The Supreme Court heard the appeal challenging the High Court's decision and the judgment was delivered by Hon'ble The Justice Uday Umesh Lalit."
                },
                "case": {
                    "date": "31_October_2022.PD",
                    "name": "Directorate_Of_Enforcement_vs_Padmanabhan_Kishore"
                }
                }
            ]
            }
    # output_data = new_data['response']
    output_data = resp.json()["response"]
    
    formatted_msg = ""
    for msg_data in output_data:
        msg_con = f"ARGUMENT \n \n {msg_data['argument_res']['text']} \n \n INTERPRETATION \n \n {msg_data['interpretation_res']['text']} \n \n ARTICLES \n \n {msg_data['articles_res']['text']} \n \n BACKGROUND \n \n {msg_data['background_res']['text']} \n \n CLAUSE \n \n {msg_data['clause_res']['text']} \n \n POINTS \n \n {msg_data['points_res']['text']} \n \n SUBMISSION \n \n {msg_data['submission_res']['text']} \n \n CASE: {msg_data['case']['name']} \n \n DATE:  {msg_data['case']['date']} \n \n ------------------------------------------------------------------------------------------------------------------------- \n \n "
        formatted_msg += msg_con

    str_msg = structurize_message(formatted_msg, is_user=False)
    return str_msg


def chat_interface(): 
    model = st.selectbox("Select model", ["gpt-3.5-turbo"])
    st.markdown("<h3 style='text-align:center; color:grey;'> New Chat </h3>", unsafe_allow_html= True ) 
    message("Hey there! What question do you have for me?")

    # setting up session state for message history
    if "message_history" not in st.session_state:
        st.session_state.message_history = [] 

    # previous messages
    for message_obj in st.session_state.message_history:
        if message_obj.get("content",False): 
            message(message_obj["content"],is_user=True if message_obj["role"] == "user" else False, key = generate()) # display all the previous message
    
    placeholder = st.empty() # placeholder for latest message
    
    # submitting form for new message ( clear input not found in other ways. )
    chat_input_form = st.form("chat_input" , clear_on_submit= True)
    input_ = chat_input_form.text_input(label = "message", key = "usermessage",value = '' , placeholder="Enter your message")
    # send button 
    submit = chat_input_form.form_submit_button(label = "Send" )
    #setting up for the proper inputs 
    if input_:
        st.session_state.message_history.append({"role":"user", "content":input_})
        formatted_msgs = get_response(st.session_state.message_history, model)
        st.session_state.message_history.append(formatted_msgs)
        # for msg in formatted_msgs:
        #     st.session_state.message_history.append(msg)
    
    if len(st.session_state.message_history)>= 2:
        with placeholder.container():
            message( st.session_state.message_history[-2]["content"], is_user=True if st.session_state.message_history[-2]["role"] == "user" else False, key = generate()) # display the latest message
            message( st.session_state.message_history[-1]["content"], is_user=True if st.session_state.message_history[-1]["role"] == "user" else False, key = generate()) # display the latest message


# chat_interface()