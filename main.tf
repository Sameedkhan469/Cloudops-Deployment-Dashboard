
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 5.0"
    }
  }
}

provider "azurerm" {
  features {}

  subscription_id = "0c5d586b-3f22-483b-aed7-12936f779b9b"
}

# 1. Create Azure Resource Group
resource "azurerm_resource_group" "cloudops" {
  name     = "sam-cloudops-rg"
  location = "Central India"
}

# 2. Create Linux App Service Plan
resource "azurerm_service_plan" "cloudops" {
  name                = "sam-cloudops-plan"
  resource_group_name = azurerm_resource_group.cloudops.name
  location            = azurerm_resource_group.cloudops.location

  os_type  = "Linux"
  sku_name = "F1"
}

# 3. Create Python Web App
resource "azurerm_linux_web_app" "cloudops" {
  name                = "sameed-cloudops-dashboard-20261030"
  resource_group_name = azurerm_resource_group.cloudops.name
  location            = azurerm_resource_group.cloudops.location
  service_plan_id     = azurerm_service_plan.cloudops.id

  https_only = true

  site_config {
    always_on = false

    application_stack {
      python_version = "3.14"
    }
  }

  app_settings = {
    SCM_DO_BUILD_DURING_DEPLOYMENT = "true"
  }
}

# 4. Display Web App URL
output "web_app_url" {
  value = "https://${azurerm_linux_web_app.cloudops.default_hostname}"
}
