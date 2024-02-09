from dataiku.customrecipe import get_input_names_for_role, get_output_names_for_role, get_recipe_config
from gtts import gTTS
import os

# get_recipe_config restituisce un dizionario con le chiave corrispondenti ai params definiti in recipe.json

# To retrieve the datasets of an input role named 'input_A' as an array of dataset names:
dataset_name = get_input_names_for_role('input_dataset')[0]
df = dataiku.Dataset(dataset_name).get_dataframe()

# For outputs, the process is the same:
output_name = get_output_names_for_role('output_folder')[0]
output_folder = dataiku.Folder(output_name).get_info().get('path')

text_column_name = get_recipe_config().get('text_column_name')
output_files_type = get_recipe_config().get('output_files_type')
language_and_tld_params = get_recipe_config().get('language')

lang, tld = language_and_tld_params.split('-')[0], language_and_tld_params.split('-')[1]

list_text = df[text_column_name].to_list()

for text in list_text:
    tts = gTTS(text, lang=lang, tld=tld, slow=True)
    tts.save(os.path.join(output_folder, f'{str(text)[:15]}.{str(output_files_type)}'))
