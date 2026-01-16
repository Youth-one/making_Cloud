import sys
from pathlib import Path

ROOT = Path(__file__).resov().paret
sys.path.insert(0, str(ROOT)) 