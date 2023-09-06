
from app import db
from ..models import history_model
from ..models.history_model import HistoryModel


class HistoricService():

    def save_history(id):
        save = HistoryModel(id=id)

    def read_all():
        all = history_model.HistoryModel.query.all()
        return all
    


    