from modules.data_extractor import extract_data
from modules.data_process import process_payments_data
from modules.data_base import update_db_data
from modules.logger import get_logger
from datetime import datetime

# Configuração de logging
logger = get_logger()

def run_pipeline(endpoint, table, start_date=None, end_date=None):
    """
    Executa os scripts de extração, processamento e atualização dos dados no banco de dados.

    :param endpoint: endpoint da API a ser acessado para extrair dados.
    :param table: nome da tabela do banco onde os dados serão inseridos.
    :param start_date: Data de início para a extração de dados (no formato 'AAAA-MM-DD').
    :param end_date: Data de término para a extração de dados (a data atual)
    """
    try:
        # extraindo dados da API
        logger.info(f"Iniciando a extração dos dados do endpoint '{endpoint}'! Por favor aguarde...")
        raw_data = extract_data(endpoint, start_date=start_date, end_date=end_date)

        # Processando dados extraídos
        logger.info("Processando os dados extraídos...")
        processed_data = process_payments_data(raw_data)

        # Atualizando banco de dados
        logger.info(f"Iniciando atualização dos dados na tabela '{table}'...")
        update_db_data(processed_data, table)

        logger.info("Pipeline concluído com sucesso!")

    except Exception as e:
        logger.error(f"Ocorreu um erro inesperado: {e}")

def main():
    # Configurações para extrair os dados de cobranças
    endpoint = "payments"
    table = "DADOS_ASAAS_PAYMENTS"
    start_date = "2023-01-01"
    end_date = datetime.now().strftime("%Y-%m-%d")

    # Executa o pipeline
    run_pipeline(endpoint, table, start_date=start_date, end_date=end_date)

if __name__ == "__main__":
    main()
