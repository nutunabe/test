import os
import sys
PROJECT_PATH = os.getcwd()
CLASSES_PATH = os.path.join(
    PROJECT_PATH, "models"
)
COMPONENTS_PATH = os.path.join(
    PROJECT_PATH, "components"
)
sys.path.append(COMPONENTS_PATH)
sys.path.append(CLASSES_PATH)
