import streamlit as st
from agent_test import *

def main():
    st.title('Trusted Bank')

    with st.container(border=True):
        st.write("Your Wallet")
        tab1, tab2 , tab3 = st.tabs(["Account Overview", "Account Details", "Banking Bob"])
        with tab1:
            numberContainer = st.container(height=175, vertical_alignment="distribute", horizontal_alignment="center")
            with numberContainer:
                col1, col2, col3 = st.columns(3)
                col1.metric("Total Cash", "$0", "0%")
                col2.metric("Monthly Spend", "$10", "+100%")
                col3.metric("Number of Transactions", "1", "+100%")
                st.markdown("_Here is a snapshot of your account_")
        with tab2:
            left, right = st.columns(2)
            left.write("Name:")
            right.write("Ian Kim")
            left.write("Email:")
            right.write("ik7@williams.edu")
            left.write("Account Number:")
            right.write("PMZJGB4W")
            left.write("Routing Number:")
            right.write("MYNB48764759382421")
        with tab3:
            st.markdown("Banking Bob - _Your personal accountant_")
            chatContainer = st.container(height=500)
            user_input = st.chat_input("Start a conversation.", key="1")
            with chatContainer:
                if "show" not in st.session_state:
                    st.session_state["show"] = "True"
                if "show_chats" not in st.session_state:
                    st.session_state["show_chats"] = "False"
                if "messages" not in st.session_state:
                    st.session_state["messages"] = []
                show_msgs()
                if user_input:
                    with st.chat_message("user"):
                        st.write(user_input)
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    messages = "\n".join(msg["content"] for msg in st.session_state.messages)
                    response = chat(messages)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    with st.chat_message("assistant"):
                        st.write_stream(response_generator(response))
                elif st.session_state['messages'] is None:
                    st.info("Start a conversation.")
            

if __name__ == "__main__":
    main()




