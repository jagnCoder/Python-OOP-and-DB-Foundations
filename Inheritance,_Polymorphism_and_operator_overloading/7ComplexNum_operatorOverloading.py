class Addition:
    def __init__(self):
        self.real = 0.0
        self.img = 0.0

    def set_real(self, real):
        self.real = real

    def set_img(self, img):
        self.img = img

    def get_real(self):
        return self.real

    def get_img(self):
        return self.img

    @staticmethod
    def add_real_part(obj1, obj2):
        return obj1.real + obj2.real

    @staticmethod
    def add_imaginary_part(obj1, obj2):
        return obj1.img + obj2.img

    def __add__(self, add_obj):
        result = Addition()
        result.real = self.real + add_obj.real
        result.img = self.img + add_obj.img
        return result

    def __str__(self):
        return f"{self.real} + {self.img}i"


# MAIN PROGRAM
real1 = float(input("Enter real part of first complex number: "))
img1 = float(input("Enter imaginary part of first complex number: "))
real2 = float(input("Enter real part of second complex number: "))
img2 = float(input("Enter imaginary part of second complex number: "))

obj1 = Addition()
obj2 = Addition()

obj1.set_real(real1)
obj1.set_img(img1)

obj2.set_real(real2)
obj2.set_img(img2)

real_sum = Addition.add_real_part(obj1, obj2)
img_sum = Addition.add_imaginary_part(obj1, obj2)

print("Real part addition:", real_sum)
print("Imaginary part addition:", img_sum)

complex_sum = obj1 + obj2
print("Complex Number:", complex_sum)
