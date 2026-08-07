class BoletoService:
    def __init__(self):
        pass

    def generate_boleto(self, amount: float, recipient: str):
        return {"status": "generated", "amount": amount, "recipient": recipient}

class CategoryService:
    def __init__(self):
        pass

    def list_categories(self):
        return ["Receitas", "Despesas Fixas", "Investimentos"]
