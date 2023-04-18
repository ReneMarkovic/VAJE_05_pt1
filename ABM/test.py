seznam_agentov=["Trava","Ovca","Volk"]

def ali_agent_obstaja(agent:str):
    if agent in seznam_agentov:
        print(f"Da, {agent} je v seznamu agentov")
    else:
        print(f"Ne, {agent} ni v seznamu agentov.")