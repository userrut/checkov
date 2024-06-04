from __future__ import annotations

from typing import Any

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.arm.base_resource_check import BaseResourceCheck


class AzureDefenderOnKeyVaults(BaseResourceCheck):
    def __init__(self) -> None:
        name = "Ensure that Azure Defender is set to On for Key Vault"
        id = "CKV_AZURE_87"
        supported_resources = ("Microsoft.Security/pricings",)
        categories = (CheckCategories.GENERAL_SECURITY,)
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf: dict[str, list[Any]]) -> CheckResult:
        if conf["properties"]["pricingTier"] == "Standard":
            return CheckResult.PASSED
        else:
            return CheckResult.FAILED

    def get_evaluated_keys(self) -> list[str]:
        return ["pricingTier"]


check = AzureDefenderOnKeyVaults()
