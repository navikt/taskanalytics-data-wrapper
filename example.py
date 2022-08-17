# %%
import os

from taskanalytics_data_wrapper import log_in_taskanalytics, get_survey_metadata, download_survey

# %%
email = os.environ["ta_email"]
password = os.environ["ta_password"]
# %%
status = log_in_taskanalytics(username=email, password=password)
status.status_code
# %%
get_survey = download_survey(
    username=email, password=password, survey_id="03324", filename="data/survey.csv"
)
get_survey.status_code
# %%
survey_metadata = get_survey_metadata(
    username=email, password=password, survey_id="03324"
)
survey_metadata.status_code
# %%
survey_metadata.text  # survey metadata