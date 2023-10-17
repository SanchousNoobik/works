
def search_substr(substr, st):
    if substr.lower() in st.lower():
        return 'Есть контакт'
    else:
        return 'Мимо'
print(search_substr('chinese', 'cheese'))


    