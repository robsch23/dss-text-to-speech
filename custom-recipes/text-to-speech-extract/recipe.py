from dataiku.customrecipe import get_input_names_for_role, get_output_names_for_role, get_recipe_config
from gtts import gTTS

# get_recipe_config restituisce un dizionario con le chiave corrispondenti ai params definiti in recipe.json

# To retrieve the datasets of an input role named 'input_A' as an array of dataset names:
dataset_name = get_input_names_for_role('dataset_input')[0]

# For outputs, the process is the same:
output_name = get_output_names_for_role('dataset_output')[0] # se è una folder allora mi ritroverò qui il nome della folder

text_column_name = get_recipe_config().get('text_column_name')

# Read recipe inputs
df_input = dataiku.Dataset(dataset_name).get_dataframe()

tts = gTTS('text')
tts.save('path + .mp3')


# Write recipe outputs
output_dataset = dataiku.Dataset(output_name)
output_dataset.write_with_schema(df)
