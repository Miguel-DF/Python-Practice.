
class Sport:

    alive = True

    def Basketball(self):
        print("Basketball Player")

    def Football(self):
        print("Soccer Player")

    def Baseball(self):
        print("Baseball Player")

class Stephen(Sport):

    def shooting(self):
        print("This Player can shoot")
class Messi(Sport):
    pass
class Ohtani(Sport):
    pass

stephen = Stephen()
messi = Messi()
Ohtani = Ohtani

print(Stephen.Basketball)
stephen.shooting()