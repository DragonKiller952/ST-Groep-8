from Models.PluralityModel import PluralityModel
from Models.InstantRunoffModel import InstantRunoffModel
from Models.PrefrenceModel import PrefrenceModel

from mesa.batchrunner import BatchRunner

# Batch runned (1000 times) and write to csv
def generate_winners_data():
    parameters = { "n_partys": [10] * 10, "n_voters": [1000] * 100 }
    batch_run = BatchRunner(PrefrenceModel, parameters, max_steps=100, model_reporters={"Winner": lambda m: m.compute_winner().color})
    batch_run.run_all()
    batch_df = batch_run.get_model_vars_dataframe()
    batch_df.to_csv('data.csv')  

