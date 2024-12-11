class Smartphone:
    def __init__(self, brand, model, RAM, processor, storage):
        self.brand = brand
        self.model = model
        self.RAM = RAM
        self.processor = processor
        self.storage = storage

    def display_specs(self):
        return f"Brand: {self.brand}, Model: {self.model}, RAM: {self.RAM}GB, Processor: {self.processor}, Storage: {self.storage}GB"


# Creating objects with values
tecno = Smartphone("Tecno", "Camon 16", 8, "Intel", 128)
iphone = Smartphone("Apple", "iPhone 12", 4, "A14 Bionic", 64)

# Display
print(tecno.display_specs())
print(iphone.display_specs())


class Tablet(Smartphone):
    pass
tablet = Tablet("Samsung", "A14", 8, "intel", 128)
print(tablet.brand)
