from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
import sys,os
from insurance.entity import config_entity
from insurance.components.data_ingestion import DataIngestion



if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          print(data_ingestion.initiate_data_ingestion())

          training_pipeline_config = config_entity.TrainingPipelineConfig()
          data_transformation_config  = config_entity.DataTransformationConfig(training_pipeline_config)(training_pipeline_config=training_pipeline_config)
          print(data_transformation_config.to_dict())
          data_ingestion = DataTransformation(data_transformation_config=data_transformation_config)
          print(data_transformation.initiate_data_transformation())
     except Exception as e:
          print(e)
