import os
from main import generate_dataset, demo_dataset
# from generators import generate_11852cab
# from verifiers import verify_11852cab
import tqdm

generate_dataset(n_examples=10)
os.makedirs('out', exist_ok=True)
demo_dataset(n=1,s=0, e=80)
