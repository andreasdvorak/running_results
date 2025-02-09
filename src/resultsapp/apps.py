"""_summary_"""
from django.apps import AppConfig

# @todo what is this class
class ResultsAppConfig(AppConfig):
    """_summary_

    Args:
        AppConfig (_type_): _description_
    """
    # type of the automatically created primary key
    default_auto_field = 'django.db.models.AutoField'
    name = 'resultsapp'
    verbose_name = "Result App"
