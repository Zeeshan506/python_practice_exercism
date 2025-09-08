class SpaceAge:

    EARTH_YEAR = 31557600
    def __init__(self, seconds):
        self.seconds = seconds

    def get_planet_seconds(self, scale):
        planet_scale = SpaceAge.EARTH_YEAR * scale
        age = self.get_seconds() / planet_scale
        return round(age,2) 
    
    def get_seconds(self):
        return self.seconds

    def on_earth(self):
        age = self.get_planet_seconds(1)
        return age

    def on_mercury(self):
        return self.get_planet_seconds(0.2408467)

    def on_venus(self):
         return self.get_planet_seconds(0.61519726)
        
    def on_mars(self):
        return self.get_planet_seconds(1.8808158)
        
        
    def on_jupiter(self):
        return self.get_planet_seconds(11.862615)
        
    def on_saturn(self):
        return self.get_planet_seconds(29.447498)
        
    def on_uranus(self): 
        return self.get_planet_seconds(84.016846)
    
    def on_neptune(self):
        return self.get_planet_seconds(164.79132)

    
        