from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

# artifact.set_text(text)
# artifact.set_font_size(FONT_SIZE)
# artifact.set_color(color)
# artifact.set_position(position)
# artifact.set_message(message)

class Artifact(Actor):


    
    def __init__(self):

        # invoking the parent class constructor. 
        super().__init__() 
        self._message = 0

    def get_message(self):
        return self._message

    def set_message(self, message):
        self._message = message
