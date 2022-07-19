class Gun:
    def __init__(self):
        self.reload_cycle = ['Regular', 'Piercing', 'Hollow-tip']
        self.current_reload_index = 3 
        self.cartridge = []
        self.cartridge_max = 5

    def Shoot(self):
        """
        A function that checks to see if the gun is empty, and then returns the bullet it its not empty, otherwise return "empty"
        """
        if(len(self.cartridge) != 0):
            return self.cartridge.pop()
        else:
            return 'Empty'

    def Reload(self):
        """
        Have the cartridge reload to max capacity using the next bullet type in the cycle
        """
        self.current_reload_index +=1
        
        if self.current_reload_index >= len(self.reload_cycle):
            self.current_reload_index = 0
        
        while len(self.cartridge) < self.cartridge_max:
            self.cartridge.append(self.reload_cycle[self.current_reload_index])
    
    def Show_Next_Bullet(self):
        """
        print what the next bullet in the cartridge to be shot is
        """
        copy = self.cartridge[:]
        print(copy.pop())

gun = Gun()
gun.Reload()
print(gun.Shoot()) #'regular'
gun.Shoot()
gun.Shoot()
gun.Reload()
gun.Show_Next_Bullet() # 'piercing'
gun.Shoot()
gun.Reload()

print("\nNow shoot the rest\n")
print(gun.Shoot()) #'hollow-tip'
print(gun.Shoot()) #'piercing'
print(gun.Shoot()) #'piercing'
print(gun.Shoot()) #'regular'
print(gun.Shoot()) #'regular'
print(gun.Shoot()) #'empty'