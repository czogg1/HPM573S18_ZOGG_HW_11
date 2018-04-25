# simulation settings
POP_SIZE = 2000     # cohort population size
SIM_LENGTH = 15     # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

DELTA_T = 1/52

# transition matrix
#TRANS_MATRIX = [
#    [0.75,  0.15,   0.0,    0.1],   # Well
#    [0,     0.0,    1.0,    0.0],   # Stroke
#    [0,     0.25,   0.55,   0.2],   # Post-Stroke
#    [0.0,   0.0,    0.0,    1.0],   # Dead
#    ]

TRANS_MATRIX = [
    [0.0000,    0.0136,    0.0000,    0.0015,   0.0178],   # Well
    [0.0000,    0.0000,    52.143,    0.0000,   0.0000],   # Stroke
    [0.0000,    0.0298,    0.0000,    0.0075,   0.0178],   # Post-Stroke
    [0.0000,    0.0000,    0.0000,    0.0000,   0.0000],   # Stroke Dead
    [0.0000,    0.0000,    0.0000,    0.0000,   0.0000],   # Dead
    ]

ANTICOAG_MATRIX = [
    [0.0000,    0.0136,    0.0000,    0.0015,   0.0178],   # Well
    [0.0000,    0.0000,    52.143,    0.0000,   0.0000],   # Stroke
    [0.0000,    0.0223,    0.0000,    0.0075,   0.0187],   # Post-Stroke
    [0.0000,    0.0000,    0.0000,    0.0000,   0.0000],   # Stroke Dead
    [0.0000,    0.0000,    0.0000,    0.0000,   0.0000],   # Dead
    ]

# annual health utility of each health state
HEALTH_UTILITY = [
    1.0000,  # well
    0.2000,  # stroke ONLY WHEN THE CYCLE LENGTH IS 1 YEAR
    0.9000,  # post-stroke
    0.0000,  # stroke dead
    0.0000,  # dead
    ]

# annual cost of each health state
HEALTH_COST = [
       0,    # well
    5000,    # stroke
     200,    # post-stroke /year
       0,    # stroke dead
       0,    # dead
    ]

# annual drug cost
Anticoag_COST = 750 - 200
