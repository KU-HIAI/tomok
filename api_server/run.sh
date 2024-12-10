source ~/miniconda3/etc/profile.d/conda.sh
conda activate tomok

export PORT=51032

python openapi_generator.py
python app.py
