from collections import Counter
def top3(st):
    counter_top3=Counter(st.replace(' ','')).most_common(3)
    print(counter_top3)
top3("sdfjdsfjdskljdslfjdjldjsdjflhfhhjsdsdhkfj")