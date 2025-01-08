import json

def get_brain_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

file_path = 'brain_regions.json'
brain_data = get_brain_data(file_path)
listOfKeys = list(brain_data.keys())
simple_string = "Choose one of the available regions or type 'exit' to leave:"
final = ", ".join(listOfKeys)
full_prompt = simple_string + " " + final + ": "
while True:
    user_choice = input(full_prompt)
    p1 = user_choice.split()
    if user_choice in brain_data:
        key = user_choice
    else:
        key = p1[0] + " lobe"
    if key in brain_data.keys():
        region_info = brain_data[key]
        print(region_info)
    elif user_choice == 'exit':
        print("Exiting...")
        break
    else:
        print("Error, not a valid input.")
