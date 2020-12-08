# from mesa.datacollection import DataCollector
# from mesa.batchrunner import BatchRunner

 # self.dc = DataCollector(model_reporters={"agent_count":
        #                             lambda m: m.schedule.get_agent_count()},
        #                         agent_reporters={"name": lambda a: a.name})

# parameters = {"n_agents": range(0, 5)}
# batch_run = BatchRunner(PluralityModel, parameters, max_steps=10,
#                         model_reporters={"n_agents": lambda m: m.schedule.get_agent_count()})
# batch_run.run_all()
# batch_df = batch_run.get_model_vars_dataframe()
# print(batch_df)

# grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)
# server = ModularServer(PluralityModel,
#                        [grid],
#                        "My Model",
#                        {'n_agents': 10})
# server.launch()
