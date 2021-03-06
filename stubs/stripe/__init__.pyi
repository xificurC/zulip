import stripe.error as error
import stripe.util as util

from typing import Optional, Any, Dict, List

api_key: Optional[str]

class Customer:
    default_source: Card
    created: int
    id: str
    subscriptions: List[Subscription]

    @staticmethod
    def retrieve(customer_id: str, expand: Optional[List[str]]) -> Customer:
        ...
    @staticmethod
    def create(description: str, metadata: Dict[str, Any], source: str) -> Customer:
        ...

class Invoice:
    amount_due: int
    @staticmethod
    def upcoming(customer: str) -> Invoice:
        ...

class Subscription:
    created: int
    status: str
    @staticmethod
    def create(customer: str, billing: str, items: List[Dict[str, Any]],
               prorate: bool, tax_percent: float) -> Subscription:
        ...

class Card:
    last4: str

class Plan:
    id: str
    @staticmethod
    def create(currency: str, interval: str, product: str, amount: int,
               billing_scheme: str, nickname: str, usage_type: str) -> Plan:
        ...

class Product:
    id: str

    @staticmethod
    def create(name: str, type: str, statement_descriptor: str, unit_label: str) -> Product:
        ...
