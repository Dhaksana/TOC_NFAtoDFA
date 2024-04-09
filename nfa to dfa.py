import pandas as pd
states = ['q0', 'q1', 'q2']
var = ['0', '1']
nfa = {'q0': {'0': ['q0', 'q1'], '1': ['q1']}, 'q1': {'0': ['q2'], '1': ['q2']}, 'q2': {'0': [], '1': ['q2']}}

nfa_final_state = ['q1', 'q2']

new_states = [states[0]]
dfa = {'%': {}}
for i in var:
    dfa['%'][i] = ['%']
dfa[states[0]] = {}
for j in var:
    dfa[states[0]][j] = []
while True:
    l = list(dfa.keys())
    for i in l:
        if i != '%':  # to skip the trap state of dfa
            for j in var:
                # s = ' '.join(nfa[i][j])    # --> expanding this in next phase
                x = i.split(' ')
                values = []
                for k in x:
                    values.extend(nfa[k][j])
                values = list(set(values))  # to remove duplicates
                values.sort()
                s = ' '.join(values)
                if s not in dfa.keys() and s != '':
                    states.append(s)
                    dfa[s] = {}
                    for l in var:
                        dfa[s][l] = []
                dfa[i][j] = [s]
                '''
                
                '''
                if s == '':
                    states.append(s)
                    if i not in dfa.keys():  # if the state doesn't exist create a state
                        dfa[i] = {}
                    dfa[i][j] = ['%']
    flag = True
    for key in dfa.keys():
        for m in var:
            if dfa[key] == {} or dfa[key][m] == []:
                flag = False
    if flag:
        break
print("\nPrinting DFA table :- ")
dfa_table = pd.DataFrame(dfa)
print(dfa_table.transpose())