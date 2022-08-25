
class Hero:

    def heal(self, hp_gained, hp_max, hp_current):
        hp_current += hp_gained
        if hp_current > hp_max:
            hp_max

    def damage(self, hp_lost, hp_max, hp_current):
        hp_current -= hp_lost
        if hp_current <= 0:
            print(f"{Hero} has died")
            quit()
