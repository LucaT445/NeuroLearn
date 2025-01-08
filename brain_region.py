class BrainRegion:
    def __init__(self, name, function, location):
        self.name = name
        self.function = function
        self.location = location
    def display_info(self):
        print("Name: " + self.name + "\n", "Function: " + self.function + "\n", "Location: " + self.location + "\n")
    def __str__(self):
        message = "Name: {0}\nFunction: {1}\nLocation: {2}\n".format(self.name, self.function, self.location)
        return message

list_of_lobes = []
frontal = BrainRegion("Frontal Lobe", "Executive functions, movement, and thinking", "Front of the brain")
parietal = BrainRegion("Parietal Lobe", "Sensory integration and spatial awareness", "Top and back of the brain")
temporal = BrainRegion("Temporal Lobe", "Auditory processing and memory", "Sides of the brain")
occipital = BrainRegion("Occipital Lobe", "Visual processing", "Back of the brain")
list_of_lobes.extend([frontal, parietal, temporal, occipital])


      

if __name__ == "__main__":
    user_input = input("Enter a name: ")
    for lobe in list_of_lobes:
        user_input = user_input.lower()
        if user_input in lobe.name.lower():
            lobe.display_info()
        # print(lobe)
   
