"""
Multi-Energy System (MESpy) model

Modelling framework for optimization of hybrid electric and thermal small-scale energy systems sizing

Authors: 
    Lorenzo Rinaldi   - Department of Energy, Politecnico di Milano, Milan, Italy
    Stefano Pistolese - Department of Energy, Politecnico di Milano, Milan, Italy
    Nicolò Stevanato  - Department of Energy, Politecnico di Milano, Milan, Italy
                        Fondazione Eni Enrico Mattei, Milan, Italy
    Sergio Balderrama - Department of Mechanical and Aerospace Engineering, University of Liège, Liège, Belgium
                        San Simon University, Centro Universitario de Investigacion en Energia, Cochabamba, Bolivia
"""

                                                                                                                                        
                                                                 
#%% Economic constraints

"Objective function"
def Net_Present_Cost(model):
    return (sum(model.Scenario_Net_Present_Cost[s]*model.Scenario_Weight[s] for s in model.scenario))

def Scenario_Net_Present_Cost(model,s): 
    return model.Scenario_Net_Present_Cost[s] == model.Total_Investment_Cost + model.Fixed_Costs + model.Variable_Costs[s]


"Investment cost"
def Total_Investment_Cost(model):
    return model.Total_Investment_Cost == model.Generator_Investment_Cost + sum(model.Boiler_Investment_Cost[c] for c in model.classes)

def Generator_Investment_Cost(model):
   return model.Generator_Investment_Cost == model.Generator_Nominal_Capacity*model.Generator_Inv_Specific_Cost

def Boiler_Investment_Cost(model,c):
   return model.Boiler_Investment_Cost[c] == model.Boiler_Nominal_Capacity[c]*model.Boiler_Inv_Specific_Cost


"Fixed costs"                                                  
def Fixed_Costs(model):
    return model.Fixed_Costs == model.Generator_OM_Cost + sum(model.Boiler_OM_Cost[c] for c in model.classes)
 
def Generator_OM_Cost(model):
    return model.Generator_OM_Cost == sum(((model.Generator_Investment_Cost*model.Generator_OM_Specific_Cost)/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years)

def Boiler_OM_Cost(model,c):
    return model.Boiler_OM_Cost[c] == sum(((model.Boiler_Investment_Cost[c]*model.Boiler_OM_Specific_Cost)/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years)


"Variable costs"
def Variable_Costs(model,s):
    return model.Variable_Costs[s] == model.Scenario_Lost_Load_Cost_EE[s] + model.Total_Diesel_Cost[s] + sum(model.Scenario_Lost_Load_Cost_Th[s,c] + model.Total_NG_Cost[s,c] for c in model.classes)
                                                                                      
def Scenario_Lost_Load_Cost_EE(model,s):
    foo=[]
    for f in range(1,model.Periods+1):
        foo.append((s,f))
    return  model.Scenario_Lost_Load_Cost_EE[s] == sum(((sum(model.Lost_Load_EE[s,t]*model.EE_Value_Of_Lost_Load/60 for s,t in foo))/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years) 

def Total_Diesel_Cost(model,s):
    foo=[]
    for f in range(1,model.Periods+1):
        foo.append((s,f))
    return model.Total_Diesel_Cost[s] == sum(((sum(model.Diesel_Consumption[s,t]*model.Diesel_Unitary_Cost for s,t in foo))/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years) 
    
def Scenario_Lost_Load_Cost_Th(model,s,c):
    foo=[] 
    for f in range(1,model.Periods+1):
        foo.append((s,f))
    return  model.Scenario_Lost_Load_Cost_Th[s,c] == sum(((sum(model.Lost_Load_Th[s,c,t]*model.Th_Value_Of_Lost_Load/60 for s,t in foo))/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years) 
       
def Total_NG_Cost(model,s,c):
    foo=[] 
    for f in range(1,model.Periods+1):
        foo.append((s,f))
    return  model.Total_NG_Cost[s,c] == sum(((sum(model.NG_Consumption[s,c,t]*model.NG_Unitary_Cost for s,t in foo))/((1+model.Discount_Rate)**model.Project_Years[y])) for y in model.years)



#%% Electricity generation system constraints 

def Electric_Energy_Balance(model,s,t):
    return model.Electric_Energy_Demand[s,t] == model.Generator_Energy_Production[s,t] + model.Lost_Load_EE[s,t] - model.Electric_Curtailment[s,t]

"Diesel generator constraints"
def Maximum_Generator_Energy(model,s,t):
    return model.Generator_Energy_Production[s,t] <= model.Generator_Nominal_Capacity

def Diesel_Consumption(model,s,t): 
    return model.Diesel_Consumption[s,t] == model.Generator_Energy_Production[s,t]/model.Generator_Efficiency/model.Lower_Heating_Value/60

"Lost Load constraints"
def Maximum_Lost_Load_EE(model,s):
    return model.EE_Lost_Load_Tolerance*sum(model.Electric_Energy_Demand[s,t] for t in model.periods) >= sum(model.Lost_Load_EE[s,t] for t in model.periods)


#%% Thermal energy generation system constraints

def Thermal_Energy_Balance(model,s,c,t):
     return  model.Thermal_Energy_Demand[s,c,t] == model.Boiler_Energy_Production[s,c,t] - model.Thermal_Energy_Curtailment[s,c,t] + model.Lost_Load_Th[s,c,t]

"Boiler constraints"
def Maximum_Boiler_Energy(model,s,c,t):   
    return model.Boiler_Energy_Production[s,c,t] <= model.Boiler_Nominal_Capacity[c]

def NG_Consumption(model,s,c,t):
    return model.NG_Consumption[s,c,t] == model.Boiler_Energy_Production[s,c,t]/model.Boiler_Efficiency/model.Lower_Heating_Value_NG/60

"Lost load constraints"
def Maximum_Lost_Load_Th(model,s,c):
    return model.Th_Lost_Load_Tolerance*sum(model.Thermal_Energy_Demand[s,c,t] for t in model.periods) >= sum(model.Lost_Load_Th[s,c,t] for t in model.periods)


