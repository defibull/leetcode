from datetime import datetime, timedelta
def solution(S):
    old_time = datetime.strptime(S, "%H:%M")
    h_m_set = set([char for char in S if char.isdigit()])
    while (True):
        old_time = old_time+timedelta(minutes=1)
        str_time = old_time.strftime("%H:%M")
        all_in_set = True
        for char in str_time:
            if char.isdigit() and char not in h_m_set:
                print char, h_m_set
                all_in_set = False
                return None
        if all_in_set:
            return str_time

print solution('11:00')
