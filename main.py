from logic import *
import pandas as pd

Rain = Symbol("Rain")
HeavyTraffic = Symbol("HeavyTraffic")
EarlyMeeting = Symbol("EarlyMeeting")
Strike = Symbol("Strike")
Appointment = Symbol("Appointment")
RoadConstruction = Symbol("RoadConstruction")

WFH = Symbol("WFH")
Drive = Symbol("Drive")
PublicTransport = Symbol("PublicTransport")

rule1 = Implication(Or(Rain, EarlyMeeting), WFH)

rule2 = Implication(And(Not(Rain), Not(HeavyTraffic)), Drive)

rule3 = Implication(And(Not(Strike), Not(Rain)), PublicTransport)

rule4 = Implication(Appointment, Drive)

rule5 = Implication(RoadConstruction, Not(Drive))

knowledge_base = And(rule1, rule2, rule3, rule4, rule5)

scenarios = {
    "Scenario 1": {Rain: True, HeavyTraffic: True, EarlyMeeting: False, Strike: False, Appointment: False, RoadConstruction: False},
    "Scenario 2": {Rain: False, HeavyTraffic: False, EarlyMeeting: False, Strike: True, Appointment: False, RoadConstruction: False},
    "Scenario 3": {Rain: False, HeavyTraffic: False, EarlyMeeting: False, Strike: False, Appointment: False, RoadConstruction: False},
}

queries = {
    "WFH": WFH,
    "Drive": Drive,
    "PublicTransport": PublicTransport
}

results = {}
for scenario_name, scenario_model in scenarios.items():
    scenario_results = {}
    for query_name, query in queries.items():
        scenario_results[query_name] = model_check(knowledge_base, query)
    results[scenario_name] = scenario_results

results_df = pd.DataFrame(results)
print(results_df)