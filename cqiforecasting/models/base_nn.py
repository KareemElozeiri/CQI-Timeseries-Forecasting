"""Abstract base model"""

from abc import ABC, abstractmethod
from cqiforecasting.utils.config import Config
from cqiforecasting.dataloader.nn_data_loader  import NNDataLoader

class BaseNN(ABC):
    """Abstract Model class that is inherited to all models"""

    def __init__(self, cfg):
        self.config = Config.from_json(cfg)
        self.data_loader = NNDataLoader(self.config["data"])

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def build(self):
        pass
    
    @abstractmethod
    def compile(self):
        pass

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def evaluate(self):
        pass

    