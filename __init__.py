import os
import sys
PROJECT_PATH = os.getcwd()
CLASSES_PATH = os.path.join(
    PROJECT_PATH, "models"
)
COMPONENTS_PATH = os.path.join(
    PROJECT_PATH, "components"
)
if COMPONENTS_PATH not in sys.path:
    sys.path.append(COMPONENTS_PATH)
if CLASSES_PATH not in sys.path:
    sys.path.append(CLASSES_PATH)
