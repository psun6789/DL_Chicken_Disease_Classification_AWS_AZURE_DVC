from ImageClassification.config.configuration import ConfigurationManager
from ImageClassification.components.prepare_base_model import PrepareBaseModel
from ImageClassification import logger
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

STAGE_NAME = 'Data Ingestion Stage'

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):    
        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            logger.error(f"Error during data ingestion: {e}")
            raise e


if __name__ == '__main__':
     try:
          logger.info('*****************************************************')
          logger.info(f'........ Stage {STAGE_NAME} started........!!!!!!!!')
          obj = PrepareBaseModelTrainingPipeline()
          obj.main()
          logger.info(f'......... Stage {STAGE_NAME} Completed .......!!!!!!')
          logger.info('*****************************************************')
     except Exception as e:
          logger.exception(e)
          raise e



