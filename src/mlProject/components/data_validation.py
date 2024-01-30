import os
from src.mlProject import logger
from src.mlProject.config.configuration import ConfigurationManager
from src.mlProject.entity.config_entity import DataValidationConfig
import pandas as pd


class DataValiadtion:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def are_dicts_equal(self, dict1, dict2):
        return all(item in dict2.items() for item in dict1.items())

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
            # all_cols = list(data.columns)

            all_schema = self.config.all_schema
            columns_dtypes_dict = data.dtypes.apply(lambda x: x.name).to_dict()

            # Check if all elements of dict1 are in dict2
            result = self.are_dicts_equal(all_schema, columns_dtypes_dict)

            if not result:
                validation_status = False
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")
            else:
                validation_status = True
                with open(self.config.STATUS_FILE, 'w') as f:
                    f.write(f"Validation status: {validation_status}")

            return validation_status


            # for col in all_cols:
            #     if col not in all_schema:
            #         validation_status = False
            #         with open(self.config.STATUS_FILE, 'w') as f:
            #             f.write(f"Validation status: {validation_status}")
            #     else:
            #         validation_status = True
            #         with open(self.config.STATUS_FILE, 'w') as f:
            #             f.write(f"Validation status: {validation_status}")
            #
            # return validation_status

        except Exception as e:
            raise e


if __name__ == '__main__':
    config = ConfigurationManager()
    data_validation_config = config.get_data_validation_config()
    data_validator = DataValiadtion(data_validation_config)
    val_status = data_validator.validate_all_columns()
    print(0)
