class Cat:
    """Un chat."""

    def meow(self):
        """Miaule."""
        print("Meow!")
    
    def test(self):
        print("TEST FROM CAT")


class Talker:
    """Interface qui définit la méthode "say" (dire)."""
     
    def say(self, to_say):
        """Affiche "to_say" (à dire)."""
        print(to_say)
    
    def test(self):
        print("TEST FROM TALKER")


class TalkingCat(Cat, Talker):
    """Un chat qui parle ??"""
    pass


salem = TalkingCat()
salem.meow()
salem.say("Hello!")
salem.test()