from checkov.common.models.enums import CheckCategories
from checkov.arm.base_resource_value_check import BaseResourceValueCheck


class MariaDBPublicAccessDisabled(BaseResourceValueCheck):
    def __init__(self) -> None:
        name = "Ensure 'public network access enabled' is set to 'False' for MariaDB servers"
        id = "CKV_AZURE_48"
        supported_resources = ("Microsoft.DBforMariaDB/servers",)
        categories = (CheckCategories.NETWORKING,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def get_inspected_key(self) -> str:
        return "properties/publicNetworkAccess"

    def get_expected_value(self) -> str:
        return "Disabled"


check = MariaDBPublicAccessDisabled()
