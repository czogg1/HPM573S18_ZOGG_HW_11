from enum import Enum
import InputData as Data
import numpy as np
import scr.MarkovClasses as MarkovCls

class HealthStats(Enum):
    """ health states of patients """
    WELL = 0
    STROKE = 1
    POST_STROKE = 2
    STROKE_DEAD = 3
    DEAD = 4


class Therapies(Enum):
    """ none versus anticoagulation therapy """
    NONE = 0
    ANTICOAG = 1


class ParametersFixed():
    def __init__(self, therapy):

        # selected therapy
        self._therapy = therapy

        # simulation time step
        self._delta_t = Data.DELTA_T

        # calculate the adjusted discount rate
        self._adjDiscountRate = Data.DISCOUNT * Data.DELTA_T

        # initial health state
        self._initialHealthState = HealthStats.WELL

        # annual treatment cost
        if self._therapy == Therapies.NONE:
            self._annualTreatmentCost = 0
        if self._therapy == Therapies.ANTICOAG:
            self._annualTreatmentCost = Data.Anticoag_COST

        # transition probability matrix of the selected therapy
        self._prob_matrix = []

        # calculate transition probabilities depending on which therapy options is in use
        if therapy == Therapies.NONE:
            self._prob_matrix = calculate_prob_matrix_none()
        else:
            self._prob_matrix = calculate_prob_matrix_anticoag()

        # annual state costs and utilities
        self._annualStateCosts = Data.HEALTH_COST
        self._annualStateUtilities = Data.HEALTH_UTILITY

    def get_initial_health_state(self):
        return self._initialHealthState

    def get_delta_t(self):
        return self._delta_t

    def get_adj_discount_rate(self):
        return self._adjDiscountRate

    def get_transition_prob(self, state):
        return self._prob_matrix[state.value]

    def get_annual_state_cost(self, state):
        if state == HealthStats.DEAD or state == HealthStats.STROKE_DEAD:
            return 0
        else:
            return self._annualStateCosts[state.value]

    def get_annual_state_utility(self, state):
        if state == HealthStats.DEAD or state == HealthStats.STROKE_DEAD:
            return 0
        else:
            return self._annualStateUtilities[state.value]

    def get_annual_treatment_cost(self):
        return self._annualTreatmentCost


def calculate_prob_matrix_none():
    """ :returns transition probability matrix for disease under no therapy """

    # create an empty matrix populated with zeros
    prob_matrix = []
    for s in prob_matrix:
        prob_matrix.append[0] * len(s)

    # call the transition rate matrix
    rate_matrix = Data.TRANS_MATRIX

    # convert to transition probability matrix
    prob_matrix[:], p = MarkovCls.continuous_to_discrete(rate_matrix=rate_matrix, delta_t=Data.DELTA_T)

    return prob_matrix


def calculate_prob_matrix_anticoag():
    """ :returns transition probability matrix for disease under no therapy """

    # create an empty matrix populated with zeros
    anticoag_matrix = []
    for l in anticoag_matrix:
        anticoag_matrix.append[0] * len(l)

    # call the transition rate matrix
    rate_matrix = Data.ANTICOAG_MATRIX

    # convert to transition probability matrix
    anticoag_matrix[:], p = MarkovCls.continuous_to_discrete(rate_matrix=rate_matrix, delta_t=Data.DELTA_T)

    return anticoag_matrix
