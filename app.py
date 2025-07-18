import contact
import streamlit as st

st.title('📒 Contact Book ✆')
st.write('')

if 'contact_book' not in st.session_state :
    st.session_state.contact_book = contact.ContactBook()

manual_add = st.button('ADD')
if manual_add :
    st.session_state.contact_book.add_contact('ali' , '123-456-789' , 'ali@gmail.com')
    st.session_state.contact_book.add_contact('mohammad' , '987-654-321' , 'mohammad@gmail.com')
    st.session_state.contact_book.add_contact('reza' , '111-222-333' , 'reza@gmail.com')
    st.session_state.contact_book.add_contact('ali' , '999-999-999' , 'ali.ali@gmail.com')
    st.session_state.contact_book.add_contact('ali' , '111-111-111' , 'ali.ali2@gmail.com')

if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'

col1 , col2 , col3 , col4 , col5 = st.columns(5)

add = col1.button('Add')
view = col2.button('View')
edit = col3.button('Edit')
find = col4.button('Find')
delete = col5.button('Delete')

if add : st.session_state.current_page = 'add'
if view : st.session_state.current_page = 'view'
if edit : st.session_state.current_page = 'edit'
if find : st.session_state.current_page = 'find'
if delete : st.session_state.current_page = 'delete'

if st.session_state.current_page == 'add':
    name = st.text_input('' , placeholder = 'name')
    phone = st.text_input('' , placeholder = 'phone')
    email = st.text_input('' , placeholder = 'email')
    if add and name != '' and phone != '' :
        add_msg = st.session_state.contact_book.add_contact(name , phone , email)
        if add_msg[0] == 'added' :
            st.success(add_msg[1])
        else :
            st.error(add_msg[1])

if st.session_state.current_page == 'view' :
    contacts = st.session_state.contact_book.view_contacts()
    if len(contacts.items()) == 0 :
        st.error('contact book is empty!')
    else :
        for key , value in contacts.items() :
            st.info(f'''
                    name : {contacts[key]["name"]} \n
                    phone : {contacts[key]["phone"]} \n
                    email : {contacts[key]["email"]}''')

if st.session_state.current_page == 'edit' : 
    edit_name = st.text_input('' , placeholder = 'name of contact you want to edit')
    new_name = st.text_input('' , placeholder = 'new name')
    new_phone = st.text_input('' , placeholder = 'new phone')
    new_email = st.text_input('' , placeholder = 'new email')
    if (edit and edit_name != '' and (new_name != '' or new_phone != '' or new_email != '')):
        contacts = st.session_state.contact_book.get_contact(edit_name)
        if len(contacts.items()) > 1 :
            for key , value in contacts.items() :
                st.info(f'''
                    name : {contacts[key]["name"]} \n
                    phone : {contacts[key]["phone"]} \n
                    email : {contacts[key]["email"]}''')
            edit_phone = st.text_input('' , placeholder = 'phone of contact you want to edit')
            if edit and edit_phone != '' :
                update_msg = st.session_state.contact_book.update_contact(edit_name , edit_phone , new_name , new_phone , new_email)
                if ('updated' in update_msg) :
                    st.success(update_msg)
                else :
                    st.error(update_msg)
        else :
            update_msg = st.session_state.contact_book.update_contact(edit_name , new_name , new_phone , new_email)
            if ('updated' in update_msg) :
                st.success(update_msg)
            else :
                st.error(update_msg)

    if st.session_state.current_page == 'find' :
        search_name = st.text_input('' , placeholder = 'name of contact that you want search')
        if find and search_name != '' :
            contacts = st.session_state.contact_book.get_contact(search_name)
            if len(contacts.items()) == 0 :
                st.error(f'contact {search_name} not found!')
            else :
                for key , value in contacts.items() :
                    st.info(f'''
                            name : {contacts[key]["name"]} \n
                            phone : {contacts[key]["phone"]} \n
                            email : {contacts[key]["email"]}''')

if st.session_state.current_page == 'delete' :
    del_name = st.text_input('' , placeholder = 'name of contact that you want delete')
    if delete and del_name != '' :
        contacts = st.session_state.contact_book.get_contact(del_name)
        if len(contacts.items()) > 1 :
            for key , value in contacts.items() :
                st.info(f'''
                    name : {contacts[key]["name"]} \n
                    phone : {contacts[key]["phone"]} \n
                    email : {contacts[key]["email"]}''')
            del_phone = st.text_input('Please Enter a Phone number' , placeholder = 'phone of contact that you want delete')
            if delete and del_phone != '' :
                delete_msg = st.info(st.session_state.contact_book.delete_contact(del_name , del_phone))
                if ('deleted' in delete_msg) :
                    st.success(delete_msg)
                else :
                    st.error(delete_msg)
        else :
            delete_msg = st.session_state.contact_book.delete_contact(del_name)
            if ('deleted' in delete_msg) :
                st.success(delete_msg)
            else :
                st.error(delete_msg)
