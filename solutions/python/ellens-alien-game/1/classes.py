"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0
    
    def __init__(self, x_cordinate, y_cordinate,health = 3):
        self.x_coordinate = x_cordinate
        self.y_coordinate = y_cordinate
        self.health = health
        Alien.total_aliens_created += 1

    def hit(self):
        self.health -=1
        

    def is_alive(self):
        return self.health >= 1

    def teleport(self,new_x_coordinate, new_y_coordinate):
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate

    def collision_detection(x_coordinate, y_coordinate):
        pass
    


#TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.
def new_aliens_collection(alien_start_position):
    list_of_aliens = []
    for pair in alien_start_position:
        alien = Alien(pair[0],pair[1])
        list_of_aliens.append(alien)
    return list_of_aliens
        
    