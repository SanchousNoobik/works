def search_substr(subst, st):
    if subst.lower() in st.lower():
        	return 'Есть контакт!'
    else:
    	return 'Мимо!'


# Тесты
print(search_substr('Клон', 'поклон'))

