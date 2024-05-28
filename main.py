from ImageClassification import logger
from ImageClassification.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from ImageClassification.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from ImageClassification.pipeline.stage_03_training import ModelTrainingPipeline
from ImageClassification.pipeline.stage_04_evaluation import EvaluationPipeline

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

STAGE_NAME = 'Training'

try:
    logger.info(f'........ Stage {STAGE_NAME} started........!!!!!!!!')
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f'......... Stage {STAGE_NAME} Completed .......!!!!!!')
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Evaluation stage"
try:
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    model_evalution = EvaluationPipeline()
    model_evalution.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
    logger.exception(e)
    raise e