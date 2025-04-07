from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception .exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestedConfig, DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys


if __name__=="__main__":
    try:
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig= DataIngestedConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("eInitiate the data ingestion")
        dataingestionartifact= data_ingestion.initiate_data_ingestion()
        logging.info("data ingestion is completed")
        print(dataingestionartifact)
        datavalidationconfig=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Initiate the data validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("Data validation completed")


        

    except Exception as e:
        raise NetworkSecurityException(e, sys)