from pathlib import Path

# CONFIG_FILE_PATH = Path("config/config.yaml")
# PARAMS_FILE_PATH = Path("params.yaml")



# from pathlib import Path
#
# # Get the parent directory of the current file (which is constants/__init__.py)
current_dir = Path(__file__).resolve().parent
# # Go up two levels to get the root directory of the project
root_dir = current_dir.parent.parent.parent
#
CONFIG_FILE_PATH = root_dir / "config" / "config.yaml"
PARAMS_FILE_PATH = root_dir / "params.yaml"

# print(f"Config file path: {CONFIG_FILE_PATH}")
# print(f"Params file path: {PARAMS_FILE_PATH}")
# # Ensure these paths are correct
# CONFIG_FILE_PATH = Path(r'C:\Users\Nimbus\_00_Peter_Practice_Projects\_02_In_Progress\_02_ML_Projects_Krish_Naik_Course_list\_02_DL_MLOPS_DVC_AZURE_AWS\DL_Chicken_Disease_Classification_AWS_AZURE_DVC\config\config.yaml')
# PARAMS_FILE_PATH = Path(r'C:\Users\Nimbus\_00_Peter_Practice_Projects\_02_In_Progress\_02_ML_Projects_Krish_Naik_Course_list\_02_DL_MLOPS_DVC_AZURE_AWS\DL_Chicken_Disease_Classification_AWS_AZURE_DVC\params.yaml')
