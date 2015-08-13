m = input()
m_set = set(raw_input().strip().split())
n = input()
n_set = set(raw_input().strip().split())
final_set = sorted(m_set.symmetric_difference(n_set))
for i in final_set:
    print i
