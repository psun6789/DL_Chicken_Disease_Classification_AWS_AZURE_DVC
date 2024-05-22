from ImageClassification import logger
from ImageClassification.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline


STAGE_NAME = 'Data Ingestion Stage'


try:
    logger.info(f'........ Stage {STAGE_NAME} started........!!!!!!!!')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'......... Stage {STAGE_NAME} Completed .......!!!!!!')
except Exception as e:
    logger.exception(e)
    raise e