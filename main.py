
import yaml
from src.logger import setup_logger
from src.data_ingestion import load_data
from src.data_cleaning import clean_data
from src.data_analysis import summarize_data
from src.visualization import plot_summary
from src.report_generator import generate_pdf

if __name__ == "__main__":
    config = yaml.safe_load(open("config.yaml"))
    logger = setup_logger(config['log_file'])

    try:
        logger.info("Loading data...")
        df = load_data(config['input_path'])

        logger.info("Cleaning data...")
        df = clean_data(df)

        logger.info("Analyzing data...")
        summary = summarize_data(df)

        logger.info("Generating visualizations...")
        plot_summary(df, config['output_path'])

        logger.info("Generating PDF report...")
        generate_pdf(summary, config['report_path'])

        logger.info("Pipeline executed successfully.")
    except Exception as e:
        logger.error(f"Error: {e}")
