"""
This class is going to calculate how many years will it take to generate passive for a given income from renting apts.
"""
import math


class Calculator:
    def __init__(self, passive_income_desired_yearly, yearly_savings, starting_year, price_of_one_apartment,
                 price_od_renting_one_apartment):
        self._passive_income_desired_yearly = passive_income_desired_yearly #instance variable
        self._yearly_savings = yearly_savings
        self._starting_year = starting_year
        self._price_of_one_apartment = price_of_one_apartment
        self._price_od_renting_one_apartment = price_od_renting_one_apartment
        self._answer = dict() #odpowiedx w postaci słownika
        self._calculate()

    def _calculate(self):
        apt_number_owned = 0 #apt - apartment local variable
        income_reached = 0

        while self._passive_income_desired_yearly >= (apt_number_owned * self._price_od_renting_one_apartment):
            frac, whole = math.modf((self._yearly_savings + income_reached) / self._price_of_one_apartment)

            if whole >= 2:
                # if we can buy two/more apartments widac z całościowej częsci liczby math.modf
                apt_number_owned += whole
                income_reached = (self._yearly_savings + income_reached) - (whole * self._price_of_one_apartment)
                # odjecie pieniedzy po kupnie apartamentu/ów
                income_reached += (apt_number_owned * self._price_od_renting_one_apartment)  # liczba apartmaentów * roczny przychód z czynszu
            elif whole >= 1:
                apt_number_owned += whole
                income_reached = frac * self._price_of_one_apartment
                income_reached += (apt_number_owned * self._price_od_renting_one_apartment) # liczba apartmaentów * roczny przychód z czynszu
            else:
                # jeśli nie ma wystarczającej ilości pieniądzy na kupno kolejnego mieszkania
                income_reached += self._yearly_savings

            # bierzemy początkowy rok jako kluz słownika, [how many apartments do I own, income reached]
            self._answer[self._starting_year] = [apt_number_owned, round(income_reached)]
            self._starting_year += 1


