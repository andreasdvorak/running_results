from django.apps import AppConfig

# @todo what is this class
class ResultsAppConfig(AppConfig):
    default_auto_field = 'django.db.models.AutoField' # type of the automatically created primary key
    name = 'resultsapp'
    verbose_name = "Rock ’n’ roll"
