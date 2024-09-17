from src.cnnClassifier import logger
from src.cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

# logger.info("Welcome to our custom log")


STAGE_NAME = "Data Ingestion stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======")
except Exception as e:
        logger.exception(e)
        raise e
