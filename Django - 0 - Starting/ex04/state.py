import sys


def find_state():
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
    
    capital_name = sys.argv[1]
    
    # Inverser (capital -> code)
    capital_to_code = {v: k for k, v in capital_cities.items()}
    
    # Inverser (code -> state)
    code_to_state = {v: k for k, v in states.items()}
    
    if capital_name in capital_to_code:
        state_code = capital_to_code[capital_name]
        
        if state_code in code_to_state:
            print(code_to_state[state_code])
            return
    
    print("Unknown capital city")
    
if __name__ == '__main__':
    find_state()
