import argparse
import shutil
import subprocess
import sys
from pathlib import Path


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run the full stock ML preprocessing pipeline on a chosen raw dataset."
    )
    parser.add_argument(
        "--raw-csv",
        type=Path,
        default=Path("data/raw/reliance_daily.csv"),
        help="Path to the raw stock CSV file to process.",
    )
    return parser.parse_args()


def run_script(script_path: Path) -> None:
    print(f"\n=== Running: {script_path.relative_to(ROOT)} ===")
    result = subprocess.run([sys.executable, str(script_path)], cwd=ROOT)
    if result.returncode != 0:
        raise SystemExit(
            f"Script failed with exit code {result.returncode}: {script_path}"
        )


def prepare_raw_data(raw_csv: Path, target_raw: Path) -> None:
    raw_csv = raw_csv.expanduser().resolve()
    target_raw.parent.mkdir(parents=True, exist_ok=True)

    if raw_csv == target_raw.resolve():
        print(f"Using existing raw dataset: {target_raw}")
        return

    if not raw_csv.exists():
        raise FileNotFoundError(f"Raw CSV file not found: {raw_csv}")

    print(f"Copying raw dataset from {raw_csv} to {target_raw}")
    shutil.copy2(raw_csv, target_raw)


if __name__ == "__main__":
    ROOT = Path(__file__).resolve().parent
    args = parse_args()

    expected_raw = ROOT / "data" / "raw" / "reliance_daily.csv"
    prepare_raw_data(args.raw_csv, expected_raw)

    steps = [
        ROOT / "data" / "clean_data.py",
        ROOT / "indicators" / "build_indicators.py",
        ROOT / "features" / "build_features.py",
        ROOT / "labels" / "create_labels.py",
        ROOT / "cv" / "generate_images.py",
    ]

    for step in steps:
        run_script(step)

    run_script(ROOT / "prediction.py")

    final_output = ROOT / "data" / "processed" / "reliance_labeled.csv"
    print("\n=== Pipeline complete ===")
    print(f"Final labeled dataset: {final_output}")
    print("Generated images are saved under: cv/images/")
    print("Prediction image is saved under: cv/prediction_latest.png")
    print("Run the full pipeline by calling: python run_pipeline.py --raw-csv path/to/your_dataset.csv")
