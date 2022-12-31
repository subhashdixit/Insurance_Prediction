from insurance.logger import logging
from insurance.exception import InsuranceException
from insurance.utils import get_collection_as_dataframe
import sys,os
from insurance.entity import config_entity
from insurance.components.data_ingestion import DataIngestion
<<<<<<< HEAD



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
=======
from insurance.components.data_validation import DataValidation
from insurance.components.data_transformation import DataTransformation
from insurance.components.model_trainer import ModelTrainer
# from insurance.components.model_evaluation import ModelEvaluation

# file_path="/config/workspace/insurance_main_dataset.csv"
# print(__name__)
# if __name__=="__main__":
#      try:
#           #start_training_pipeline()
#           # output_file = start_training_pipeline()
#           # print(output_file)
#      except Exception as e:
#           print(e)



print(__name__)
if __name__=="__main__":
     try:
          training_pipeline_config = config_entity.TrainingPipelineConfig()

          #data ingestion
          data_ingestion_config  = config_entity.DataIngestionConfig(training_pipeline_config=training_pipeline_config)
          print(data_ingestion_config.to_dict())
          data_ingestion = DataIngestion(data_ingestion_config=data_ingestion_config)
          data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
          
          #data validation
        
          data_validation_config = config_entity.DataValidationConfig(training_pipeline_config=training_pipeline_config)
          data_validation = DataValidation(data_validation_config=data_validation_config,
                         data_ingestion_artifact=data_ingestion_artifact)
        
          data_validation_artifact = data_validation.initiate_data_validation()

          # data transformation
          data_transformation_config = config_entity.DataTransformationConfig(training_pipeline_config=training_pipeline_config)
          data_transformation = DataTransformation(data_transformation_config=data_transformation_config, 
          data_ingestion_artifact=data_ingestion_artifact)
          data_transformation_artifact = data_transformation.initiate_data_transformation()
          
          #model trainer
          model_trainer_config = config_entity.ModelTrainerConfig(training_pipeline_config=training_pipeline_config)
          model_trainer = ModelTrainer(model_trainer_config=model_trainer_config, data_transformation_artifact=data_transformation_artifact)
          model_trainer_artifact = model_trainer.initiate_model_trainer()

          # model_eval_config = config_entity.ModelEvaluationConfig(training_pipeline_config=training_pipeline_config)
          # model_eval  = ModelEvaluation(model_eval_config=model_eval_config,
          #  data_ingestion_artifact=data_ingestion_artifact,
          #  data_transformation_artifact=data_transformation_artifact,
          #   model_trainer_artifact=model_trainer_artifact)
          # # model_eval_artifact = model_eval.initiate_model_evaluation()
          
>>>>>>> 89e6215a6579f5377f2a3feffed56462736d8cb0
     except Exception as e:
          print(e)
