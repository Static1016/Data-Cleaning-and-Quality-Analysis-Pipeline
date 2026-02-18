from src.cleaner import clean_data


def main():
    input_path = "data/raw/messy_housing_data.csv"
    output_path = "data/cleaned/housing_cleaned.csv"

    df = clean_data(input_path, output_path)

    print("\nCleaning pipeline executed successfully.")
    print(f"Cleaned dataset saved to: {output_path}")
    print(f"Final dataset shape: {df.shape}")


if __name__ == "__main__":
    main()
