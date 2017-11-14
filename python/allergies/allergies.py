class Allergies():
    
    allergen_scores = (128, 64, 32, 16, 8, 4, 2, 1)
    allergen_names = 'cats pollen chocolate tomatoes strawberries shellfish peanuts eggs'.split()
    score_to_allergen = dict(zip(allergen_scores, allergen_names))

    def __init__(self, score):
        self._score = score % 256
        self._allergen_scores = []
        for alsc in self.allergen_scores:
            if self._score >= alsc:
                self._allergen_scores.append(alsc)
                self._score -= alsc
        self._allergens = [self.score_to_allergen[score] for score in self._allergen_scores]

    def is_allergic_to(self, item):
        return item in self._allergens

    @property
    def lst(self):
        return self._allergens