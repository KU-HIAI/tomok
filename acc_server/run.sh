export HYDRA_FULL_ERROR=1

# Determine the script directory
export SCRIPT_DIR=$(dirname "$0")
export PORT=51080
export LIBRARY_PATH="./library_files"
export IFC_PATH="./uploads}"
export SPECIFICATION_DIR="./openapi"
export API_FILE=${API_FILE:-tomok-demo.yaml}

# Run the app.py script
python "$SCRIPT_DIR/app.py"