from django.apps import AppConfig

# @todo what is this class
class ResultsAppConfig(AppConfig):
    # type of the automatically created primary key
    default_auto_field = 'django.db.models.AutoField'
    name = 'resultsapp'
    verbose_name = "Result App"
