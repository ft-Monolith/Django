import sys


def search_all():
    states = {
        "Oregon" : "OR",
        "Alabama" : "AL",
        "New Jersey": "NJ",
        "Colorado" : "CO"
    }
    
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    
    if len(sys.argv) != 2:
        return
    
    # Récupérer l'argument et split par virgule
    search_string = sys.argv[1]
    
    # Vérifier s'il y a deux virgules d'affilées
    if ",," in search_string:
        return
    
    words = search_string.split(",")
    
    # Créer des dictionnaires inversés pour recherche par capital
    capital_to_code = {v.lower(): k for k, v in capital_cities.items()}
    code_to_state = {v.lower(): k for k, v in states.items()}
    
    # Traiter chaque mot
    for word in words:
        word_clean = word.strip()
        
        # Ignorer les mots vides
        if not word_clean:
            continue
        
        word_normalized = word_clean.lower()
        
        # Chercher dans states (clé = état)
        found_state = None
        for state, code in states.items():
            if state.lower() == word_normalized:
                found_state = state
                state_code = code
                break
        
        if found_state:
            capital = capital_cities[state_code]
            print(f"{capital} is the capital of {found_state}")
            continue
        
        # Chercher dans capital_cities (valeur = capitale)
        found_capital = None
        found_code = None
        for code, capital in capital_cities.items():
            if capital.lower() == word_normalized:
                found_capital = capital
                found_code = code
                break
        
        if found_capital:
            state = code_to_state[found_code.lower()]
            print(f"{found_capital} is the capital of {state}")
            continue
        
        # Ni état ni capitale
        print(f"{word_clean} is neither a capital city nor a state")


if __name__ == '__main__':
    search_all()
