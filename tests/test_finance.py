import sys
from pathlib import Path

api_dir = Path(__file__).resolve().parent.parent / "apps" / "api"
if str(api_dir) not in sys.path:
    sys.path.insert(0, str(api_dir))

import pytest
from app.modules.finance.services import BoletoService, CategoryService

def test_boleto_service():
    service = BoletoService()
    result = service.generate_boleto(100.0, "Cliente X")
    assert result["status"] == "generated"
    assert result["amount"] == 100.0

def test_category_service():
    service = CategoryService()
    categories = service.list_categories()
    assert "Receitas" in categories
