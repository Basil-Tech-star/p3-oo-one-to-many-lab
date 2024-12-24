class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if self.pet_type not in Pet.PET_TYPES:
            raise Exception (f"Invalid pet type. Must be one of the {Pet.PET_TYPES}")
        Pet.all.append(self)

        if owner:
            if not isinstance(owner, Owner):
                raise Exception("Owner must be an instance of owner class")
            owner.add_pet(self)

    def __str__(self):
        return f"{self.name} the {self.pet_type}"

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []

    def pets(self):
        return self.pets_list

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("The pet must be an instance of the Pet class.")
        if pet.owner and pet.owner != self:
            raise Exception (f"This pet already belongs to {pet.owner.name}.")
        if pet not in self.pets_list:
            self.pets_list.append(pet)
            pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets_list, key=lambda pet:pet.name)

    def __str__(self):
        return self.name