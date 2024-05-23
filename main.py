from ImageClassification import logger
from ImageClassification.pipeline.state_01_data_ingestion import DataIngestionTrainingPipeline
from ImageClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'........ Stage {STAGE_NAME} started........!!!!!!!!')
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f'......... Stage {STAGE_NAME} Completed .......!!!!!!')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Prepare Base Model'

try:
    logger.info(f'........ Stage {STAGE_NAME} started........!!!!!!!!')
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f'......... Stage {STAGE_NAME} Completed .......!!!!!!')
except Exception as e:
    logger.exception(e)
    raise e