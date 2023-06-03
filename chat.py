import streamlit as st 
from streamlit_chat import message 
import openai 
from nanoid import generate # unique ids for every messages.
import requests 


def structurize_message(message_ , is_user):
    return {"role": "user" if is_user else "assistant", "content": message_}

def get_response(messages , model):
    messages = "\n".join([message["content"] for message in messages])
    # resp = requests.get("https://ed1d-2a09-bac5-3afb-18d2-00-279-32.ap.ngrok.io/query", params={"search": messages})
    # print(resp.text)
    new_data = {"docs":[{"pageContent":"38822985/\n6\n","metadata":{"id":"S_N_Bhardwaj_vs_Archeological_Survey_Of_India-11","case_name":"S_N_Bhardwaj_vs_Archeological_Survey_Of_India","case_date":"4_February_2016.PD"}},{"pageContent":"iankanoon.org/doc/73809958/\n6\n","metadata":{"id":"Educational_Society_Tumsar_And_vs_State_Of_Maharashtra_And_Ors-11","case_name":"Educational_Society_Tumsar_And_vs_State_Of_Maharashtra_And_Ors","case_date":"1_February_2016.PD"}},{"pageContent":"al, naming about 20 persons/companies as accused for the offences punishable under Sections\n120-B, 420, 468 and 471 of IPC, Section 66 of the Information Technology Act, 2000 and Section\n7(c) read with Section 13(2) of the Prevention of Corruption Act, 1988. It was found in the\npreliminary enquiry that e- Tender Nos. 91,93, and 94 for total works amounting to Rs. 1769.00\ncrores of Madhya Pradesh Water Corporation were tempered to change the price bid of M/s GVPR\nDirectorate Of Enforcement vs Aditya Tripathi on 12 May, 2023\nIndian Kanoon - http://indiankanoon.org/doc/194961561/\n1\n\fEngineers Limited, M/s The Indian Hume Pipe Company Limited and M/s IMC (sic) Project India\nLimited to make them the lowest bidders. Subsequent to the registration of the FIR, Economic\nOffences Wing, Bhopal conducted investigation and filed the chargesheet before the competent\ncourt on 04.07.2019. That on study of chargesheet, it was found that the accused have also\ncommitted the offences under the PML Act, 2002 as the offences for which they were chargesheeted,\nnamely, Sections 120-B, 420, 468 and 471 of IPC and Section 7 read with Section 13(2) of the PC\nAct, are also scheduled offences and therefore, the Enforcement Directorate, Hyderabad had\ninitiated money laundering investigation in the F. No. ECIR/HYZO/36/2020. That respective\nrespondent No. 1 herein in respective appeals were arrested on 19.01.2021, therefore, they filed the\npresent bail applications before the High Court to enlarge them on bail in connection with the\n","metadata":{"id":"Directorate_Of_Enforcement_vs_Aditya_Tripathi-1","case_name":"Directorate_Of_Enforcement_vs_Aditya_Tripathi","case_date":"12_May_2023.PD"}},{"pageContent":"Bharamappa Gogi vs Praveen Murthy & Ors. Etc on 9 February, 2016\nIndian Kanoon - http://indiankanoon.org/doc/12728689/\n4\n","metadata":{"id":"Bharamappa_Gogi_vs_Praveen_Murthy_Ors_Etc-7","case_name":"Bharamappa_Gogi_vs_Praveen_Murthy_Ors_Etc","case_date":"9_February_2016.PD"}}],"response":[{"res":{"text":"- The documents discuss the case of S.N. Bhardwaj vs. Archaeological Survey of"},"case":{"date":"4_February_2016.PD","name":"S_N_Bhardwaj_vs_Archeological_Survey_Of_India"}},{"res":{"text":"Documents:\n1. Government Resolution dated 14.03."},"case":{"date":"1_February_2016.PD","name":"Educational_Society_Tumsar_And_vs_State_Of_Maharashtra_And_Ors"}},{"res":{"text":"- The documents include: \n  - Judgment and Order passed by the High Court (impugned judgment)\n  - Criminal Appeal No. 1401 of 2023 and Criminal Appeal No. 1402 of 2023 (present appeals)\n  - Sections of the Prevention of Money Laundering Act, 2002 (PML Act, 2002)\n  - FIR No. 12/2019\n  - Chargesheet filed before the competent court on 04.07.2019\n- The argument of the respondent: \n  - Respective respondent No. 1 have been acquitted/discharged for the predicated offences in the FIR, therefore should be enlarged on bail for the scheduled offences under PML Act.\n  - Investigation is over and chargesheet has been filed, hence the High Court has rightly enlarged the accused on bail.\n  - The investigation by the Enforcement Directorate is still going on for the scheduled offences, but the accused have been on bail since March, 2021.\n  - The High Court has not committed any error in directing to enlarge the accused on bail.\n- Case interpretation: \n  - The High Court has failed to appreciate the rigour of Section 45 of the PML Act, 2002 and the seriousness of the scheduled offences alleged against the accused.\n  - The investigation by the Enforcement Directorate for the scheduled offences under the PML Act, 2002 is still ongoing, therefore, the impugned orders enlarging the respective respondent No. 1 on bail are unsustainable. \n  - The matters are remitted back to the High Court to consider the bail applications afresh in light of the observations made and only after the respective respondent No. 1 surrenders within a period of one week. \n- Laws referenced: \n  - Prevention of Money Laundering Act, 2002 (PML Act, 2002)\n  - Code of Criminal Procedure, 1973 (CrPC) \n  - Information Technology Act, 2000\n  - Prevention of Corruption Act, 1988"},"case":{"date":"12_May_2023.PD","name":"Directorate_Of_Enforcement_vs_Aditya_Tripathi"}},{"res":{"text":"- The case involves a challenge to the judgment and order dated 4.12.2009 rendered in Criminal Appeal Nos. 1126 of 2006 and 1167 of 2006 preferred by the respondent Nos. 1 and 2 in Criminal Appeal No. 2216 of 2010 and respondent No. 1 in Criminal Appeal No. 2217 of 2010 respectively.\n- The trial court framed charges against the respondents-accused under Sections 120B/302/390/392/457 read with Section 34 IPC.\n- The High Court found fault with the trial court in omitting to frame charge under Section 397 IPC against the respondents-accused and believed that the trial court was not justified in acquitting the respondent Nos. 1 and 2 in Criminal Appeal No. 1126 of 2006 of the charge under Section 302 IPC.\n- Referring to Sections 386 and 401 Cr.P.C. and invoking its suo motu power of revision, the High Court interfered with the conviction of the respondents-accused and remitted the matter to the trial court to frame charge under Section 397 IPC against the respondents-accused and to undertake a fresh consideration of the materials on record.\n- The appellant-informant argued that the trial court did not commit any error in not framing a charge under Section 397 IPC against the respondents-accused and that the High Court ought not to have interfered with their conviction.\n- The Supreme Court of India states that Section 397 IPC, having regard to the case of the prosecution, may not be wholly irrelevant, but the charges framed against the respondents-accused by the trial court do adequately encompass all essential facts building up the offences imputed against them.\n- The order of remand was deemed unnecessary, and the appeals should have been decided on the merits on the basis of the charges already framed and the materials on record.\n- The judgement refers to legal provisions such as Sections 120B, 302, 390, 392, 457, and 34 IPC."},"case":{"date":"9_February_2016.PD","name":"Bharamappa_Gogi_vs_Praveen_Murthy_Ors_Etc"}}]}
    output_data = new_data["response"]
    # output_data = resp.json()["response"]
    
    formatted_msg = ""
    for msg_data in output_data:
        msg_con = f"STUDY \n \n {msg_data['res']['text']} \n \n CASE NAME \n \n {msg_data['case']['name']} \n CASE_DATE {msg_data['case']['date']}  \n \n -------- \n \n"
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